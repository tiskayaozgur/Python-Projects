import tkinter as tk
import tkinter.scrolledtext
class GUI:

    def __init__(self, master):

        master.geometry('300x300')
        master.title('Contact Books')
        self.master = master

        # Creating top frame
        self.top = tk.Frame(self.master, bg="blue")
        self.top.grid(row=0, column=0, sticky='nswe')

        # Creating bottom Frame
        self.bottom = tk.Frame(self.master, bg="blue")
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


        # Creating entry area using scrolledtext for taking strings.
        self.entry = tk.scrolledtext.ScrolledText(self.top, font='Calibri 14', heigh=5)
        self.entry.grid(row=1, column=0, sticky='nswe')

        self.button = tk.Button(self.bottom, text="SHOW", command=self.button_show_handler)
        self.button.pack(side='left', expand=True)



    def button_show_handler(self):
        pass

root = tk.Tk()
gdb = GUI(root)
root.mainloop()
