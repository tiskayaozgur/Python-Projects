from tkinter import messagebox
import tkinter as tk
import tkinter.scrolledtext
import hashlib

class Hash_GUI:

    def __init__(self, master):

        master.geometry('300x300')
        master.title('Contact Books')
        self.master = master

        # Creating top frame
        self.top = tk.Frame(self.master, bg="blue")
        self.top.grid(row=0, column=0, sticky='nswe')

        # Creating bottom Frame
        self.bottom = tk.Frame(self.master, bg="grey")
        self.bottom.grid(row=1, column=0, sticky='nswe')

        #setting GUI for expantion
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)
        self.master.rowconfigure(1, weight=1)
        #self.master.rowconfigure(2, weight=1)


        #Creating description
        self.label = tk.Label(self.top, text='Input string for encryption', bg='grey')
        self.label.grid(row=0, column=0, sticky='nsew')

        self.top.columnconfigure(0, weight=1)
        self.top.rowconfigure(0, weight=1)
        self.top.rowconfigure(1, weight=1)
        self.top.rowconfigure(2, weight=1)


        # Creating entry area using scrolledtext for taking strings.
        self.entry_string = tk.scrolledtext.ScrolledText(self.top, font='Calibri 14', heigh=5)
        self.entry_string.grid(row=1, column=0, sticky='nswe')

        # Creating description
        self.label = tk.Label(self.top, text='Hash Code', bg='grey')
        self.label.grid(row=2, column=0, sticky='nsew')

        # Creating entry area using scrolledtext for taking strings.
        self.entry_hash = tk.scrolledtext.ScrolledText(self.top, font='Calibri 14', heigh=5)
        self.entry_hash.grid(row=3, column=0, sticky='nswe')

        #Creating str to hash button
        self.button = tk.Button(self.bottom, text="Str to hash", command=self.button_str_to_hash_handler)
        self.button.pack(side='left', expand=True)

        # # Creating hash to str button
        # self.button = tk.Button(self.bottom, text="Hash to str", command=self.button_hash_to_str_handler)
        # self.button.pack(side='left', expand=True)

    def button_str_to_hash_handler(self):

        text = self.entry_string.get('1.0', tk.END)
        # print(len(text))

        if len(text) == 1:
            messagebox.showwarning(title="Warning", message="You should write str for converting")

        else:
            sha1 = hashlib.sha1()
            sha1.update(text.encode('UTF-8'))
            ht = sha1.hexdigest()
            self.entry_hash.insert(tk.END, ht)
            self.entry_string.delete('1.0', tk.END)

root = tk.Tk()
gdb = Hash_GUI(root)
root.mainloop()
