import socket, sys

print("Port Scanner v1.0")
print("Copyright (c) 2020 miniprime1\n")

target = input("Enter Target IP: ")

print("")
try:
    for port in range(1, 65535): 
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        socket.setdefaulttimeout(1) 
        result = s.connect_ex((target,port)) 
        if result == 0: print("Port {} is open".format(port)) 
        s.close() 

except KeyboardInterrupt: 
    print("\nError: KeyboardInterrupt") 

except socket.gaierror: 
    print("\nError: Hostname Could Not Be Resolved")  

except socket.error: 
    print("\nError: Server not responding")

finally:
    input("\nPress enter key to exit")
    sys.exit()