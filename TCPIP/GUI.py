import tkinter as tk
import tkinter.messagebox
import sqlite3
from tkinter import ttk
from tkinter import *
import tkinter.font as tkFont
import tkinter.scrolledtext



class GUI:
    def __init__(self, master):

        master.geometry('1000x800')
        master.title('Chat Program')
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





    def button_send_handler(self):

        #Taking datas from entries
        msg = self.entry.get()

        #inerting every sentence or words to the text_chat, after that deleting
        self.text_chat.insert(tk.END, msg)
        self.entry.delete(0, tk.END)




    def button_delete_handler(self):
        pass



root = tk.Tk()
gdb = GUI(root)
root.mainloop()