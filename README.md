How to Set Up and Install the BEE Network Tool on Kali Linux and Termux
Welcome to this comprehensive guide on how to set up and install the BEE Network Tool on both Kali Linux and Termux. Whether you're using a Linux system or the lightweight Termux environment on Android, this guide will help you install and use the BEE Network Tool efficiently.

Setting Up on Kali Linux
Step 1: Update and Upgrade Kali Linux
Start by ensuring your system is up to date. Open your terminal and run:

bash
Copy code
sudo apt update
sudo apt upgrade -y
Step 2: Install Git and Python
Install git and python3:

bash
Copy code
sudo apt install git python3 python3-venv -y
Step 3: Clone Your Repository
Clone the BEE Network Tool repository and navigate to the project directory:

bash
Copy code
git clone https://github.com/Codeblackspider/beenetwork.git
cd beenetwork
Step 4: Create and Activate a Virtual Environment
Create a virtual environment:

bash
Copy code
python3 -m venv venv
Activate it:

bash
Copy code
source venv/bin/activate
Step 5: Install Project Dependencies
Install the necessary Python packages:

bash
Copy code
pip install -r requirements.txt
Step 6: Run the BEE Network Tool
Run the tool using:

bash
Copy code
python3 beenet.py
Setting Up on Termux
Step 1: Update and Upgrade Termux
Start by updating Termux to ensure all packages are up to date:

bash
Copy code
pkg update
pkg upgrade -y
Step 2: Install Git and Python
Install git and python3:

bash
Copy code
pkg install git python -y
Step 3: Clone Your Repository
Clone the BEE Network Tool repository and navigate to the project directory:

bash
Copy code
git clone https://github.com/Codeblackspider/beenetwork.git
cd beenetwork
Step 4: Create and Activate a Virtual Environment
Install python3-venv and create a virtual environment:

bash
Copy code
pkg install python3-venv -y
python3 -m venv venv
Activate the virtual environment:

bash
Copy code
source venv/bin/activate
Step 5: Install Project Dependencies
Install the required packages:

bash
Copy code
pip install -r requirements.txt
Step 6: Run the BEE Network Tool
Run the tool with:

bash
Copy code
python3 beenet.py
Using the BEE Network Tool
Here’s a brief overview of the functions available in the BEE Network Tool and how to use them:

1. IP Finder
Description: Find the IP address associated with a given URL.
Usage: Choose option 1, enter the URL, and the tool will display the IP address.
2. Vulnerable Port Scanner
Description: Scan a target for common vulnerable ports.
Usage: Choose option 2, enter the target IP or hostname, and the tool will scan and display open vulnerable ports.
3. Custom Port Scanner
Description: Scan specific ports on a target.
Usage: Choose option 3, enter the target IP or hostname and the ports to scan, and the tool will display open ports.
4. Ping Test
Description: Test the reachability of a host using ping.
Usage: Choose option 4, enter the IP address or hostname, and the tool will perform a ping test and display the results.
5. Traceroute
Description: Trace the path packets take to a target.
Usage: Choose option 5, enter the target IP or hostname, and the tool will display the traceroute.
6. Service Version Detection
Description: Detect service versions running on open ports.
Usage: Choose option 6, enter the target IP or hostname and the ports to scan, and the tool will detect and display service versions.
7. DNS Lookup
Description: Perform a DNS lookup for a domain to find its IP address.
Usage: Choose option 7, enter the domain, and the tool will display the associated IP address.
8. Subnet Calculator
Description: Calculate network information based on IP address and subnet mask.
Usage: Choose option 8, enter the IP address and subnet mask, and the tool will display network details.
9. Port Service Lookup
Description: Find out which service is associated with a specific port.
Usage: Choose option 9, enter the port number, and the tool will display the associated service.
10. Reverse DNS Lookup
Description: Perform a reverse DNS lookup to find the hostname associated with an IP address.
Usage: Choose option 10, enter the IP address, and the tool will display the associated hostname.
11. Network Interface Information
Description: Display information about the network interfaces on the system.
Usage: Choose option 11, and the tool will display details of each network interface.
