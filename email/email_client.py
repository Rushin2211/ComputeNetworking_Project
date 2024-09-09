import sys
import socket
import base64
import time
import image_rc
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class LoginWindow(QWidget):

    def __init__(self):

        super().__init__()

        self.resize(360, 300)

        self.setWindowFlag(Qt.FramelessWindowHint)

        self.setWindowIcon(QIcon(':IMAGES/icon'))

        self.setWindowTitle("MailSpace")

        layout = QVBoxLayout()
        layout.addStretch(1)

        title = QLabel("MailSpace")
        title.setAlignment(Qt.AlignCenter)
        title.setFont(QFont("Arial", 16))
        layout.addWidget(title)
        layout.addStretch(1)

        self.email_addr = QLineEdit()
        self.email_addr.setPlaceholderText("E-mail address")
        self.email_addr.setFont(QFont("Arial", 15))
        layout.addWidget(self.email_addr)
        layout.addStretch(1)

        self.email_password = QLineEdit()
        self.email_password.setPlaceholderText("E-mail authorization code")
        self.email_password.setFont(QFont("Arial", 15))
        layout.addWidget(self.email_password)
        layout.addStretch(2)
        self.email_password.setEchoMode(QLineEdit.Password)
        self.email_password.returnPressed.connect(self.login_button_click)

        login_button = QPushButton("login")
        login_button.setFont(QFont("Arial", 15))
        layout.addWidget(login_button)
        layout.addStretch(1)
        login_button.clicked.connect(self.login_button_click)

        exit_button = QPushButton("exit")
        exit_button.setFont(QFont("Arial", 15))
        layout.addWidget(exit_button)
        layout.addStretch(1)
        exit_button.clicked.connect(self.exit_button_click)

        self.setLayout(layout)

    def exit_button_click(self):

        sys.exit()

    def login_button_click(self):

        global email_addr, email_password, mail_server

        email_addr = self.email_addr.text()

        email_password = self.email_password.text()

        mail_name = email_addr.partition("@")[2]

        mail_server = 'smtp.' + mail_name

        if email_addr == 'admin@qq.com' and email_password == '123456':

            email_addr = '1912577205@qq.com'

            email_password = 'uwhumeqmfytobbac'

            QCoreApplication.instance().quit()

        elif email_addr == 'admin@163.com' and email_password == '654321':

            email_addr = 'komorebi2211@163.com'

            email_password = 'YKJEATPGIHJRDMTE'

            QCoreApplication.instance().quit()

        else:

            message_box = QMessageBox(QMessageBox.Warning, 'MailSpace', 'Warning: The e-mail address or e-mail '
                                                                        'authorization code is incorrect!')

            message_box.setIconPixmap(QPixmap(':IMAGES/icon'))

            message_box.exec()


class SendWindow(QWidget):

    def __init__(self):

        super().__init__()

        self.resize(600, 400)

        self.setWindowFlag(Qt.FramelessWindowHint)

        self.setWindowTitle("MailSpace")

        self.setWindowIcon(QIcon(':IMAGES/icon'))

        layout = QVBoxLayout()
        layout.addStretch(1)

        title = QLabel("MailSpace")
        title.setAlignment(Qt.AlignCenter)
        title.setFont(QFont("Arial", 16))
        layout.addWidget(title)
        layout.addStretch(1)

        self.recipient_addr = QLineEdit()
        self.recipient_addr.setPlaceholderText("Recipient address")
        self.recipient_addr.setFont(QFont("Arial", 15))
        layout.addWidget(self.recipient_addr)
        layout.addStretch(1)

        self.subject_edit = QLineEdit()
        self.subject_edit.setPlaceholderText("Subject")
        self.subject_edit.setFont(QFont("Arial", 15))
        layout.addWidget(self.subject_edit)
        layout.addStretch(1)

        self.content_edit = QLineEdit()
        self.content_edit.setPlaceholderText("Content")
        self.content_edit.setFont(QFont("Arial", 15))
        layout.addWidget(self.content_edit)
        layout.addStretch(1)

        send_button = QPushButton("Send")
        send_button.setFont(QFont("Arial", 15))
        layout.addWidget(send_button)
        layout.addStretch(1)
        send_button.clicked.connect(self.SendButton)

        exit_button = QPushButton("Exit")
        exit_button.setFont(QFont("Arial", 15))
        layout.addWidget(exit_button)
        layout.addStretch(1)
        exit_button.clicked.connect(self.ExitButton)

        self.setLayout(layout)

    def SendButton(self):

        recipient = self.recipient_addr.text()
        if recipient == 'admin@qq.com':
            recipient = '1912577205@qq.com'
        elif recipient == 'admin@163.com':
            recipient = 'komorebi2211@163.com'
        subject = self.subject_edit.text()
        content = self.content_edit.text()

        message = 'From: ' + email_addr + '\r\n'
        message = message + 'To: ' + recipient + '\r\n'
        message = message + 'Subject: ' + subject + '\r\n'
        message = message + '\r\n' + content + '\r\n'
        end_message = '.' + '\r\n'

        client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            client_sock.connect((mail_server, 25))
            client_sock.settimeout(1)
            recv_message = client_sock.recv(10000)
            recv_message = recv_message.decode()
            print(recv_message)
        except:
            message_box = QMessageBox(QMessageBox.Warning, 'MailSpace', 'Please check your network')
            message_box.setIconPixmap(QPixmap(':IMAGES/icon'))
            message_box.exec()

        helo_command = 'HELO ' + mail_server + '\r\n'
        print(helo_command)
        while True:
            client_sock.send(helo_command.encode())
            recv_message = client_sock.recv(10000)
            recv_message = recv_message.decode()
            print(recv_message)
            if recv_message[:3] == '250':
                break
            else:
                message_box = QMessageBox(QMessageBox.Warning, 'MailSpace', 'Warning: E-mail delivery failed')
                message_box.setIconPixmap(QPixmap(':IMAGES/icon'))
                message_box.exec()
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
            else:
                message_box = QMessageBox(QMessageBox.Warning, 'MailSpace', 'Warning: E-mail delivery failed')
                message_box.setIconPixmap(QPixmap(':IMAGES/icon'))
                message_box.exec()
                break

        UserName_command = base64.b64encode(email_addr.encode()) + b'\r\n'
        print(UserName_command)
        while True:
            client_sock.send(UserName_command)
            recv_message = client_sock.recv(10000)
            recv_message = recv_message.decode()
            print(recv_message)
            if recv_message[:3] == '334':
                break
            else:
                message_box = QMessageBox(QMessageBox.Warning, 'MailSpace', 'Warning: E-mail delivery failed')
                message_box.setIconPixmap(QPixmap(':IMAGES/icon'))
                message_box.exec()
                break

        PassWord_command = base64.b64encode(email_password.encode()) + b'\r\n'
        print(PassWord_command)
        while True:
            client_sock. send(PassWord_command)
            recv_message = client_sock.recv(10000)
            recv_message = recv_message.decode()
            print(recv_message)
            if recv_message[:3] == '235':
                break
            else:
                message_box = QMessageBox(QMessageBox.Warning, 'MailSpace', 'Warning: E-mail delivery failed')
                message_box.setIconPixmap(QPixmap(':IMAGES/icon'))
                message_box.exec()
                break

        MailFrom_command = 'MAIL FROM: <' + email_addr + '>' + '\r\n'
        print(MailFrom_command)
        while True:
            client_sock.send(MailFrom_command.encode())
            recv_message = client_sock.recv(10000)
            recv_message = recv_message.decode()
            print(recv_message)
            if recv_message[:3] == '250':
                break
            else:
                message_box = QMessageBox(QMessageBox.Warning, 'MailSpace', 'Warning: E-mail delivery failed')
                message_box.setIconPixmap(QPixmap(':IMAGES/icon'))
                message_box.exec()
                break

        RcptTo_command = 'RCPT TO: <' + recipient + '>' + '\r\n'
        print(RcptTo_command)
        while True:
            client_sock.send(RcptTo_command.encode())
            recv_message = client_sock.recv(10000)
            recv_message = recv_message.decode()
            print(recv_message)
            if recv_message[:3] == '250':
                break
            else:
                message_box = QMessageBox(QMessageBox.Warning, 'MailSpace', 'Warning: E-mail delivery failed')
                message_box.setIconPixmap(QPixmap(':IMAGES/icon'))
                message_box.exec()
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
            else:
                message_box = QMessageBox(QMessageBox.Warning, 'MailSpace', 'Warning: E-mail delivery failed')
                message_box.setIconPixmap(QPixmap(':IMAGES/icon'))
                message_box.exec()
                break

        client_sock.send(message.encode())
        print(message)
        while True:
            client_sock.send(end_message.encode())
            recv_message = client_sock.recv(10000)
            recv_message =recv_message.decode()
            print(recv_message)
            if recv_message[:3] == '250':
                break
            else:
                message_box = QMessageBox(QMessageBox.Warning, 'MailSpace', 'Warning: E-mail delivery failed')
                message_box.setIconPixmap(QPixmap(':IMAGES/icon'))
                message_box.exec()
                break

        Quit_command = 'QUIT' + '\r\n'
        print(Quit_command)
        while True:
            client_sock.send(Quit_command.encode())
            recv_message = client_sock.recv(10000)
            recv_message = recv_message.decode()
            print(recv_message)
            if recv_message[:3] == '221':
                message_box = QMessageBox(QMessageBox.Information, 'MailSpace', 'E-mail delivery successful')
                message_box.setIconPixmap(QPixmap(':IMAGES/icon'))
                message_box.exec()
                break
            else:
                message_box = QMessageBox(QMessageBox.Warning, 'MailSpace', 'Warning: E-mail delivery failed')
                message_box.setIconPixmap(QPixmap(':IMAGES/icon'))
                message_box.exec()
                break

    def ExitButton(self):

        sys.exit()


application = QApplication(sys.argv)

login_window = LoginWindow()

login_window.show()

application.exec()

time.sleep(1)

del login_window

send_window = SendWindow()

send_window.show()

application.exec()
