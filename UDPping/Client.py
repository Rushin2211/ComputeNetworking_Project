import socket
import time


client_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_addr = ('172.31.100.175', 8888)

for i in range(10):

    send_data = 'ping' + str(i)

    send_time = time.time()

    client_sock.settimeout(1)

    client_sock.sendto(send_data.encode(), server_addr)

    try:
        recv_data, s_addr = client_sock.recvfrom(10000)

        recv_time = time.time()

        interval_time = recv_time - send_time

        output_data = recv_data.decode() + "  " + "RTT:" + str(interval_time)

        time.sleep(1)

        print(output_data)

        print("")

    except:
        output_data = 'lost' + str(i)

        time.sleep(1)

        print(output_data)

        print("")

time.sleep(100)
