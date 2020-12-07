import socket
import os
import tkinter as tk

# tk
root = tk.Tk()
root.overrideredirect(True)
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
root.resizable(width=False, height=False)

# client
HOST_IP = "127.0.0.1"
DST_PORT = 2222
client_socket = socket.socket()
try:
    client_socket.connect((HOST_IP, DST_PORT))
except socket.error:
    print("no server is waiting...")
    client_socket.close()
    exit()
client_socket.send(str.encode("hello"))


def main():
    server_message = client_socket.recv(1024).decode()
    if server_message == "shutdown":
        os.system("shutdown /s /t 10")
    elif server_message == "lock":
        root.attributes("-alpha", 0.1)
        tk.mainloop()
    elif server_message == "unlock":
        root.quit()



if __name__ == main():
    main()