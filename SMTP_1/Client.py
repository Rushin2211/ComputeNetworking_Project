import socket
import base64
import getpass
import time


while True:

    print("请先登陆邮箱")

    print("")

    mail_user_addr = input("请输入发件人的邮箱地址: ")

    print("")

    mail_user_password = getpass.getpass("请输入发件人的邮箱密码: ")

    print("")

    if mail_user_addr == '1912577205@qq.com' and mail_user_password == 'Zzx133802470z':

        print("登陆成功")

        print("")

        mail_server = 'smtp.qq.com'

        mail_user_password = 'uwhumeqmfytobbac'

        break

    elif mail_user_addr != '1912577205@qq.com' and mail_user_password == 'Zzx133802470z':

        print("邮箱地址不存在,请重新输入")

        print("")

        continue

    elif mail_user_addr == '1912577205@qq.com' and mail_user_password != 'Zzx133802470z':

        print("密码错误,请重新输入")

        print("")

        continue

    if mail_user_addr == 'komorebi2211@163.com' and mail_user_password == 'Zzx133802470z':

        print("登陆成功")

        print("")

        mail_server = 'smtp.163.com'

        mail_user_password = 'YKJEATPGIHJRDMTE'

        break

    elif mail_user_addr != 'komorebi2211@163.com' and mail_user_password == 'Zzx133802470z':

        print("邮箱地址不存在,请重新输入")

        print("")

        continue

    elif mail_user_addr == 'komorebi2211@163.com' and mail_user_password != 'Zzx133802470z':

        print("密码错误,请重新输入")

        print("")

        continue


mail_recipient_addr = input("请输入收件人的邮箱地址: ")

print("")


message = 'From: ' + mail_user_addr + '\r\n'

message = message + 'To: ' + mail_recipient_addr + '\r\n'

subject = input("请输入邮件主题: ")

print("")

message = message + 'Subject: ' + subject + '\r\n'

content = input("请输入邮件内容: ")

print("")

message = message + '\r\n' + content + '\r\n'

end_message = '.' + '\r\n'

client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_sock.connect((mail_server, 25))

recv_message = client_sock.recv(10000)

recv_message = recv_message.decode('utf-8')

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

    recv_message = recv_message.decode('utf-8')

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


client_sock.send(message.encode())

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


time.sleep(1000)
