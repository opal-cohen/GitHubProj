import socket
import tkinter as tk
from wakeonlan import send_magic_packet

# server
server_socket = socket.socket()
server_socket.bind(("0.0.0.0", 2222))
server_socket.listen(1)
(client_socket, address) = server_socket.accept()
data = client_socket.recv(1024).decode()
print(data)


def lock_screen():
    client_socket.send(str.encode("lock"))


def unlock_screen():
    client_socket.send(str.encode("unlock"))


def awake():
    send_magic_packet('1C-6F-65-F8-78-67', ip_address='192.168.2.107', port=2222)


def shutdown():
    client_socket.send(str.encode("shutdown"))


# tk
root = tk.Tk()
x = root.winfo_screenwidth()
y = root.winfo_screenheight()
root.geometry("%dx%d" % (x, y))
root.title("SMART CLASS")
root["background"] = "#%02x%02x%02x" % (188, 191, 194)
Button1 = tk.Button(root, text="Turn off computer", font=('calibri', 20, 'bold'), width=15, height=2, command=shutdown)\
    .place(x=100, y=20)
Button2 = tk.Button(root, text="Turn on computer", font=('calibri', 20, 'bold'),  width=15, height=2, command=awake)\
    .place(x=100, y=120)
Button3 = tk.Button(root, text="lock", font=('calibri', 20, 'bold'),  width=15, height=2, command=lock_screen)\
    .place(x=100, y=220)
Button4 = tk.Button(root, text="unlock", font=('calibri', 20, 'bold'),  width=15, height=2, command=unlock_screen)\
    .place(x=100, y=320)
root.mainloop()


def main():
    input1 = input("Enter a code...")
    client_socket.send(str.encode(input1))


if __name__ == main():
    main()
