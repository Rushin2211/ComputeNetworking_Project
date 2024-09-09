import socket
import base64
import time


mail_server = 'smtp.qq.com'

mail_user_addr = '1912577205@qq.com'

mail_user_password = 'uwhumeqmfytobbac'

mail_recipient_addr = 'komorebi2211@163.com'


# mail_server = 'smtp.163.com'
#
# mail_user_addr = 'komorebi2211@163.com'
#
# mail_user_password = 'YKJEATPGIHJRDMTE'
#
# mail_recipient_addr = '1912577205@qq.com'


client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_sock.connect((mail_server, 25))

recv_message = client_sock.recv(10000)

recv_message = recv_message.decode()

print(recv_message)

if recv_message[:3] != '220':

    print("未收到来自服务器的响应")


helo_command = 'HELO ' + mail_server + '\r\n'

print(helo_command)

while True:

    client_sock.send(helo_command.encode())

    recv_message = client_sock.recv(10000)

    recv_message = recv_message.decode()

    print(recv_message)

    if recv_message[:3] == '250':

        break


login_command = 'auth login' + '\r\n'

print(login_command)

while True:

    client_sock.send(login_command.encode())

    recv_message = client_sock.recv(10000)

    recv_message = recv_message.decode()

    print(recv_message)

    if recv_message[:3] == '334':

        break


UserName_command = base64.b64encode(mail_user_addr.encode()) + b'\r\n'

print(UserName_command)

while True:

    client_sock.send(UserName_command)

    recv_message = client_sock.recv(10000)

    recv_message = recv_message.decode()

    print(recv_message)

    if recv_message[:3] == '334':

        break


PassWord_command = base64.b64encode(mail_user_password.encode()) + b'\r\n'

print(PassWord_command)

while True:

    client_sock.send(PassWord_command)

    recv_message = client_sock.recv(10000)

    recv_message = recv_message.decode()

    print(recv_message)

    if recv_message[:3] == '235':

        break


MailFrom_command = 'MAIL FROM: <' + mail_user_addr + '>' + '\r\n'

print(MailFrom_command)

while True:

    client_sock.send(MailFrom_command.encode())

    recv_message = client_sock.recv(10000)

    recv_message = recv_message.decode()

    print(recv_message)

    if recv_message[:3] == '250':

        break


RcptTo_command = 'RCPT TO: <' + mail_recipient_addr + '>' + '\r\n'

print(RcptTo_command)

while True:

    client_sock.send(RcptTo_command.encode())

    recv_message = client_sock.recv(10000)

    recv_message = recv_message.decode()

    print(recv_message)

    if recv_message[:3] == '250':

        break


Data_command = 'DATA' + '\r\n'

print(Data_command)

while True:

    client_sock.send(Data_command.encode())

    recv_message = client_sock.recv(10000)

    recv_message = recv_message.decode()

    print(recv_message)

    if recv_message[:3] == '354':

        break


message = 'From: ' + mail_user_addr + '\r\n'

message = message + 'To: ' + mail_recipient_addr + '\r\n'

message = message + 'Subject: ' + '你好' + '\r\n'

message = message + '\r\n' + '你好' + '\r\n'

client_sock.send(message.encode())


end_message = '.' + '\r\n'

while True:

    client_sock.send(end_message.encode())

    recv_message = client_sock.recv(10000)

    recv_message = recv_message.decode()

    print(recv_message)

    if recv_message[:3] == '250':

        break


Quit_command = 'QUIT' + '\r\n'

print(Quit_command)

while True:

    client_sock.send(Quit_command.encode())

    recv_message = client_sock.recv(10000)

    recv_message = recv_message.decode()

    print(recv_message)

    if recv_message[:3] == '221':

        break


time.sleep(1000000)
