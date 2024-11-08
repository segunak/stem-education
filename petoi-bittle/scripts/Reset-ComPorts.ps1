# Ensure running with admin privileges
if (-not ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole] "Administrator")) {
    Write-Host "This script requires administrator privileges. Please re-run as administrator."
    exit
}

# Check for devcon.exe in the script's directory
$devconPath = Join-Path -Path (Split-Path -Parent $MyInvocation.MyCommand.Path) -ChildPath "devcon.exe"
if (-not (Test-Path $devconPath)) {
    Write-Host "devcon.exe not found in the script directory. Please place devcon.exe in the same directory as this script."
    exit
}

# Retrieve a list of all COM ports
Write-Output "Listing all detected COM ports..."
$allPorts = & $devconPath find "Ports"
if ($allPorts.Count -eq 0) {
    Write-Output "No COM ports found."
    exit
}

# Display each port with its description
foreach ($port in $allPorts) {
    if ($port -match "(\S+)\s+\((COM\d+)\)") {
        $deviceDescription = $matches[1]
        $comName = $matches[2]
        Write-Output "Found: $deviceDescription ($comName)"
    }
}

# Retrieve list of Bluetooth-linked COM ports
Write-Output "`nGetting list of Bluetooth-linked COM ports..."
$comPorts = $allPorts | Where-Object { $_ -match "Standard Serial over Bluetooth link \(COM\d+\)" }

if ($comPorts.Count -eq 0) {
    Write-Output "No Bluetooth-linked COM ports found."
    exit
}

# Disable all Bluetooth-linked COM ports
Write-Output "`nDisabling all Bluetooth-linked COM ports..."
foreach ($port in $comPorts) {
    if ($port -match "\\Device\\(\S+)\s+\(COM\d+\)") {
        $deviceId = $matches[1]
        Write-Output "Disabling $deviceId..."
        & $devconPath disable $deviceId | Out-Null
        Start-Sleep -Milliseconds 500
    }
}

# Pause briefly before re-enabling
Start-Sleep -Seconds 2

# Enable all Bluetooth-linked COM ports
Write-Output "`nEnabling all Bluetooth-linked COM ports..."
foreach ($port in $comPorts) {
    if ($port -match "\\Device\\(\S+)\s+\(COM\d+\)") {
        $deviceId = $matches[1]
        Write-Output "Enabling $deviceId..."
        & $devconPath enable $deviceId | Out-Null
        Start-Sleep -Milliseconds 500
    }
}

Write-Output "All Bluetooth-linked COM ports have been processed."
