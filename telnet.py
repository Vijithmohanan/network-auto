import getpass
import sys
import telnetlib

HOST = "192.168.232.131"
user = input("Enter your telnet username: ")  
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username:")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password:")
    tn.write(password.encode('ascii') + b"\r")

tn.write(b"enable\r")
tn.write(b"cisco\r")
tn.write(b"conf t\r")
tn.write(b"int loop 0\r")
tn.write(b"ip address 1.1.1.1 255.255.255.255\r")
tn.write(b"int loop 1\r")
tn.write(b"ip address 2.2.2.2 255.255.255.255\r")
tn.write(b"router ospf 1\r")
tn.write(b"network 0.0.0.0 255.255.255.255 area 0\r")
tn.write(b"end\r")
tn.write(b"exit\r")

print(tn.read_all().decode('ascii'))
