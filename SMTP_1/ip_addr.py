import socket


qq_server = 'smtp.qq.com'

wy_server = 'smtp.163.com'

ip_addr = socket.gethostbyname(wy_server)

print(ip_addr)
