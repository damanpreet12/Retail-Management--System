from tkinter import *
from tkinter import ttk,messagebox
import databaseconnection
class View_Employees:


    def __init__(self,root):
        self.root=root
        self.root.geometry("1500x700+0+0")
        self.root.title("Products Details")

        bg_color= "#494949"
        # root.configure(background='#c8c3cc')
        heading= "#F5F5F5"
        sub_heading= "#C8C8C8"
        title=Label(self.root,text="View Employees Page ",bd=12,bg=bg_color,fg=heading,font=("times new roman",30,"bold"),padx=10,pady=2).pack(fill=X)



        #########################*************************** Variables *******************************###########################


        self.empsearch=IntVar()


        #########################***************************Functions*******************************###########################

        def fetchdata():
            self.txtarea.delete('1.0', END)
            self.txtarea.insert(INSERT, fetch())

        def detailsdata():
            self.txtarea.delete('1.0', END)
            self.txtarea.insert(INSERT, details())


        def details():
            id = []
            name = []
            email = []
            password = []
            mobile = []
            designation = []
            gender = []
            address = []
            proof = []
            proofnumb = []
            data=databaseconnection.fetchdata_emp_details()

            for i in data:
                id.append(i[0])
                name.append(i[1])
                email.append(i[2])
                password.append(i[3])
                mobile.append(i[4])
                designation.append(i[5])
                gender.append(i[6])
                address.append(i[7])
                proof.append(i[8])
                proofnumb.append(i[9])

            blist = ""

            for i in range(0, len(id)):

                blist += '  {:<8}  {:<23} {:<27}  {:<10}  {:<20} {:<15} {:<15}{:<15} {:<10} {:<10}\n'.format( id[i],name[i],email[i],designation[i],address[i],proof[i],proofnumb[i],mobile[i],gender[i],password[i])
            blist += "\n"
            return blist

        def fetch():
            id = []
            name = []
            email = []
            password = []
            mobile = []
            designation = []
            gender = []
            address = []
            proof = []
            proofnumb = []
            data = databaseconnection.fetchdata_emp(self.empsearch.get())

            for i in data:
                id.append(i[0])
                name.append(i[1])
                email.append(i[2])
                password.append(i[3])
                mobile.append(i[4])
                designation.append(i[5])
                gender.append(i[6])
                address.append(i[7])
                proof.append(i[8])
                proofnumb.append(i[9])

            blist = ""

            for i in range(0, len(id)):
                blist += '   {:<8}  {:<23} {:<27}  {:<10}  {:<20} {:<15} {:<15}{:<15} {:<10} {:<10}\n'.format(id[i],name[i],email[i],designation[i],address[i],proof[i], proofnumb[i], mobile[i],gender[i],password[i])






            blist += "\n"
            return blist
        def cleardata():
             self.empsearch.set(" ")
             self.txtarea.delete('1.0', END)

        #########################********************************************************************############################


        F1 = LabelFrame(self.root, text="Search Employees", bg=bg_color, fg="#F5F5F5",
                        font=("times new roman", 15, "bold"))
        F1.place(x=330, y=100,width=850)

        emp_label = Label(F1, text=" Employee Id", bd=12, bg=bg_color, fg=sub_heading,
                           font=("times new roman", 15, "bold"), pady=2).grid(row=0, column=0, padx=30, pady=5)
        emp_txt = Entry(F1, width=20, font=("times new roman", 15, "bold"),textvariable=self.empsearch).grid(row=0, column=1, padx=20, pady=5)
        emp_search = Button(F1, text="Search", width=10, font=("times new roman", 12, "bold"),bg='white',relief="solid",borderwidth=1,command=fetchdata).grid(row=0, column=2,
                                                                                                padx=20, pady=5)
        emp_search = Button(F1, text="Show All", width=10, font=("times new roman", 12, "bold"), bg='white',
                            relief="solid", borderwidth=1, command=detailsdata).grid(row=0, column=3,
                                                                                   padx=20, pady=5)
        emp_search = Button(F1, text="Clear", width=10, font=("times new roman", 12, "bold"), bg='white',
                            relief="solid", borderwidth=1, command=cleardata).grid(row=0, column=4,
                                                                                   padx=20, pady=5)

        self.empsearch.set(" ")

        F4 = LabelFrame(self.root, text="View Employees", bg=bg_color, fg="silver",
                        font=("times new roman", 15, "bold"))
        F4.place(x=50, y=210, width=1400, height=450)

        F5 = LabelFrame(F4, bg='white', fg="silver", font=("times new roman", 15, "bold"))
        F5.place(x=0, y=0, width=1380, height=60)
        Label(F5, text="Id", bd=12, bg='white', fg='black', font=("times new roman", 14, "bold"),padx=15,pady=2).grid(row=0, column=0,sticky=W)
        Label(F5, text="Name", bd=12, bg='white', fg='black', font=("times new roman", 14, "bold"),padx=40, pady=2).grid(row=0, column=1,sticky=W)
        Label(F5, text="Email", bd=12, bg='white', fg='black', font=("times new roman", 14, "bold"),padx=100, pady=2).grid(row=0, column=2,sticky=W)
        Label(F5, text="Designation", bd=12, bg='white', fg='black', font=("times new roman", 14, "bold"), padx=5,
              pady=2).grid(row=0, column=3, sticky=W)

        Label(F5, text="Address", bd=12, bg='white', fg='black', font=("times new roman", 14, "bold"), padx=5,pady=2).grid(row=0, column=4, sticky=W)
        Label(F5, text="Proof", bd=12, bg='white', fg='black', font=("times new roman", 14, "bold"), padx=55,pady=2).grid(row=0, column=5, sticky=W)
        Label(F5, text="Proof No.", bd=12, bg='white', fg='black', font=("times new roman", 14, "bold"), padx=0,pady=2).grid(row=0, column=6)
        Label(F5, text="Mobile", bd=12, bg='white', fg='black', font=("times new roman", 14, "bold"), padx=15,
              pady=2).grid(row=0, column=7, sticky=W)

        Label(F5, text="Gender", bd=12, bg='white', fg='black', font=("times new roman", 14, "bold"), padx=17,
              pady=2).grid(row=0, column=8, sticky=W)
        Label(F5, text="Password", bd=12, bg='white', fg='black', font=("times new roman", 14, "bold"), padx=0,
              pady=2).grid(row=0, column=9)

        F6 = LabelFrame(F4, bg='white', fg="silver", font=("times new roman", 15, "bold"))
        F6.place(x=0, y=59, width=1380, height=500)
        scroll_y = Scrollbar(F6, orient=VERTICAL)
        scroll_x = Scrollbar(F6, orient=HORIZONTAL)
        self.txtarea = Text(F6, yscrollcommand=scroll_y.set, xscrollcommand=scroll_x)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)
        self.txtarea.insert(INSERT, details())



# root=Tk()
# obj=View_Employees(root)
# root.mainloop()