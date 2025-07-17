

def toggle_com_ports(enable=True):
    """Disable or enable all COM ports on Windows."""
    action = "enable" if enable else "disable"
    print(f"{'Enabling' if enable else 'Disabling'} all COM ports...")

    # Try devcon command to disable/enable COM ports
    try:
        # List all COM ports
        com_ports_output = subprocess.check_output("wmic path Win32_SerialPort get DeviceID", shell=True).decode()
        com_ports = [line.strip() for line in com_ports_output.splitlines() if "COM" in line]

        for port in com_ports:
            # Run the disable/enable command for each COM port
            subprocess.run(f"devcon {action} {port}", shell=True, check=True)
            print(f"{'Enabled' if enable else 'Disabled'} {port}")

    except Exception as e:
        print(f"Failed to {action} COM ports with devcon. Trying PowerShell commands.")
        
        # If devcon fails, use PowerShell as a fallback
        for com_port in com_ports:
            try:
                command = f"Get-PnpDevice | Where-Object {{ $_.InstanceId -like '*{com_port}*' }} | Disable-PnpDevice -Confirm:$false" if not enable else \
                          f"Get-PnpDevice | Where-Object {{ $_.InstanceId -like '*{com_port}*' }} | Enable-PnpDevice -Confirm:$false"
                subprocess.run(["powershell", "-Command", command], check=True)
                print(f"{'Enabled' if enable else 'Disabled'} {com_port}")
            except Exception as ps_e:
                print(f"PowerShell failed for {com_port}: {ps_e}")

# Disable all COM ports, wait a moment, then enable them
toggle_com_ports(enable=False)
time.sleep(2)  # Wait for a few seconds
toggle_com_ports(enable=True)
