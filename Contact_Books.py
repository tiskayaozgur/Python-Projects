import tkinter as tk
import tkinter.messagebox
import sqlite3
from tkinter import ttk
from tkinter import *


import tkinter.font as tkFont

class GUI:

    def __init__(self, master):

        master.geometry('1000x800')
        master.title('Contact Books')
        self.master = master

        # Db connection and table creation
        self.conn = sqlite3.connect(r'C:\Users\Monster\Desktop\Ozgur_Python_Projeler\contact_books.sqlite')
        cur = self.conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS contact_books(name TEXT, job TEXT, email TEXT)")

        # Creating left frame
        self.left_frame = tk.Frame(self.master, bg="gray", width=10)
        self.left_frame.grid(row=0, column=0, sticky='nswe')

        # Creating Right Frame
        self.right_frame = tk.Frame(self.master, bg="blue", width=10)
        self.right_frame.grid(row=0, column=1, sticky='nswe')

        # when we try to expand horizontal, frame automaticly will expand
        master.columnconfigure(0, weight=2)
        master.columnconfigure(1, weight=1)

        # when we try to expand vertical, frame automaticly will expand
        master.rowconfigure(0, weight=1)


        # Creating top_right Frame
        self.top_right_frame = tk.Frame(self.right_frame, bg="yellow")
        self.top_right_frame.grid(row=0, column=1, sticky='nswe')

        #creating bottom-right frame
        self.bottom_right_frame = tk.Frame(self.right_frame, bg="blue")
        self.bottom_right_frame.grid(row=1, column=1, sticky='nswe')

        #setting right frame's heavy when we extend the guı
        self.right_frame.rowconfigure(0, weight=1)
        self.right_frame.rowconfigure(1, weight=1)
        self.right_frame.columnconfigure(1, weight=1)


        # Creating add button in top_right frame
        self.button_add = tk.Button(self.bottom_right_frame, text="  ADD  ", command=self.button_add_handler)
        self.button_add.pack(side='left', expand=True)

        # Creating delete button in right frame
        self.button_delete = tk.Button(self.bottom_right_frame, text="DELETE", command=self.button_delete_handler)
        self.button_delete.pack(side='left', expand=True)
        # self.button_delete.bind('<Button-1>', self.button_delete_handler)




        #creating label-entry name in top-right-frame
        self.label_name_in_top_right_frame = tk.Label(self.top_right_frame, text='Name', bg='grey')
        self.label_name_in_top_right_frame.grid(row=0, column=0, sticky='nsew')
        self.entry_name_in_top_right_frame = tk.Entry(self.top_right_frame)
        self.entry_name_in_top_right_frame.grid(row=0, column=1, sticky='nsew')

        #creating label-entry job in top-right-frame
        self.label_job_in_top_right_frame = tk.Label(self.top_right_frame, text='Job', bg='grey')
        self.label_job_in_top_right_frame.grid(row=1, column=0, sticky='nsew')
        self.entry_job_in_top_right_frame = tk.Entry(self.top_right_frame)
        self.entry_job_in_top_right_frame.grid(row=1, column=1, sticky='nsew')

        # creating label-entry email in top-right-frame
        self.label_email_in_top_right_frame = tk.Label(self.top_right_frame, text='Email', bg='grey')
        self.label_email_in_top_right_frame.grid(row=2, column=0, sticky='nsew')
        self.entry_email_in_top_right_frame = tk.Entry(self.top_right_frame)
        self.entry_email_in_top_right_frame.grid(row=2, column=1, sticky='nsew')

        #creating button search in top_right_frame
        self.button_search = tk.Button(self.top_right_frame, text="SEARCH", command=self.button_search_handler)
        self.button_search.grid(row=3, column=0, columnspan=2)


        # setting labels and entries column heavy when we try to expand
        self.top_right_frame.columnconfigure(0, weight=2)
        self.top_right_frame.columnconfigure(1, weight=7)

        # setting labels and entries row heavy when we try to expand
        self.top_right_frame.rowconfigure(0, weight=1)
        self.top_right_frame.rowconfigure(1, weight=1)
        self.top_right_frame.rowconfigure(2, weight=1)
        self.top_right_frame.rowconfigure(3, weight=15)



        #creating tree's and scroll bars
        self.tree = ttk.Treeview(columns=employees_header, show="headings")
        vsb = ttk.Scrollbar(orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=vsb.set)
        self.tree.grid(column=0, row=0, sticky='nsew', in_=self.left_frame)
        vsb.grid(column=1, row=0, sticky='ns', in_=self.left_frame)
        self.left_frame.columnconfigure(0, weight=1)
        self.left_frame.rowconfigure(0, weight=1)




        #showing all datas at guı from database
        for col in employees_header:
            self.tree.heading(col, text=col.title())
            self.tree.column(col,width=tkFont.Font().measure(col.title()))

        #inserting all datas from databases for gui to show.
        for item in datas:
            self.tree.insert('', 'end', values=item)
            # adjust column's width if necessary to fit each value
            for ix, val in enumerate(item):
                col_w = tkFont.Font().measure(val)
                if self.tree.column(employees_header[ix],width=None)<col_w:
                    self.tree.column(employees_header[ix], width=col_w)


    #add button in bottom-right frame
    def button_add_handler(self):
        #Creating new window while clicking add button
        new_window_in_add_button = Tk()
        new_window_in_add_button.geometry("300x300")
        new_window_in_add_button.title("Add Some Contact")

        #Creating name listbox&entries
        self.label_name_in_add_button = tk.Label(new_window_in_add_button, text='Name:', font='Calibri 12')
        self.label_name_in_add_button.place(x=10, y=10)
        self.entry_name_in_add_button = tk.Entry(new_window_in_add_button, width=15, font='Calibri 12')
        self.entry_name_in_add_button.place(x=70, y=10)

        #Creating job listbox&entries
        self.label_job_in_add_button = tk.Label(new_window_in_add_button, text='Job:', font='Calibri 12')
        self.label_job_in_add_button.place(x=10, y=40)
        self.entry_job_in_add_button = tk.Entry(new_window_in_add_button, width=15, font='Calibri 12')
        self.entry_job_in_add_button.place(x=70, y=40)

        #Creating email listbox&entries
        self.label_email_in_add_button = tk.Label(new_window_in_add_button, text='Email:', font='Calibri 12')
        self.label_email_in_add_button.place(x=10, y=70)
        self.entry_email_in_add_button = tk.Entry(new_window_in_add_button, width=15, font='Calibri 12')
        self.entry_email_in_add_button.place(x=70, y=70)


        #Creating button ok and cancel
        self.button_ok = tk.Button(new_window_in_add_button, text="OK", command=self.button_ok_handler)
        self.button_ok.place(x=25, y=125, heigh=25, width=50)

        self.button_cancel = tk.Button(new_window_in_add_button, text="Cancel", command=self.button_cancel_handler)
        self.button_cancel.place(x=100, y=125, heigh=25, width=50)


    # delete button in bottom-right frame
    def button_delete_handler(self):


        if self.tree.selection() != (): #if we want to delete some datas, we should select one of them
            # deleting datas from GUI(trees)that ve selected
            selected_item = self.tree.selection()[0]

            # creating list because , it will include row elements that we select
            l = []
            # tum trees ıcerısındekı datalarda gezınıyorum
            for line in self.tree.get_children():
                for value in self.tree.item(line)['values']:

                    # trees ıcerısınde tıklanmıs yanı secılmıs olan datayı lısteye attım kı oradan da okuyarak database'den de sılecegım kı goruntude de gıtsın.
                    if line == selected_item:
                        l.append(value)

            # deleting datas that we choose from database
            sql = "DELETE FROM contact_books WHERE name=? AND job=? AND email=?"
            cur = self.conn.cursor()
            cur.execute(sql, (l[0], l[1], l[2]))
            self.conn.commit()

            # deleting datas from GUI(trees)that ve selected
            self.tree.delete(selected_item)

        else:#otherwise we cant delete any datas
            messagebox.showwarning(title="Warning", message="You should select at least one row to delete!")



    #search button in top-right-frame
    def button_search_handler(self):
        # taking data's from entries
        name = self.entry_name_in_top_right_frame.get().strip()
        job = self.entry_job_in_top_right_frame.get().strip()
        email = self.entry_email_in_top_right_frame.get().strip()

        names = []
        jobs = []
        emails = []

        # taking datas from db to show guı
        sql = "SELECT * FROM contact_books WHERE name=? or job=? or email=?"
        result = cur.execute(sql, (name, job, email))
        for i in result:
            names.append(i[0])
            jobs.append(i[1])
            emails.append(i[2])


        while True:
            if name != "" or job != "" or email != "":
                if names !=[] or jobs != [] or emails !=[]:


                    # Creating new window while clicking search button
                    new_window_in_search_button = Tk()
                    new_window_in_search_button.geometry("500x400")
                    # new_window_in_search_button.resizable(width=False, height=False)
                    new_window_in_search_button.title("Search Results")

                    # Name Label in search button
                    self.label_name_in_search_button = tk.Label(new_window_in_search_button, text="Name", width=13,bg='red')
                    self.label_name_in_search_button.grid(row=0, column=0, sticky='nsew')

                    # Job Label in search button
                    self.label_job_in_search_button = tk.Label(new_window_in_search_button, text="Job", width=13,bg='green')
                    self.label_job_in_search_button.grid(row=0, column=1, sticky='nsew')

                    # email label in search button
                    self.label_email_in_search_button = tk.Label(new_window_in_search_button, text="email", width=13,bg='purple')
                    self.label_email_in_search_button.grid(row=0, column=2, sticky='nsew')

                    # setting every colums size when we try to expand new window in search button
                    new_window_in_search_button.columnconfigure(0, weight=1)
                    new_window_in_search_button.columnconfigure(1, weight=1)
                    new_window_in_search_button.columnconfigure(2, weight=1)


                    # showing names datas on new gui in search button
                    for i in range(len(names)):
                        self.listbox_name = tk.Listbox(new_window_in_search_button, heigh=1, width=13, bg="white")
                        self.listbox_name.grid(row=i + 1, column=0, sticky='nswe')
                        self.listbox_name.insert(tk.END, names[i])

                    # showing jobs datas on new gui in search button
                    for i in range(len(jobs)):
                        self.listbox_job = tk.Listbox(new_window_in_search_button, heigh=1, width=13, bg="white")
                        self.listbox_job.grid(row=i + 1, column=1, sticky='nswe')
                        self.listbox_job.insert(tk.END, jobs[i])

                    # showing emails datas on new gui in search button
                    for i in range(len(emails)):
                        self.listbox_email = tk.Listbox(new_window_in_search_button, heigh=1, width=13, bg="white")
                        self.listbox_email.grid(row=i + 1, column=2, sticky='nswe')
                        self.listbox_email.insert(tk.END, jobs[i])

                else:
                    messagebox.showwarning(title="Warning", message="No Records Found")

                break
            else:
                #You should enter at least one entries
                messagebox.showwarning(title="Warning", message="Please enter at least one entries")
                break




    #ok button in add button
    def button_ok_handler(self):
        try:
            while True:
                # taking data's from entries
                name = self.entry_name_in_add_button.get().strip()
                job = self.entry_job_in_add_button.get().strip()
                email = self.entry_email_in_add_button.get().strip()

                if name != "" and job != "" and email != "":
                    # inserting this datas to the databases, inserting db because we are showing all datas from databases
                    cur = self.conn.cursor()
                    cur.execute("INSERT INTO contact_books VALUES(?, ?, ?)", (name, job, email))
                    self.conn.commit()
                    cur.close()

                    #inserting new datas to the trees.
                    self.tree.insert('', 'end', values=[name, job, email])


                    # Deleting datas from every entries, because we can add another contact' values, this will automactily delete
                    self.entry_name_in_add_button.delete(0, tk.END)
                    self.entry_job_in_add_button.delete(0, tk.END)
                    self.entry_email_in_add_button.delete(0, tk.END)

                    break

                else:
                    # if anybody will try to add some contact with empty case, she/he can not do it
                    messagebox.showwarning(title="Warning", message="Please enter all entries")
                    break


        except sqlite3.Error as e:
            print(e)


    #button cancel, inside the add button
    def button_cancel_handler(self):
        # Deleting datas from every entries, because we can add another contact' values, this will automactily delete
        self.entry_name_in_add_button.delete(0, tk.END)
        self.entry_job_in_add_button.delete(0, tk.END)
        self.entry_email_in_add_button.delete(0, tk.END)



#trees haders
employees_header = ['name', 'jobs', "email"]

# connecting databases again, because taking result for inserting new datas from last datas
conn = sqlite3.connect(r'C:\Users\Monster\Desktop\Ozgur_Python_Projeler\contact_books.sqlite')
cur = conn.cursor()
# selecting for taking datas for showing gui
cur.execute("SELECT  * FROM contact_books")

datas = cur.fetchall()

if __name__ == '__main__':
    root = tk.Tk()
    gdb = GUI(root)
    root.mainloop()











