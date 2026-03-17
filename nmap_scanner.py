# Nmap Scanner
# Name: Sumathi
# This program performs basic network scanning using Nmap

import subprocess

print("----- Nmap Scanner -----")

# taking target IP from user
target = input("Enter target IP address: ")

print("\nSelect Scan Type")
print("1. Host Discovery")
print("2. Port Scan")
print("3. Service Version Detection")

# user selects type of scan
choice = input("Enter your choice: ")

# deciding which nmap command to run
if choice == "1":
    cmd = ["nmap", "-sn", target]   # checks if host is active

elif choice == "2":
    cmd = ["nmap", target]          # scans open ports

elif choice == "3":
    cmd = ["nmap", "-sV", target]   # detects service versions

else:
    print("Invalid option")
    exit()

print("\nScanning...\n")

# executing the nmap command
result = subprocess.run(cmd, stdout=subprocess.PIPE, text=True)

# displaying scan result
print(result.stdout)