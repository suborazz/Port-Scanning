import socket
import threading
from datetime import datetime

# Function to scan a single port
def scan_port(target_ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)
            result = sock.connect_ex((target_ip, port))
            if result == 0:
                print(f"Port {port}: Open")
    except Exception as e:
        print(f"Error scanning port {port}: {e}")

# Get user input for target
target = input("Enter the host to be scanned: ")

try:
    target_ip = socket.gethostbyname(target)
    print(f"Scanning target {target_ip}...")
except socket.gaierror:
    print("Invalid host. Please enter a valid hostname or IP address.")
    exit()

# Define port range
start_port = 1
end_port = 1024

# Record the start time
start_time = datetime.now()

# Use threading for faster scanning
threads = []
for port in range(start_port, end_port + 1):
    thread = threading.Thread(target=scan_port, args=(target_ip, port))
    threads.append(thread)
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()

# Record the end time
end_time = datetime.now()
print(f"Scanning completed in: {end_time - start_time}") 
