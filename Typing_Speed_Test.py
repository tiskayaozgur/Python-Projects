import tkinter.messagebox
import tkinter as tk
from tkinter import *
import tkinter.scrolledtext
class GUI_Server:
    def __init__(self, master):

        #Creating main frame
        master.geometry('500x500')
        master.title('Typing Speed Test')
        self.master = master


        # Creating text label for texting
        self.text = tk.Label(self.master, text='''
        Welcome to the speed test program! In which field would you like to race?
        If you want to select one of them, you should click twice on the one you want''', bg='red')
        self.text.grid(row=0, column=0, sticky='nsew')

        #Creating listbox for chosing write platform.
        self.listbox = tk.Listbox(self.master)
        self.listbox.grid(row=1, column=0, sticky='nsew')


        #Inserting datas for selecting subject from listbox
        self.listbox.insert(tk.END, 'Computer Science')
        self.listbox.insert(tk.END, 'Politics')
        self.listbox.insert(tk.END, 'History')
        self.listbox.insert(tk.END, 'Crypto Currency')
        self.listbox.insert(tk.END, 'Evolution')

        self.listbox.bind('<Double-Button-1>', self.double_click)

        #Setting master, when we try to expand
        self.master.rowconfigure(0, weight=1)
        self.master.rowconfigure(1, weight=1)
        self.master.columnconfigure(0, weight=1)


    def double_click(self, x):
        # print(self.listbox.get(tk.ACTIVE))
        if self.listbox.curselection()[0] == 0:
            print('0. indis seçildi')

        elif self.listbox.curselection()[0] == 1:
            pass

        elif self.listbox.curselection()[0] == 2:
            pass

        elif self.listbox.curselection()[0] == 3:
            pass

        elif self.listbox.curselection()[0] == 4:
            pass

root = tk.Tk()
gdb = GUI_Server(root)
root.mainloop()