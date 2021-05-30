#Client Program
import tkinter.messagebox
import tkinter as tk
import tkinter.scrolledtext
import socket
import threading
from tkinter import *


# import tkinter.messagebox
# from tkinter import ttk
# import tkinter.font as tkFont


class GUI_Client:
    def __init__(self, master):
        # self.client_sock = client_sock

        master.geometry('800x250')
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
        self.text_chat_client = tk.scrolledtext.ScrolledText(self.left_frame, font='Calibri 14', width=60)
        self.text_chat_client.grid(row=0, column=0, sticky='nswe')


        #creating chat entry, and binding this entry to send data when we clicked enter
        self.entry = tk.Entry(self.left_frame)
        self.entry.grid(row=1, column=0, sticky='nsew')
        self.entry.bind("<Return>", self.enter_handler)

        # setting chat area for if we expend the GUI
        self.left_frame.columnconfigure(0, weight=1)
        self.left_frame.rowconfigure(0, weight=1)

        #creating send button in right frame
        self.button_send = tk.Button(self.right_frame, text="SEND", command=self.button_send_handler)
        self.button_send.pack(side='left', expand=True)

        # creating delete button in right frame
        self.button_delete= tk.Button(self.right_frame, text="DELETE", command=self.button_delete_handler)
        self.button_delete.pack(side='left', expand=True)

        # creating save chat button in right frame
        self.button_save_chat = tk.Button(self.right_frame, text="SAVE CHAT", command=self.button_save_chat_handler)
        self.button_save_chat.pack(side='left', expand=True)

    #Creating run method() for creating thread to take datas from server side
    def run(self):

        self.clients = {}
        self.lock = threading.Lock()

        # connection requeriments
        SERVER_PORT_NO = 50050
        SERVER_HOSTNAME = "127.0.0.1"
        self.client_sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM, proto=socket.IPPROTO_TCP)
        self.client_sock.connect((SERVER_HOSTNAME, SERVER_PORT_NO))

        # Creating thread for taking datas from server side.
        self.thread = threading.Thread(target=self.thread_proc)
        self.thread.start()

    # This will be run like  another process
    def thread_proc(self):
        while True:
            # takiing all datas that server sent, and inserting that datas to the text area
            binary_client = self.client_sock.recv(1024)
            text_client = binary_client.decode("UTF-8")
            if text_client:
                # print(text_client)
                self.text_chat_client.insert(tk.END,"<Server>" + text_client + '\n')
            else:
                break


    def button_send_handler(self):
        # taking datas from client entries
        text_client = self.entry.get()

        # showing all datas that server sent
        self.text_chat_client.insert(tk.END, "<Client>" + text_client + '\n')

        # coverting bytes, for send to the server side
        b = text_client.encode("UTF-8")
        self.client_sock.send(b)

        # Deleting all in entry
        self.entry.delete(0, tk.END)


    #Deleting all datas in text_chat
    def button_delete_handler(self):
        self.text_chat_client.delete('1.0', 'end')


    def enter_handler(self, x):
        # taking datas from client entries
        text_client = self.entry.get()

        # showing all datas that server sent
        self.text_chat_client.insert(tk.END, "<Client>" + text_client + '\n')

        # coverting bytes, for send to the server side
        b = text_client.encode("UTF-8")
        self.client_sock.send(b)

        # Deleting all in entry
        self.entry.delete(0, tk.END)

    #saving all datas to the Desktop
    def button_save_chat_handler(self):
        if self.text_chat_client.get('1.0', END + '-1c') != "":
            with open("C:\\Users\Monster\Desktop\client_side_chat.txt", "a+", encoding="UTF-8") as file:
                file.write(self.text_chat_client.get('1.0', END+'-1c'))
            #print(self.text_chat_client.get('1.0', END+'-1c'))

        else:
            messagebox.showwarning(title="Warning",message="If you want to save conversation, you should write something!")

root = tk.Tk()
gdb = GUI_Client(root)
gdb.run() #Calling run method to create thread
root.mainloop()