import subprocess

print("ARP Scanner")

# running arp command to get ARP table
result = subprocess.run(["arp", "-a"], stdout=subprocess.PIPE, text=True)

# storing output in a variable
output = result.stdout

print("\nDevices connected in the network:\n")

# printing ARP table which contains IP and MAC addresses
print(output)