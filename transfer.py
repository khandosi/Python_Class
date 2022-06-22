import socket
from time import sleep

# Initialize variables
target_host = input("Please enter the target IP: ")
save_file = input("Enter the name of the file you want to write the scans to: ")

results = []

# Define port range, set timeout to 0.1 (This is POC, in real world change to suit your latency), open a TCP socket for the specified port, attempt a connection over the specified port. For TCP, a result of 0 indicates a connection was successful. Lastly, close the connection.
def tcp_scan():

    for port in range(7995, 8005):
        socket.setdefaulttimeout(0.1)
        print("Scanning port " + str(port) + " on " + target_host)
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = client.connect_ex((target_host, port))
        if result == 0:
            results.append("\nOpen connection found on TCP port " + str(port))
        client.close()
    return results


# Define port range, set timeout to 0.1 (This is POC, in real world change to suit your latency), open a UDP socket for the specified port, attempt a connection over the specified port. Lastly, close the connection.
def udp_scan():

    for port in range(7995, 8005):
        print("Scanning port " + str(port) + " on " + target_host)
        client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        socket.setdefaulttimeout(0.1)
        result = client.connect_ex((target_host, port))
        if result == 0:
            results.append("\nOpen connection found on UDP port " + str(port))
    client.close()
    return results


# Initiate the scans
print("\nStarting TCP scan\n")
sleep(1)
tcp_scan()
print("\nStarting UDP scan\n")
sleep(1)
udp_scan()

# Append results to the specified file, then close the file
f = open(save_file, "a")

for line in results:
    f.write(line)

f.close()
