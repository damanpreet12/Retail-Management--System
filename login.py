from tkinter import *
from tkinter import ttk,messagebox
from bill_emp import Bill_App
from admin_dashboard import Dashboard_App
import databaseconnection
class Login:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1500x700+0+0")
        self.root.title("Login/Signup")

        bg_color = "#494949"
        root.configure(background='#494949')
        heading = "#F5F5F5"
        sub_heading = "#C8C8C8"


        #########*************************** Variables *****************************#############

        self.username = StringVar()
        self.password = StringVar()
        self.loginas = StringVar()
        self.dbname = StringVar()
        self.dbpassword = StringVar()
        self.dbloginas = StringVar()
        self.loginname = StringVar()



        #########*************************** Functions  *****************************#############

        def bill_window():
            self.newWindow = Toplevel(self.root)
            self.newWindow = Bill_App(self.newWindow)


        def dashboard_window():
            self.newWindow = Toplevel(self.root)
            self.newWindow = Dashboard_App(self.newWindow)


        def login():
            name = []
            password = []
            designation = []
            email = []
            data1 = databaseconnection.fetchdata_emp_login()
            for row in data1:
                name.append(row[0])
                password.append(row[2])
                designation.append(row[1])
                email.append(row[3])

            for i in range(len(name)):
                if self.username.get() == email[i] and self.password.get() == password[i] and self.loginas.get() == \
                        designation[i]:
                    self.dbname.set(self.username.get())
                    self.dbpassword.set(self.password.get())
                    self.dbloginas.set(self.loginas.get())
                    self.loginname.set(name[i])

            if self.username.get() == "" or self.password.get() == "":
                messagebox.showerror("Error", "All fields are required!!")

            elif self.username.get() == self.dbname.get() and self.password.get() == self.dbpassword.get():
                messagebox.showinfo("Successful", f"welcome {self.loginname.get()}")
                if self.loginas.get() == 'Admin':
                    dashboard_window()
                elif self.loginas.get() == 'Employee':
                    bill_window()
            else:
                messagebox.showerror("Error", "Invalid Username or Password")

        #########*************************** Main Frame *****************************#############


        F0 = LabelFrame(self.root, fg="#F5F5F5",
                        font=("times new roman", 15, "bold"))
        F0.place(x=440, y=5, width=600, height=690)
        title = Label(F0, text=" Retail Management System ", bd=12, bg=bg_color, fg=heading,
                      font=("times new roman", 30, "bold"), padx=10, pady=10).pack(pady=30)


        ########******************************   Sub Frame for login details  *************************************#############


        F01 = LabelFrame(F0, fg="#F5F5F5",
                        font=("times new roman", 15, "bold"))
        F01.place(x=70, y=400, width=450,height=260)





        user=PhotoImage(file="C:/Users/hi/Desktop/loginpic.gif")


        cicon_label = Label(root,image=user)
        cicon_label.image = user         # keep a reference!
        cicon_label.pack(pady=170)

        login_v = ['Admin',
                     'Employee',

                     ]

        ########******************************   Login details  *************************************#############

        uname_label = Label(F01, bd=12, text="Login As", fg="black",
                            font=("times new roman", 15, "bold"), pady=2).grid(row=0, column=0, padx=40, pady=10)

        cat_txt = ttk.Combobox(F01, values=login_v, width=15,textvariable=self.loginas, font=("times new roman", 15, "bold")).grid(row=0,
                                                                                                          column=1,
                                                                                                          padx=10,
                                                                                                          pady=5)

        uname_label = Label(F01,bd=12,text="User Id", fg="black",
                            font=("times new roman", 15, "bold"), pady=2).grid(row=1, column=0, padx=40, pady=10)
        uname_txt = Entry(F01, width=20, font=("times new roman", 15, "bold"),textvariable=self.username).grid(row=1, column=1, padx=20, pady=10)

        self.loginas.set('Select')

        pass_label = Label(F01, text="Password", bd=12, fg="black",
                            font=("times new roman", 15, "bold"), pady=2).grid(row=2, column=0, padx=40, pady=10)
        pass_txt = Entry(F01, width=20, font=("times new roman", 15, "bold"),textvariable=self.password).grid(row=2, column=1, padx=20, pady=10)

        login_btn = Button(F01, text="Login", width=18,bg ="#494949",fg=heading, font=("times new roman", 12, "bold"),command = login).place(relx=0.5, rely=0.9, anchor=CENTER)










