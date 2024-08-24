import socket
import sys
import urllib.parse
import subprocess
import ipaddress
import psutil

# Define color codes
class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    MAGENTA = '\033[95m'
    WHITE = '\033[97m'
    RESET = '\033[0m'

# List of common vulnerable ports
VULNERABLE_PORTS = [21, 22, 23, 25, 80, 110, 143, 443, 3306, 3389]

def print_colored(text, color):
    """Prints the text in the specified color."""
    print(f"{color}{text}{Colors.RESET}")

def print_title():
    """Prints the title of the tool."""
    title = r"""
     ____               _   __     __                      __  
   / __ )___  ___     / | / /__  / /__      ______  _____/ /__
  / __  / _ \/ _ \   /  |/ / _ \/ __/ | /| / / __ \/ ___/ //_/
 / /_/ /  __/  __/  / /|  /  __/ /_ | |/ |/ / /_/ / /  / ,<   
/_____/\___/\___/  /_/ |_/\___/\__/ |__/|__/\____/_/  /_/|_| 
                                                           
"""
    print_colored(title, Colors.GREEN)
    print_colored("Visit us at: https://www.fontbees.store", Colors.CYAN)

def scan_ports(target, ports):
    """Scans the specified ports on the target and returns a list of open ports."""
    open_ports = []
    total_ports = len(ports)
    for i, port in enumerate(ports, start=1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)
            result = sock.connect_ex((target, port))
            if result == 0:
                open_ports.append(port)
        
        # Display loading bar
        percent_complete = (i / total_ports) * 100
        sys.stdout.write(f"\r{Colors.CYAN}Scanning... [{i}/{total_ports}] ({percent_complete:.2f}%)")
        sys.stdout.flush()
        
    # Clear the loading bar
    sys.stdout.write("\rDone!                        \n")
    sys.stdout.flush()
    return open_ports

def find_ip_from_url(url):
    """Finds the IP address for a given URL."""
    try:
        # Extract hostname from URL
        hostname = urllib.parse.urlparse(url).hostname
        # Resolve hostname to IP address
        ip_address = socket.gethostbyname(hostname)
        return ip_address
    except Exception as e:
        print_colored(f"Error: {e}", Colors.RED)
        return None

def ip_finder():
    """Prompts the user for a URL and displays its IP address."""
    url = input("Enter URL: ")
    ip_address = find_ip_from_url(url)
    if ip_address:
        print_colored(f"IP address of {url}: {ip_address}", Colors.GREEN)
    input("\nPress Enter to return to the menu...")
    menu()

def ping_test(target):
    """Pings the specified target and displays the results."""
    try:
        output = subprocess.check_output(['ping', '-c', '4', target], stderr=subprocess.STDOUT, universal_newlines=True)
        print_colored("Ping results:", Colors.GREEN)
        print(output)
    except subprocess.CalledProcessError as e:
        print_colored(f"Ping failed: {e.output}", Colors.RED)

def perform_ping_test():
    """Prompts the user for a target and performs a ping test."""
    target = input("Enter IP address or hostname: ")
    ping_test(target)
    input("\nPress Enter to return to the menu...")
    menu()

def traceroute(target):
    """Performs a traceroute to the specified target and displays the results."""
    try:
        output = subprocess.check_output(['traceroute', target], stderr=subprocess.STDOUT, universal_newlines=True)
        print_colored("Traceroute results:", Colors.GREEN)
        print(output)
    except subprocess.CalledProcessError as e:
        print_colored(f"Traceroute failed: {e.output}", Colors.RED)

def perform_traceroute():
    """Prompts the user for a target and performs a traceroute."""
    target = input("Enter IP address or hostname: ")
    traceroute(target)
    input("\nPress Enter to return to the menu...")
    menu()

def service_version_detection(target, ports):
    """Detects and displays the service versions running on the specified ports."""
    print("Detecting service versions...")
    for port in ports:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(1)
                sock.connect((target, port))
                sock.send(b'HEAD / HTTP/1.0\r\n\r\n')
                banner = sock.recv(1024).decode().strip()
                print_colored(f"Port {port}: {banner}", Colors.GREEN)
        except:
            print_colored(f"Port {port}: Closed or no banner detected.", Colors.RED)

def perform_service_version_detection():
    """Prompts the user for a target and ports, then performs service version detection."""
    target = input("Enter IP address or hostname: ")
    ports = [int(port) for port in input("Enter ports separated by spaces: ").split()]
    service_version_detection(target, ports)
    input("\nPress Enter to return to the menu...")
    menu()

def dns_lookup(domain):
    """Performs a DNS lookup for the specified domain and displays the IP address."""
    try:
        ip_address = socket.gethostbyname(domain)
        print_colored(f"IP address of {domain}: {ip_address}", Colors.GREEN)
    except socket.error as e:
        print_colored(f"DNS lookup failed: {e}", Colors.RED)

def subnet_calculator():
    """Calculates and displays subnet information for a given IP address and subnet mask."""
    print("\n" + Colors.MAGENTA + "="*30)
    print("Subnet Calculator")
    print(Colors.MAGENTA + "="*30 + Colors.RESET)
    
    ip_address = input("Enter IP address (e.g., 192.168.1.1): ")
    subnet_mask = input("Enter subnet mask (e.g., 255.255.255.0): ")
    
    try:
        network = ipaddress.IPv4Network(f"{ip_address}/{subnet_mask}", strict=False)
        print_colored(f"Network Address: {network.network_address}", Colors.GREEN)
        print_colored(f"Broadcast Address: {network.broadcast_address}", Colors.GREEN)
        print_colored(f"Host Range: {network.network_address + 1} - {network.broadcast_address - 1}", Colors.GREEN)
        print_colored(f"Total Hosts: {network.num_addresses - 2}", Colors.GREEN)
    except ValueError as e:
        print_colored(f"Error: {e}", Colors.RED)
    
    input("\nPress Enter to return to the menu...")
    menu()

def port_service_lookup():
    """Looks up the service associated with a specified port number."""
    print("\n" + Colors.CYAN + "="*30)
    print("Port Service Lookup")
    print(Colors.CYAN + "="*30 + Colors.RESET)
    
    try:
        port = int(input("Enter port number: "))
        service = socket.getservbyport(port)
        print_colored(f"Service running on port {port}: {service}", Colors.GREEN)
    except OSError:
        print_colored(f"Port {port} is not associated with any known service.", Colors.RED)
    except ValueError:
        print_colored("Invalid port number. Please enter a number between 1 and 65535.", Colors.RED)
    
    input("\nPress Enter to return to the menu...")
    menu()

def reverse_dns_lookup():
    """Performs a reverse DNS lookup for the specified IP address."""
    print("\n" + Colors.CYAN + "="*30)
    print("Reverse DNS Lookup")
    print(Colors.CYAN + "="*30 + Colors.RESET)
    
    ip_address = input("Enter the IP address: ")
    
    try:
        hostnames = socket.gethostbyaddr(ip_address)
        print_colored(f"Reverse DNS lookup for {ip_address}:", Colors.GREEN)
        print_colored(f"Hostname: {hostnames[0]}", Colors.GREEN)
        print_colored(f"Aliases: {', '.join(hostnames[1])}", Colors.GREEN)
    except socket.herror:
        print_colored(f"Reverse DNS lookup failed for {ip_address}.", Colors.RED)
    
    input("\nPress Enter to return to the menu...")
    menu()

def network_interface_info():
    """Displays information about the network interfaces on the system."""
    print("\n" + Colors.CYAN + "="*30)
    print("Network Interface Information")
    print(Colors.CYAN + "="*30 + Colors.RESET)
    
    interfaces = psutil.net_if_addrs()
    
    for interface, addresses in interfaces.items():
        print_colored(f"Interface: {interface}", Colors.GREEN)
        for addr in addresses:
            if addr.family == socket.AF_INET:
                print_colored(f"  IP Address: {addr.address}", Colors.GREEN)
            elif addr.family == socket.AF_INET6:
                print_colored(f"  IPv6 Address: {addr.address}", Colors.CYAN)
    
    input("\nPress Enter to return to the menu...")
    menu()

def port_scanner(vulnerable_ports=False):
    """Scans ports on the target machine. Scans for vulnerable ports if specified."""
    print("\n" + Colors.CYAN + "="*30)
    print("Port Scanner")
    print(Colors.CYAN + "="*30 + Colors.RESET)
    
    target = input("Enter IP address or hostname: ")
    if vulnerable_ports:
        ports = VULNERABLE_PORTS
    else:
        ports = [int(port) for port in input("Enter ports separated by spaces: ").split()]
    
    open_ports = scan_ports(target, ports)
    if open_ports:
        print_colored(f"Open ports: {', '.join(map(str, open_ports))}", Colors.GREEN)
    else:
        print_colored("No open ports found.", Colors.RED)
    
    input("\nPress Enter to return to the menu...")
    menu()

def custom_port_scanner():
    """Prompts the user for a target and a range of ports, then scans those ports."""
    print("\n" + Colors.CYAN + "="*30)
    print("Custom Port Scanner")
    print(Colors.CYAN + "="*30 + Colors.RESET)
    
    target = input("Enter IP address or hostname: ")
    start_port = int(input("Enter start port: "))
    end_port = int(input("Enter end port: "))
    
    if start_port < 1 or end_port > 65535 or start_port > end_port:
        print_colored("Invalid port range. Please enter valid port numbers between 1 and 65535.", Colors.RED)
        input("\nPress Enter to return to the menu...")
        menu()
    
    ports = range(start_port, end_port + 1)
    open_ports = scan_ports(target, ports)
    if open_ports:
        print_colored(f"Open ports: {', '.join(map(str, open_ports))}", Colors.GREEN)
    else:
        print_colored("No open ports found.", Colors.RED)
    
    input("\nPress Enter to return to the menu...")
    menu()

def menu():
    """Displays the main menu and handles user input."""
    while True:
        print_title()
        print("\n" + Colors.BLUE + "="*40)
        print(Colors.YELLOW + "1. IP Finder")
        print("2. Vulnerable Port Scanner")
        print("3. Custom Port Scanner")
        print("4. Ping Test")
        print("5. Traceroute")
        print("6. Service Version Detection")
        print("7. DNS Lookup")
        print("8. Subnet Calculator")
        print("9. Port Service Lookup")
        print("10. Reverse DNS Lookup")
        print("11. Network Interface Information")
        print("0. Exit")
        print(Colors.BLUE + "="*40 + Colors.RESET)
        choice = input("Select a number: ")

        if choice == '1':
            ip_finder()
        elif choice == '2':
            port_scanner(vulnerable_ports=True)
        elif choice == '3':
            custom_port_scanner()
        elif choice == '4':
            perform_ping_test()
        elif choice == '5':
            perform_traceroute()
        elif choice == '6':
            perform_service_version_detection()
        elif choice == '7':
            domain = input("Enter domain: ")
            dns_lookup(domain)
        elif choice == '8':
            subnet_calculator()
        elif choice == '9':
            port_service_lookup()
        elif choice == '10':
            reverse_dns_lookup()
        elif choice == '11':
            network_interface_info()
        elif choice == '0':
            print("Exiting...")
            break
        else:
            print_colored("Invalid selection. Please try again.", Colors.RED)

if __name__ == "__main__":
    menu()
