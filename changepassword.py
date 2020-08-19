from tkinter import *
from tkinter import ttk,messagebox
from bill_emp import Bill_App
import databaseconnection
class PassUpdate_App:
    def __init__(self,root):
        self.root = root
        self.root.geometry("800x700+400+40")
        self.root.title("Login/Signup")

        bg_color = "#494949"
        root.configure(background='#494949')
        heading = "#F5F5F5"
        sub_heading = "#C8C8C8"


    #################***********************************Variables****************************************##################

        self.username = StringVar()
        self.password = StringVar()
        self.newpassword = StringVar()
        self.connewpassword = StringVar()


    #################***********************************Functions****************************************##################


        def update_window():
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
                if self.username.get() == email[i] and self.password.get() == password[i] and self.connewpassword.get() == self.newpassword.get():

                    databaseconnection.update_emp_details(email[i], self.newpassword.get())
                    messagebox.showinfo("Successful", name[i] + " password is successfully changed")
                elif self.connewpassword.get() != self.newpassword.get():
                    messagebox.showerror("Error", "Password donot match")



        ########******************************   Sub Frame for login details  *************************************#############



        user=PhotoImage(file="C:/Users/hi/Desktop/loginpic.gif")


        cicon_label = Label(root,image=user)
        cicon_label.image = user         # keep a reference!
        cicon_label.pack(pady=50)

        login_v = ['Admin',
                     'Employee',

                     ]



        ########******************************   Login details  *************************************#############

        F01 = LabelFrame(root, fg="#F5F5F5",
                         font=("times new roman", 15, "bold"))
        F01.place(x=160, y=280, width=480, height=400)

        uname_label = Label(F01,bd=12,text="User Id", fg="black",
                            font=("times new roman", 15, "bold"),pady=30).grid(row=1, column=0, padx=10,sticky=W)
        uname_txt = Entry(F01, width=20, font=("times new roman", 15, "bold"),textvariable=self.username).grid(row=1, column=1, padx=10, pady=10,sticky=W)

        pass_label = Label(F01, text="Current Password", bd=12, fg="black",
                            font=("times new roman", 15, "bold")).grid(row=2, column=0, padx=10,sticky=W)
        pass_txt = Entry(F01, width=20, font=("times new roman", 15, "bold"),textvariable=self.password).grid(row=2, column=1, padx=10, pady=20,sticky=W)
        newpass_label = Label(F01, text="New Password", bd=12, fg="black",
                              font=("times new roman", 15, "bold"), pady=2).grid(row=3, column=0, padx=10, pady=10,
                                                                                 sticky=W)
        newpass_txt = Entry(F01, width=20, font=("times new roman", 15, "bold"), textvariable=self.newpassword).grid(
            row=3,
            column=1,
            padx=10,
            pady=10, sticky=W)

        newpass_label = Label(F01, text="Confirm New Password", bd=12, fg="black",
                              font=("times new roman", 15, "bold"), pady=2).grid(row=4, column=0, padx=10, pady=10,
                                                                                 sticky=W)
        newpass_txt = Entry(F01, width=20, font=("times new roman", 15, "bold"), textvariable=self.connewpassword).grid(
            row=4, column=1, padx=10, pady=10, sticky=W)

        login_btn = Button(F01, text="Update", width=18, bg="#494949", fg='white',
                           font=("times new roman", 12, "bold"),command=update_window).place(relx=0.5, rely=0.9, anchor=CENTER)








