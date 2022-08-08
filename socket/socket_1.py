import socket
ipaddress = socket.gethostbyname('www.facebook.com')
print(ipaddress)
hostname = socket.gethostbyaddr(ipaddress)
print(hostname)