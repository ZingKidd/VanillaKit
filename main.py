import socket
from os import remove
from sys import argv

def self_delete():
    remove(argv[0])

def find_ip(hostname):
    hostname = socket.gethostname()
    return socket.gethostbyname(hostname)


hostname = socket.gethostname()
print(f"Hostname: {hostname}")
print(f"IP Address: {find_ip(hostname)}")