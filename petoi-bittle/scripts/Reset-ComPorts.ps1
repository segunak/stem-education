# Function to run a command as administrator
function Invoke-AsAdmin {
    param (
        [string]$Command,
        [string]$Arguments
    )
    Start-Process -FilePath "powershell.exe" -ArgumentList "-Command $Command $Arguments" -Verb RunAs -Wait -PassThru
}

# Function to toggle Bluetooth COM ports
function Set-BluetoothPorts {
    param (
        [string]$Action
    )
    try {
        # Get the path to devcon.exe in the same directory as the script
        $devconPath = Join-Path -Path $MyInvocation.PSScriptRoot -ChildPath "devcon.exe"

        # Check if devcon.exe exists
        if (-not (Test-Path $devconPath)) {
            Write-Output "devcon.exe not found in the script directory."
            return $false
        }

        # List all COM ports
        $ports = Get-WmiObject Win32_SerialPort
        $btPorts = $ports | Where-Object { $_.Description -like "*Bluetooth*" }

        if ($btPorts.Count -eq 0) {
            Write-Output "No Bluetooth COM ports found."
            return $false
        }

        foreach ($port in $btPorts) {
            if ($Action -eq 'disable') {
                $result = Invoke-AsAdmin -Command $devconPath -Arguments "disable $($port.DeviceID)"
                if ($result.ExitCode -eq 0) {
                    Write-Output "Disabled $($port.DeviceID)"
                } else {
                    Write-Output "Failed to disable $($port.DeviceID): $($result.StandardError)"
                }
            } elseif ($Action -eq 'enable') {
                $result = Invoke-AsAdmin -Command $devconPath -Arguments "enable $($port.DeviceID)"
                if ($result.ExitCode -eq 0) {
                    Write-Output "Enabled $($port.DeviceID)"
                } else {
                    Write-Output "Failed to enable $($port.DeviceID): $($result.StandardError)"
                }
            } else {
                throw "Invalid action. Use 'disable' or 'enable'."
            }
        }

        return $true
    } catch {
        Write-Output "An error occurred: $_"
        return $false
    }
}

# Main function to disable and then re-enable Bluetooth COM ports
function Disable-AndEnableBluetoothPorts {
    try {
        Write-Output "Disabling Bluetooth COM ports..."
        if (Set-BluetoothPorts -Action 'disable') {
            Start-Sleep -Seconds 5  # Wait for 5 seconds before re-enabling
            Write-Output "Re-enabling Bluetooth COM ports..."
            if (Set-BluetoothPorts -Action 'enable') {
                Write-Output "Bluetooth COM ports have been re-enabled."
            } else {
                Write-Output "Failed to re-enable Bluetooth COM ports."
            }
        } else {
            Write-Output "No Bluetooth COM ports were disabled."
        }
    } catch {
        Write-Output "An error occurred during the process: $_"
    }
}

Disable-AndEnableBluetoothPorts