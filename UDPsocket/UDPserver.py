import socket


server_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

port = 888

server_sock.bind(("", port))

print("已绑定端口", port)

while True:
    data, c_address = server_sock.recvfrom(10000)

    if not data or data.decode == 'quit':

        break

    print("收到来自", c_address, "的数据")

    print("")

    server_sock.sendto(data.decode('utf-8').upper().encode('utf-8'), c_address)
