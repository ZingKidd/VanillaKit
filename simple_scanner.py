import socket

def target_ip():
    ip = input('Enter target ip : ')
    return ip

def select_ports_to_scan():
    ports = input('Enter the range of the ports that you want to scan : ')
    return int(ports)

def scan(ip, ports):
    for port in range(1, ports):
        scan_port(ip, port)

def scan_port(ip, port):
    try:
        soc = socket.socket()
        soc.connect((ip, port))
        try:
            print('Port ' + str(port))
        except:
            pass
    except:
        pass

ip = target_ip()
ports = select_ports_to_scan()
scan(ip, ports)