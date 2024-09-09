import socket
import subprocess
import threading
import time
import tkinter as tk
from tkinter import StringVar
from tkinter import messagebox


class ClientGUI:
    running = True  # 标志变量

    def __init__(self, window):
        self.window = window
        self.window.title("SonyClientWallet")
        self.remaining_usage_time = 0
        self.server_ip = '192.168.43.34'
        self.server_port = 5200
        self.internet_connected = False
        self.false_counter = 0
        self.accounts_passwords = [
            ("0x22D68f9597A29511D7108B0ac911722f373738961",
             "0x9c2d018d47bfd48f5fb20d1616df74a1e64abf2c128cf5ad167bd65d824bbe431f8206b1b9a12ecc118539c06764b43f78bf8d89a6e625aa1b1ab372fcb508381b"),
            ("0x22D68f9597A29511D7108B0ac911722f373738962",
             "0x8ccbaff09abb4bba01a89e88381c0691df8656315a5631f70bb658ae22eff99c12b99c5286f0d81a92210c573b07caa31d5f29f8b6a445707403ee51d5fb95071c"),
            ("0x22D68f9597A29511D7108B0ac911722f373738963",
             "0x65d6c15b63df224a190575d534df5c474f46b1fa562f5c59b79fc81f20654d1e143f4f4b83bea4f53ad0f3bb67ee2826a5b3d22ff99c8c879042e467730c50a01b"),
            ("0x22D68f9597A29511D7108B0ac911722f373738964",
             "0x674785a91dc4b69fd29ee6f6a070a9e2f003816f2f982dc0fa6a914c54cbfdc574a9dd35e18b5b044fc4a3d1dbc71f07ab19089384496019161ccbc7086e91241b"),
            ("0x22D68f9597A29511D7108B0ac911722f373738965",
             "0x78769133ec9a97b97ba74ace4834d054d8cd396f3d3898a953063374b93b9643212ac8a14c3bff9614345b20b88eab7a91c44b197f32c423719e189c68e7f8f71c"),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),

        ]

        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        frame = tk.Frame(self.window)
        frame.pack(fill=tk.BOTH, expand=True)

        self.title_label = tk.Label(frame, text="Welcome to Your  WIFI-NFT Wallet!", font=("Arial", 30, "bold"))
        self.title_label.pack(side=tk.TOP, pady=10)

        self.response_text = tk.Text(frame, height=10, width=40, wrap=tk.WORD)
        self.response_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        scrollbar.config(command=self.response_text.yview)
        self.response_text.config(yscrollcommand=scrollbar.set)

        self.window_width = 700
        self.window_height = 700
        self.screen_width = self.window.winfo_screenwidth()
        self.screen_height = self.window.winfo_screenheight()
        self.x_pos = int((self.screen_width - self.window_width) / 2)
        self.y_pos = int((self.screen_height - self.window_height) / 2)

        # Set the window size
        self.window.geometry(f"{self.window_width}x{self.window_height}+{self.x_pos}+{self.y_pos}")
        self.window.resizable(False, False)  # Fix the window size

        self.network_status_label = tk.Label(self.window, text="Network Status:", font=("Arial", 16))
        self.network_status_label.pack(side="left", padx=(0, 0))
        self.network_status_indicator = tk.Label(self.window, text="未连接", fg="red", font=("Arial", 16))
        self.network_status_indicator.pack(side="left")

        self.countdown_event = threading.Event()
        self.remaining_usage_time_var = StringVar()
        # self.countdown_label = tk.Label(self.window, textvariable=self.remaining_usage_time_var)
        # self.countdown_label.pack()
        # self.countdown_label = tk.Label(self.window, textvariable=self.remaining_usage_time_var, font=("Arial", 16))
        # self.countdown_label.pack(side="bottom", pady=10)
        self.countdown_label = tk.Label(self.window, textvariable=self.remaining_usage_time_var, font=("Arial", 20))
        self.countdown_label.place(relx=0.5, rely=1.0, anchor="s")

        self.update_network_status()
        self.countdown_thread = threading.Thread(target=self.countdown)
        self.countdown_thread.start()
        self.network_status_thread = threading.Thread(target=self.check_internet_connection)
        self.network_status_thread.start()
        self.button_font = ("Arial", 12)
        self.text_font = ("Arial", 14)
        self.create_nft_buttons()

        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.close_button = tk.Button(self.window, text="Close", command=self.on_closing, width=8, height=2,
                                      font=self.button_font, bg="light pink", fg="black")
        self.close_button.pack(side=tk.RIGHT, pady=10, padx=10)

    def create_nft_buttons(self):
        nft_account = len(self.accounts_passwords)
        nft_scroll = tk.Scrollbar(self.window)
        nft_scroll.pack(side=tk.RIGHT, fill=tk.Y)  # 垂直滚动条放在界面窗口右侧

        nft_frame = tk.Frame(self.window)
        nft_frame.pack(fill=tk.BOTH)  # 填充整个宽度的框架

        nft_label = tk.Label(nft_frame, text="Your NFT assets (total number:" + str(nft_account) + ")",
                             font=("Arial", 14))
        nft_label.pack(pady=(15, 10), padx=15)  # 设置顶部的填充和边距

        # 在 nft_frame 上建立一个滚动区域
        nft_canvas = tk.Canvas(nft_frame)
        nft_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # 将滚动条与滚动区域关联
        nft_canvas.config(yscrollcommand=nft_scroll.set)
        nft_scroll.config(command=nft_canvas.yview)

        # 将按钮放置在滚动区域内的 nft_frame 上
        nft_button_frame = tk.Frame(nft_canvas)
        nft_canvas.create_window((0, 0), window=nft_button_frame, anchor=tk.NW)

        for i, account_password in enumerate(self.accounts_passwords, start=0):
            nft_button = tk.Button(nft_button_frame, text="NFT" + str(i + 1),
                                   command=lambda ap=account_password: self.send_data(ap),
                                   width=10, height=3, font=self.button_font,
                                   bg="light blue", fg="black")

            # 使用 grid 布局将按钮放置在三列
            nft_button.grid(row=i // 3, column=i % 3, padx=12, pady=12)

        # 更新滚动区域的可滚动范围
        nft_button_frame.update_idletasks()
        nft_canvas.config(scrollregion=nft_canvas.bbox("all"))

    def update_network_status(self):
        current_text = self.response_text.get(1.0, tk.END)
        if self.internet_connected:
            # if current_text.strip() == "In order to access the network, you do not have the required permissions. " \
            #                            "Please purchase NFT verification first.":
            #     self.response_text.delete(1.0, tk.END)
            #     self.response_text.config(font=self.text_font)
            self.network_status_indicator.config(text="Connected     ", fg="green")
            self.false_counter = 0
        else:
            self.network_status_indicator.config(text="Disconnected", fg="red")
            self.false_counter += 1

            if self.false_counter >= 3:
                self.response_text.delete(1.0, tk.END)
                self.response_text.insert(1.0,
                                          "In order to access the network, you do not have the required permissions. "
                                          "Please purchase NFT verification first.")
                self.response_text.config(font=self.text_font)

        self.window.after(1000, self.update_network_status)

    def check_internet_connection(self):
        while self.running:  # 使用标志变量停止循环
            try:
                result = subprocess.run("ping baidu.com -n 2", shell=True, stdout=subprocess.PIPE,
                                        stderr=subprocess.PIPE, text=True)
                output = result.stdout

                if "请求超时" in output or "无法连到端口" in output:
                    self.internet_connected = False
                else:
                    self.internet_connected = True
            except Exception as e:
                print(f"发生错误: {str(e)}")
                self.internet_connected = False

            time.sleep(1)

    def send_data(self, account_password):
        self.remaining_usage_time = 0
        self.countdown_event.clear()
        if messagebox.askyesno("Select NFT", "Do you want to choose this NFT to connect to WIFI?            "):
            threading.Thread(target=self.send_data_thread, args=(account_password,)).start()
        else:
            messagebox.showinfo("Cancellation", "You have cancelled using this NFT to connect to WIFI!            ")

    def send_data_thread(self, account_password):
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            client_socket.connect((self.server_ip, self.server_port))
            data = f"{account_password[0]} {account_password[1]}"
            client_socket.send(data.encode('utf-8'))
            response = client_socket.recv(1024).decode('utf-8')
            # self.response_text.insert(tk.END, f" {response}\n")

            response_lines = response.split('\n')
            authentication_result = response_lines[0]
            messagebox.showinfo("Connect WIFI results", f"Authentication Result: {authentication_result} ")
            remaining_time_line = response_lines[1]
            self.remaining_usage_time = int(remaining_time_line.split(': ')[-1])

            self.countdown_event.set()
            self.response_text.update_idletasks()

            print({authentication_result})

        except Exception as e:
            self.response_text.delete(1.0, tk.END)
            self.response_text.insert(tk.END, f"发生错误: {str(e)}\n")
        finally:
            client_socket.close()

    def countdown(self):
        while self.running:  # 使用标志变量停止循环
            self.countdown_event.wait()

            self.countdown_event.clear()

            # self.remaining_usage_time = self.remaining_usage_time - 4
            while self.remaining_usage_time > 0:
                if self.internet_connected:
                    self.remaining_usage_time -= 1
                    time.sleep(1)
                    print(self.remaining_usage_time)
                    self.response_text.delete(1.0, tk.END)
                    self.response_text.insert(1.0,
                                              "Verification successful. Enjoy using it!")
                    self.response_text.config(font=self.text_font)
                    self.update_countdown_label()

    def update_countdown_label(self):
        self.remaining_usage_time_var.set(f"Remaining Usage Time: {self.remaining_usage_time} seconds")

    def on_closing(self):
        self.running = False  # 设置标志为False停止循环
        self.countdown_event.set()
        self.countdown_thread.join()
        self.network_status_thread.join()
        self.client_socket.close()
        self.window.destroy()


if __name__ == "__main__":
    window = tk.Tk()
    client_gui = ClientGUI(window)
    window.mainloop()
