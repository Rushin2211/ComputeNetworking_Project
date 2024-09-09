import socket


def server(sock, address):

    print("已成功连接", address)

    try:
        data = sock.recv(10000).decode()

        print(data)

        file_path = data.split()[1]

        file = open(file_path[1:], 'r', encoding='UTF-8')

        output_data = file.read()

        file.close()

        output_data = 'HTTP/1.1 200 OK\r\n\r\n' + output_data

        print(output_data)

        for i in range(0, len(output_data)):

            sock.send(output_data[i].encode())

        sock.close()

    except FileNotFoundError:

        output_data = 'HTTP/1.1 404 Not Found\r\n\r\n'

        print(output_data)

        for j in range(0, len(output_data)):

            sock.send(output_data[j].encode())

        sock.close()


server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_sock.bind(("", 80))

server_sock.listen(1)

print("正在等待连接......")

while True:
    sock, address = server_sock.accept()

    server(sock, address)
