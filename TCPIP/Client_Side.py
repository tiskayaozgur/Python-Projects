import tkinter as tk
import tkinter.messagebox
import sqlite3
from tkinter import ttk
from tkinter import *
import tkinter.font as tkFont
import tkinter.scrolledtext
import socket





class GUI_Client:
    def __init__(self, master):
        # self.client_sock = client_sock

        master.geometry('1000x800')
        master.title('Client Side')
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

        # # Creating connect button in right frame
        # self.button_connect = tk.Button(self.right_frame, text="CONNECT", command=self.button_connect_handler)
        # self.button_connect.pack(side='left', expand=True)

        # connection requeriments
        SERVER_PORT_NO = 50100
        SERVER_HOSTNAME = "127.0.0.1"
        self.client_sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM, proto=socket.IPPROTO_TCP)
        self.client_sock.connect((SERVER_HOSTNAME, SERVER_PORT_NO))




    def button_send_handler(self):
        text_client = self.entry.get()
        self.entry.delete(0, tk.END)

        # showing all datas that server sent
        self.text_chat.insert(tk.END, "<Client>" + text_client + '\n')

        b = text_client.encode("UTF-8")  # Gırılen str'yı byte nesnesıne cevırdım kı bunu send ıle server tarafına gonderebıleyım.
        self.client_sock.send(b)


        b = self.client_sock.recv(1024)
        text_server = b.decode("UTF-8")  # serverdan gelen cevap byte oldugu ıcın bunu strye cevırıp prınt ıle bastım, yanı yazının tersını
        # print(text_server)
        self.text_chat.insert(tk.END, "<Server>" + text_server + '\n')
        # self.entry.delete(0, tk.END)



    #Deleting all datas in text_chat
    def button_delete_handler(self):
        self.text_chat.delete('1.0', 'end')



root = tk.Tk()
gdb = GUI_Client(root)
root.mainloop()