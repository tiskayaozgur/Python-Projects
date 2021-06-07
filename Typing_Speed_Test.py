import tkinter.messagebox
import tkinter as tk
from tkinter import *
import tkinter.scrolledtext
import datetime as dt

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
        self.listbox.insert(tk.END, 'Programming Languages')
        self.listbox.insert(tk.END, 'Horoscopes')
        self.listbox.insert(tk.END, 'Football')


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
        self.button_start = tk.Button(self.right_frame, text="START", command=self.button_start_handler)
        self.button_start.pack(side='left', expand=True)

        #Creating show result button for showing candidate results
        self.button_show_result = tk.Button(self.right_frame, text="SHOW RESULT", command=self.button_show_result_handler, state=tk.DISABLED)
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
                #Creating object for using subject_windows method's variable and
                object_computer_science = Typing_Speed_Test(root)
                object_computer_science.subject_windows()
                result = file.read()
                object_computer_science.text_board_read.insert(tk.END, result)


        # if you want to click second index in listbox
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

        # if you want to click third index in listbox
        elif self.listbox.curselection()[0] == 3:
            with open(r'C:\\Users\Monster\Desktop\subjects\crypto_currency.txt', 'r', encoding='UTF-8') as file:
                # Creating object for using subject_windows method's variable
                object_computer_science = Typing_Speed_Test(root)
                object_computer_science.subject_windows()
                result = file.read()
                object_computer_science.text_board_read.insert(tk.END, result)

        # if you want to click fourth index in listbox
        elif self.listbox.curselection()[0] == 4:
            with open(r'C:\\Users\Monster\Desktop\subjects\evolution.txt', 'r', encoding='UTF-8') as file:
                # Creating object for using subject_windows method's variable
                object_computer_science = Typing_Speed_Test(root)
                object_computer_science.subject_windows()
                result = file.read()
                #Using variable from another method in same class
                object_computer_science.text_board_read.insert(tk.END, result)


        elif self.listbox.curselection()[0] == 5:
            with open(r'C:\\Users\Monster\Desktop\subjects\programming_languages.txt', 'r', encoding='UTF-8') as file:
                # Creating object for using subject_windows method's variable
                object_computer_science = Typing_Speed_Test(root)
                object_computer_science.subject_windows()
                result = file.read()
                # Using variable from another method in same class
                object_computer_science.text_board_read.insert(tk.END, result)

        elif self.listbox.curselection()[0] == 6:
            with open(r'C:\\Users\Monster\Desktop\subjects\horoscope.txt', 'r', encoding='UTF-8') as file:
                # Creating object for using subject_windows method's variable
                object_computer_science = Typing_Speed_Test(root)
                object_computer_science.subject_windows()
                result = file.read()
                # Using variable from another method in same class
                object_computer_science.text_board_read.insert(tk.END, result)

        elif self.listbox.curselection()[0] == 7:
            with open(r'C:\\Users\Monster\Desktop\subjects\football.txt', 'r', encoding='UTF-8') as file:
                # Creating object for using subject_windows method's variable
                object_computer_science = Typing_Speed_Test(root)
                object_computer_science.subject_windows()
                result = file.read()
                # Using variable from another method in same class
                object_computer_science.text_board_read.insert(tk.END, result)

    #Creating button_start_handler method
    def button_start_handler(self):
        #If you want to start the contest you should press the start button first.
        if len(self.text_board_write.get('1.0', END+'-1c')) == 0:

            #After clicking start button, start button will be disabled, show result button will be Enabled
            self.button_start.config(state=tk.DISABLED)
            self.button_show_result.config(state=tk.NORMAL)

            #Taking start time when click start button
            self.start_time = dt.datetime.now()
            print(f'Start Time= {self.start_time}')

        else:
            messagebox.showwarning(title="Warning", message="You should write after click start button")

    #Creating button_show_result_handler method
    def button_show_result_handler(self):
        #After clicking show result button, start button will disabled,
        self.button_show_result.config(state=tk.NORMAL)

        end_time = dt.datetime.now()
        print(f'End time={end_time}')
        result = end_time - self.start_time
        print(f'Difference ={result}')

        # Taking datas from reading area
        list_read = self.text_board_read.get('1.0', END + '-1c').split()
        print(list_read)

        # Taking datas from writing area
        list_write = self.text_board_write.get('1.0', END + '-1c').split()
        print(list_write)

        correct_words = []
        incorrect_words = []
        # Comparing and taking datas for showing
        for i in range(len(list_write)):
            if list_read[i] == list_write[i]:
                correct_words.append(list_write[i])
            else:
                incorrect_words.append(list_write[i])

        # Creating new window for showing results
        self.result_window = Tk()
        self.result_window.geometry("745x745")
        self.result_window.title("Result Window")
        self.result_window.resizable(width=False, height=False)

        # Creating correct_words_label
        self.correct_words_label = tk.Label(self.result_window, text="Correct Words", bg='green', width=20)
        self.correct_words_label.grid(row=0, column=0, sticky='nsew')

        # Creating incorrect_words_label
        self.incorrect_words_label = tk.Label(self.result_window, text="Incorrect Words", bg='green', width=20)
        self.incorrect_words_label.grid(row=0, column=1, sticky='nsew')

        # Creating time_label
        self.time_label = tk.Label(self.result_window, text="Time", bg='green', width=20)
        self.time_label.grid(row=0, column=2, sticky='nsew')

        # Creating correct_words_count_label
        self.correct_words_count_label = tk.Label(self.result_window, text="Count of Correct Words", bg='green',width=21)
        self.correct_words_count_label.grid(row=0, column=3, sticky='nsew')

        # Creating incorrect_words_count_label
        self.incorrect_words_count_label = tk.Label(self.result_window, text="Count of Incorrect Words", bg='green',width=21)
        self.incorrect_words_count_label.grid(row=0, column=4, sticky='nsew')

        # showing correct_words datas on new gui
        for i in range(len(correct_words)):
            self.listbox_name = tk.Listbox(self.result_window, heigh=1, width=20, bg="white")
            self.listbox_name.grid(row=i + 1, column=0, sticky='nswe')
            self.listbox_name.insert(tk.END, correct_words[i])

        # showing incorrect_words datas on new gui
        for i in range(len(incorrect_words)):
            self.listbox_name = tk.Listbox(self.result_window, heigh=1, width=20, bg="white")
            self.listbox_name.grid(row=i + 1, column=1, sticky='nswe')
            self.listbox_name.insert(tk.END, incorrect_words[i])

        # showing time datas on new gui
        self.listbox_name = tk.Listbox(self.result_window, heigh=1, width=20, bg="white")
        self.listbox_name.grid(row=1, column=2, sticky='nswe')
        self.listbox_name.insert(tk.END, result)

        # Showing correct_words_count on gui
        self.listbox_name = tk.Listbox(self.result_window, heigh=1, width=20, bg="white")
        self.listbox_name.grid(row=1, column=3, sticky='nswe')
        self.listbox_name.insert(tk.END, len(correct_words))

        # Showing incorrect_words_count on gui
        self.listbox_name = tk.Listbox(self.result_window, heigh=1, width=20, bg="white")
        self.listbox_name.grid(row=1, column=4, sticky='nswe')
        self.listbox_name.insert(tk.END, len(incorrect_words))

        #Disabled show result button after showing results.
        self.button_show_result.config(state=tk.DISABLED)

root = tk.Tk()
gdb = Typing_Speed_Test(root)
root.mainloop()
