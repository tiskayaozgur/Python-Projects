#server Program
import tkinter as tk
import tkinter.messagebox
import sqlite3
from tkinter import ttk
from tkinter import *
import tkinter.font as tkFont
import tkinter.scrolledtext
import socket
import time

class GUI_Server:
    def __init__(self, master):

        master.geometry('800x250')
        master.title('Server Side')
        self.master = master

        # Creating left frame
        self.left_frame = tk.Frame(self.master, bg="yellow", width=10)
        self.left_frame.grid(row=0, column=0, sticky='nswe')

        # Creating Right Frame
        self.right_frame = tk.Frame(self.master, bg="blue", width=10)
        self.right_frame.grid(row=0, column=1, sticky='nswe')

        # when we try to expand horizontal, frame automaticly will expand
        master.columnconfigure(0, weight=2)
        master.columnconfigure(1, weight=1)

        # when we try to expand vertical, frame automaticly will expand
        master.rowconfigure(0, weight=1)


        #Creating chat area using scrolled text
        self.text_chat = tk.scrolledtext.ScrolledText(self.left_frame, font='Calibri 14', width=60)
        self.text_chat.grid(row=0, column=0, sticky='nswe')


        #creating chat entry
        self.entry = tk.Entry(self.left_frame)
        self.entry.grid(row=1, column=0, sticky='nsew')

        # setting chat area for if we expend the GUI
        self.left_frame.columnconfigure(0, weight=1)
        self.left_frame.rowconfigure(0, weight=1)

        #creating send button in right frame
        self.button_send = tk.Button(self.right_frame, text="SEND", command=self.button_send_handler)
        self.button_send.pack(side='left', expand=True)

        # creating delete button in right frame
        self.button_send = tk.Button(self.right_frame, text="DELETE", command=self.button_delete_handler)
        self.button_send.pack(side='left', expand=True)

        #Creating connect button in right frame
        self.button_connect = tk.Button(self.right_frame, text="CONNECT", command=self.button_connect_handler)
        self.button_connect.pack(side='left', expand=True)

    #for connecting, you should use conect button
    def button_connect_handler(self):
        try:
            # connecting requeriments
            SERVER_PORT_NO = 50050
            self.server_sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM, proto=socket.IPPROTO_TCP)
            self.server_sock.bind(("", SERVER_PORT_NO))
            self.server_sock.listen(32)

            print("Waiting for connection...")
            self.client_sock, self.client_addr = self.server_sock.accept()
            print(f"Server'a baglanan client'in ip-port bilgisi={self.client_addr}")

            while True:
                # showing all datas that client sent
                binary_client = self.client_sock.recv(1024)  # Clienttan gelen byte nesneyı recv ıle aldım.
                text_client = binary_client.decode("UTF-8")  # byte nesnesını strye cevırdım, cunku bu yazıyı ters cevırıp karsı tarafa gonderecegım
                if text_client != "":
                    print(text_client)
                    self.text_chat.insert(tk.END, "<Client>" + text_client + '\n')  # clienttan gelen mesajı guımıze yerlestırdık
                break



        except Exception as e:
            print(e)


    def button_send_handler(self):
        # taking datas from server entries
        text_server = self.entry.get()

        # showing all datas that server sent
        self.text_chat.insert(tk.END, "<Server>" + text_server + '\n')

        b = text_server.encode("UTF-8")  # Gırılen str'yı byte nesnesıne cevırdım kı bunu send ıle server tarafına gonderebıleyım.
        self.client_sock.send(b)
        self.entry.delete(0, tk.END)





    # Deleting all datas in text_chat
    def button_delete_handler(self):
        self.text_chat.delete('1.0', 'end')


root = tk.Tk()
gdb = GUI_Server(root)
root.mainloop()


