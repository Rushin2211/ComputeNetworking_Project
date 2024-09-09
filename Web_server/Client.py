import socket
import time


client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_sock.connect(('172.31.100.175', 80))

request = 'GET /C:/Users/June/Desktop/assignment/Web_server/a.txt HTTP/1.1\r\nHost:172.31.100.175\r\n'

# request = 'GET /C:/User/June/Desktop/assignment/Web_server/a.txt HTTP/1.1\r\nHost:172.31.100.175\r\n'  # 错误路径

client_sock.send(request.encode('utf-8'))

respond = b''

while True:

    character = client_sock.recv(10000)

    if not character:

        break

    respond = respond + character

print(respond.decode('utf-8'))

time.sleep(100)

client_sock.close()

