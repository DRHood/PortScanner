import socket
import threading

# User input for target Ip address
target = input("Enter target IP address to scan: ")

def port_scanner(port):
    try:   
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(5)
        con = s.connect((target,port))
        print(f'The port {port} is open')
        con.close()
    except:
        pass

# Scanning ports using threading for speed
for port in range(start_port, end_port+1):
    thread = threading.Thread(target = port_scanner, args = (port, ))
    thread.start()