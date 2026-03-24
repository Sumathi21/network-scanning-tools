import subprocess
import platform

print(" Ping Scanner")

# taking IP address or website from user
ip = input("Enter IP address or website: ")

# checking operating system
# Windows uses -n and Linux/Mac uses -c
if platform.system().lower() == "windows":
    count = "-n"
else:
    count = "-c"

# creating the ping command
command = ["ping", count, "4", ip]

# running the command using subprocess module
result = subprocess.run(command, stdout=subprocess.PIPE, text=True)

print("\nPing Output:\n")

# printing the result of the ping command
print(result.stdout)