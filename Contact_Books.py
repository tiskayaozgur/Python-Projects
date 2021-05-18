import tkinter as tk
import tkinter.messagebox
import sqlite3
from tkinter import ttk
from tkinter import *

# import tkinter.filedialog
# from tkinter.ttk import *




import tkinter.font as tkFont

class GUI:

    def __init__(self, master):

        master.geometry('1000x800')
        master.title('Contact Books')
        # master.resizable(width=False, height=False)
        self.master = master

        # Db connection and table creation
        self.conn = sqlite3.connect(r'C:\Users\Monster\Desktop\Ozgur_Python_Projeler\contact_books.sqlite')
        cur = self.conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS contact_books(name TEXT, job TEXT, email TEXT)")

        # Creating left frame
        self.left_frame = tk.Frame(self.master, bg="gray", width=10)
        self.left_frame.grid(row=0, column=0, sticky='nswe')

        # Creating Right Frame
        self.right_frame = tk.Frame(self.master, bg="gray", width=10)
        self.right_frame.grid(row=0, column=1, sticky='nswe')

        # when we try to expand horizontal, frame automaticly will expand
        master.columnconfigure(0, weight=2)
        master.columnconfigure(1, weight=1)

        # when we try to expand vertical, frame automaticly will expand
        master.rowconfigure(0, weight=1)


        # Creating add button in rifgt frame
        self.button_add = tk.Button(self.right_frame, text="  ADD  ", command=self.button_add_handler)
        self.button_add.pack(side='left', expand=True)

        # Creating delete button in right frame
        self.button_delete = tk.Button(self.right_frame, text="DELETE", command=self.button_delete_handler)
        self.button_delete.pack(side='left', expand=True)


        #creating tree's and scroll bars
        self.tree = ttk.Treeview(columns=employees_header, show="headings")
        vsb = ttk.Scrollbar(orient="vertical", command=self.tree.yview)
        # hsb = ttk.Scrollbar(orient="horizontal", command=self.tree.xview)
        self.tree.configure(yscrollcommand=vsb.set)
        self.tree.grid(column=0, row=0, sticky='nsew', in_=self.left_frame)
        vsb.grid(column=1, row=0, sticky='ns', in_=self.left_frame)
        # hsb.grid(column=0, row=1, sticky='ew', in_=self.left_frame)
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


    #add button in right frame
    def button_add_handler(self):
        #Creating new window while clicking add button
        new_window = Tk()
        new_window.geometry("300x300")
        new_window.title("New Window")

        #Creating name listbox&entries
        self.label_name = tk.Label(new_window, text='Name:', font='Calibri 12')
        self.label_name.place(x=10, y=10)
        self.entry_name = tk.Entry(new_window, width=15, font='Calibri 12')
        self.entry_name.place(x=70, y=10)

        #Creating job listbox&entries
        self.label_job = tk.Label(new_window, text='Job:', font='Calibri 12')
        self.label_job.place(x=10, y=40)
        self.entry_job = tk.Entry(new_window, width=15, font='Calibri 12')
        self.entry_job.place(x=70, y=40)

        #Creating email listbox&entries
        self.label_email = tk.Label(new_window, text='Email:', font='Calibri 12')
        self.label_email.place(x=10, y=70)
        self.entry_email = tk.Entry(new_window, width=15, font='Calibri 12')
        self.entry_email.place(x=70, y=70)


        #Creating button ok and cancel
        self.button_ok = tk.Button(new_window, text="OK", command=self.button_ok_handler)
        self.button_ok.place(x=25, y=125, heigh=25, width=50)

        self.button_cancel = tk.Button(new_window, text="Cancel", command=self.button_cancel_handler)
        self.button_cancel.place(x=100, y=125, heigh=25, width=50)


    #ok button in add button
    def button_ok_handler(self):
        try:
            while True:
                # taking data's from entries
                name = self.entry_name.get().strip()
                job = self.entry_job.get().strip()
                email = self.entry_email.get().strip()

                if name != "" and job != "" and email != "":
                    # inserting this datas to the databases, inserting db because we are showing all datas from databases
                    cur = self.conn.cursor()
                    cur.execute("INSERT INTO contact_books VALUES(?, ?, ?)", (name, job, email))
                    self.conn.commit()
                    cur.close()

                    #inserting new datas to the trees.
                    self.tree.insert('', 'end', values=[name, job, email])


                    # Deleting datas from every entries, because we can add another contact' values, this will automactily delete
                    self.entry_name.delete(0, tk.END)
                    self.entry_job.delete(0, tk.END)
                    self.entry_email.delete(0, tk.END)

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
        self.entry_name.delete(0, tk.END)
        self.entry_job.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)

    # right frame's delete handler method
    def button_delete_handler(self):

        # deleting datas from GUI(trees)that ve selected
        selected_item = self.tree.selection()[0]

        #creating list because , it will include row elements that we select
        l = []
        #tum trees ıcerısındekı datalarda gezınıyorum
        for line in self.tree.get_children():
            for value in self.tree.item(line)['values']:

            #trees ıcerısınde tıklanmıs yanı secılmıs olan datayı lısteye attım kı oradan da okuyarak database'den de sılecegım kı goruntude de gıtsın.
                if line == selected_item:
                    l.append(value)




        #deleting datas that we choose from database
        sql = "DELETE FROM contact_books WHERE name=? AND job=? AND email=?"
        cur = self.conn.cursor()
        cur.execute(sql, (l[0], l[1], l[2]))
        self.conn.commit()


        # deleting datas from GUI(trees)that ve selected
        self.tree.delete(selected_item)






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











