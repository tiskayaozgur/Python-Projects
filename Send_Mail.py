import tkinter as tk
import tkinter.messagebox
from tkinter import *
import smtplib
from email.mime.text import MIMEText


class GUI:
    def __init__(self, master):
        master.geometry('500x500')
        master.title('Send Email')
        self.master = master

        # creating username label-entries
        self.username_label = tk.Label(self.master, text='Username', bg='grey')
        self.username_label.grid(row=0, column=0, sticky='nsew')
        self.username_entry = tk.Entry(self.master)
        self.username_entry.grid(row=0, column=1, sticky='nsew')

        #creating password label-entries
        self.password_label = tk.Label(self.master, text='Password', bg='grey')
        self.password_label.grid(row=1, column=0, sticky='nsew')
        self.password_entry = tk.Entry(self.master, show='*') #for cursor invisible, i used show parameter.
        self.password_entry.grid(row=1, column=1, sticky='nsew')

        # creating to label-entries
        self.to_label = tk.Label(self.master, text='To', bg='grey')
        self.to_label.grid(row=2, column=0, sticky='nsew')
        self.to_entry = tk.Entry(self.master)
        self.to_entry.grid(row=2, column=1, sticky='nsew')

        # creating subject label-entries
        self.subject_label = tk.Label(self.master, text='Subject', bg='grey')
        self.subject_label.grid(row=3, column=0, sticky='nsew')
        self.subject_entry = tk.Entry(self.master)
        self.subject_entry.grid(row=3, column=1, sticky='nsew')

        # creating content label-entries
        self.content_label = tk.Label(self.master, text='Content', bg='grey')
        self.content_label.grid(row=4, column=0, sticky='nsew')
        self.content_entry = tk.Entry(self.master)
        self.content_entry.grid(row=4, column=1, sticky='nsew')

        # Creating add button in bottom_right_frame
        self.button_send = tk.Button(self.master, text="SEND", command=self.button_send_handler)
        self.button_send.grid(row=5, column=0, columnspan=2)

        #creating clear all button for deleting all datas in entries
        self.button_clear_all = tk.Button(self.master, text="CLEAR ALL", command=self.button_clear_all_handler)
        self.button_clear_all.grid(row=5, column=1, columnspan=2)



        #setting every entries column heavy
        self.master.columnconfigure(0, weight=1)
        self.master.columnconfigure(1, weight=3)

        # setting every entries row's heavy
        self.master.rowconfigure(0, weight=1)
        self.master.rowconfigure(1, weight=1)
        self.master.rowconfigure(2, weight=1)
        self.master.rowconfigure(3, weight=1)
        self.master.rowconfigure(4, weight=1)
        self.master.rowconfigure(5, weight=1)


    def button_send_handler(self):

        #Taking datas from entries
        user_name = self.username_entry.get().strip()
        password = self.password_entry.get().strip()
        receipants = self.to_entry.get().strip()
        # sender = self.from_entry.get()
        subject = self.subject_entry.get().strip()
        msg = self.content_entry.get().strip()

        if user_name != "" and password != "" and receipants != "" and subject != "" and msg != "":
            #creating MIME areas
            mt = MIMEText(msg)
            mt['From'] = user_name
            mt['To'] = receipants
            mt['Subject'] = subject

            msg = mt.as_string()

            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.ehlo()
            server.login(user_name, password)
            server.sendmail(user_name, receipants, msg)
            server.quit()

            #After sending, delete all data's from GUI
            self.username_entry.delete(0, tk.END)
            self.password_entry.delete(0, tk.END)
            self.to_entry.delete(0, tk.END)
            self.subject_entry.delete(0, tk.END)
            self.content_entry.delete(0, tk.END)

        else:
            messagebox.showwarning(title="Warning", message="Please enter all entries to send email!")

    def button_clear_all_handler(self):
        # Delete all datas from every entries using clear all button
        self.username_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)
        self.to_entry.delete(0, tk.END)
        self.subject_entry.delete(0, tk.END)
        self.content_entry.delete(0, tk.END)


root = tk.Tk()
gdb = GUI(root)
root.mainloop()
