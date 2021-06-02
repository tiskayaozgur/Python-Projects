import tkinter.messagebox
import tkinter as tk
from tkinter import *
import tkinter.scrolledtext

class Typing_Speed_Test:
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

        #Binding listbox
        self.listbox.bind('<Double-Button-1>', self.double_click)

        #Setting master, when we try to expand
        self.master.rowconfigure(0, weight=1)
        self.master.rowconfigure(1, weight=1)
        self.master.columnconfigure(0, weight=1)

    #Creating general window for selecting after subjects
    def subject_windows(self):
        # Creating new window while clicking add button
        self.typing_window = Tk()
        self.typing_window.geometry("800x800")
        self.typing_window.title("Computer Sicience")

        # Creating left frame
        self.left_frame = tk.Frame(self.typing_window, bg="blue")
        self.left_frame.grid(row=0, column=0, sticky='nswe')

        # Creating Right Frame
        self.right_frame = tk.Frame(self.typing_window, bg="gray")
        self.right_frame.grid(row=0, column=1, sticky='nswe')

        # when we try to expand horizontal, frame automaticly will expand
        self.typing_window.columnconfigure(0, weight=1)
        self.typing_window.columnconfigure(1, weight=1)
        self.typing_window.rowconfigure(0, weight=1)
        self.typing_window.rowconfigure(1, weight=1)


        # setting chat area for if we expend the GUI
        self.left_frame.columnconfigure(0, weight=1)
        self.left_frame.rowconfigure(0, weight=1)
        self.left_frame.rowconfigure(1, weight=1)
        self.right_frame.columnconfigure(0, weight=1)

        #Creating start button for race
        self.button_start = tk.Button(self.right_frame, text="START")
        self.button_start.pack(side='left', expand=True)

        #Creating show result button for showing candidate results
        self.button_show_result = tk.Button(self.right_frame, text="SHOW RESULT")
        self.button_show_result.pack(side='left', expand=True)



        # Creating board area using scrolledtext for reading.
        self.text_board_read = tk.scrolledtext.ScrolledText(self.left_frame, font='Calibri 14')
        self.text_board_read.grid(row=0, column=0, sticky='nswe')

        # Creating text area using scrolledtext for writing.
        self.text_board_write = tk.scrolledtext.ScrolledText(self.left_frame, font='Calibri 14')
        self.text_board_write.grid(row=1, column=0, sticky='nswe')

    def double_click(self, x):
        #if you want to click first index in listbox
        if self.listbox.curselection()[0] == 0:

            with open(r'C:\\Users\Monster\Desktop\subjects\computer_science.txt', 'r', encoding='UTF-8') as file:
                #Creating object for using subject_windows method's variable
                object_computer_science = Typing_Speed_Test(root)
                object_computer_science.subject_windows()
                result = file.read()
                object_computer_science.text_board_read.insert(tk.END, result)


        elif self.listbox.curselection()[0] == 1:
            with open(r'C:\\Users\Monster\Desktop\subjects\politics.txt', 'r', encoding='UTF-8') as file:
                # Creating object for using subject_windows method's variable
                object_computer_science = Typing_Speed_Test(root)
                object_computer_science.subject_windows()
                result = file.read()
                object_computer_science.text_board_read.insert(tk.END, result)

        elif self.listbox.curselection()[0] == 2:
            with open(r'C:\\Users\Monster\Desktop\subjects\history.txt', 'r', encoding='UTF-8') as file:
                # Creating object for using subject_windows method's variable
                object_computer_science = Typing_Speed_Test(root)
                object_computer_science.subject_windows()
                result = file.read()
                object_computer_science.text_board_read.insert(tk.END, result)

        elif self.listbox.curselection()[0] == 3:
            with open(r'C:\\Users\Monster\Desktop\subjects\crypto_currency.txt', 'r', encoding='UTF-8') as file:
                # Creating object for using subject_windows method's variable
                object_computer_science = Typing_Speed_Test(root)
                object_computer_science.subject_windows()
                result = file.read()
                object_computer_science.text_board_read.insert(tk.END, result)

        elif self.listbox.curselection()[0] == 4:
            with open(r'C:\\Users\Monster\Desktop\subjects\evolution.txt', 'r', encoding='UTF-8') as file:
                # Creating object for using subject_windows method's variable
                object_computer_science = Typing_Speed_Test(root)
                object_computer_science.subject_windows()
                result = file.read()

                #Using variable from another method in same class
                object_computer_science.text_board_read.insert(tk.END, result)

root = tk.Tk()
gdb = Typing_Speed_Test(root)
root.mainloop()