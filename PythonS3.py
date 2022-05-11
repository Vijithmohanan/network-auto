import getpass
import sys
import telnetlib

HOST = "192.168.232.134" 
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
tn.write(b"vlan 2\r")
tn.write(b"name Students\r")
tn.write(b"exit\r")
tn.write(b"vlan 3\r")
tn.write(b"name Staffs\r")
tn.write(b"vlan 4\r")
tn.write(b"name Research\r")
tn.write(b"exit\r")

tn.write(b"end\r")
tn.write(b"exit\r")

print(tn.read_all().decode('ascii'))
