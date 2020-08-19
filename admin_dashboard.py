from tkinter import *
from tkinter import ttk
from databaseconnection import db_connection
from product_management import Product_App
from supplier_management import Supplier_App
from emp_details import Emp_App
from changepassword import PassUpdate_App
from products_view import View_Products
from supplier_view import View_Supplier
from view_employees import View_Employees
class Dashboard_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1500x700+0+0")
        self.root.title("Dashboard")

        # bg_color= "#588c7e"
        bg_color = "#494949"
        # root.configure(background='#c8c3cc')
        heading= "#F5F5F5"
        sub_heading= "#C8C8C8"
        title=Label(self.root,text="Retail Management System",bd=12,bg=bg_color,fg=heading,font=("times new roman",30,"bold"),padx=10,pady=2).pack(fill=X)

    ########****************************************Functions***************************************########

        def emp_window():
            self.newWindow = Toplevel(self.root)
            self.newWindow = Emp_App(self.newWindow)

        def supplier_window():
            self.newWindow = Toplevel(self.root)
            self.newWindow = Supplier_App(self.newWindow)

        def product_window():
            self.newWindow = Toplevel(self.root)
            self.newWindow = Product_App(self.newWindow)

        def passwordchange_window():
            self.newWindow = Toplevel(self.root)
            self.newWindow = PassUpdate_App(self.newWindow)

        def view_emp_window():
            self.newWindow = Toplevel(self.root)
            self.newWindow = View_Employees(self.newWindow)

        def view_supplier_window():
            self.newWindow = Toplevel(self.root)
            self.newWindow = View_Supplier(self.newWindow)

        def view_product_window():
            self.newWindow = Toplevel(self.root)
            self.newWindow = View_Products(self.newWindow)
        ######## ****************************************View Products***************************************########


        F1 = LabelFrame(self.root,text="Products", bg=bg_color, fg="silver", font=("times new roman", 15, "bold"))
        F1.place(x=10, y=80, width=200,height=150)
        cat_search=Button(F1,text="Click Here",width=10,bg='white',relief="solid",borderwidth=1,font=("times new roman", 12, "bold"),command=view_product_window).grid(row=0, column=0,padx=50,pady=80,sticky=W)







        ######## ****************************************View Suppliers***************************************########




        F2 = LabelFrame(self.root, text="Suppliers",bg=bg_color, fg="silver", font=("times new roman", 15, "bold"))
        F2.place(x=10, y=235, width=200,height=150)
        cat_search = Button(F2, text="Click Here", width=10,bg='white',relief="solid",borderwidth=1, font=("times new roman", 12, "bold"),command=view_supplier_window).grid(row=1, column=0,
                                                                                                    padx=50, pady=80,
                                                                                                    sticky=W)




        ######## ****************************************View Employess***************************************########



        F3 = LabelFrame(self.root, text="Employee", bg=bg_color, fg="silver", font=("times new roman", 15, "bold"))
        F3.place(x=10, y=390, width=200, height=150)
        subcat_search = Button(F3, text="Click Here", bg='white',width=10,relief="solid",borderwidth=1, font=("times new roman", 12, "bold"),command=view_emp_window).grid(row=0, column=0,sticky=W,
                                                                                                    padx=50, pady=80)





        ######## ****************************************Change Password***************************************########


        F5 = LabelFrame(self.root, text="Change Password", bg=bg_color, fg="silver", font=("times new roman", 15, "bold"))
        F5.place(x=10, y=545, width=200,height=150)
        prod_search = Button(F5, text="Click Here", width=10, bg='white',relief="solid",borderwidth=1,font=("times new roman", 12, "bold"),command=passwordchange_window).grid(row=0, column=2,
                                                                                                      sticky=W,
                                                                                                      padx=50, pady=80)






        ####################***************************Manage Products*****************************#######################33



        F6 = LabelFrame(self.root, text="Manage Products",bg=bg_color, fg="silver", font=("times new roman", 15, "bold"))
        F6.place(x=1290, y=80, width=200,height=150)
        cat_search=Button(F6,text="Click Here",width=10,font=("times new roman", 12, "bold"),relief="solid",borderwidth=1,bg='white',command=product_window).grid(row=1, column=0,padx=50,pady=80,sticky=W)






        ######## ****************************************Manage Suppliers**************************************########




        F7 = LabelFrame(self.root, text="Manage Suppliers",bg=bg_color, fg="silver", font=("times new roman", 15, "bold"))
        F7.place(x=1290, y=235, width=200,height=150)
        cat_search = Button(F7, text="Click Here", width=10, font=("times new roman", 12, "bold"),relief="solid",borderwidth=1,bg='white',command=supplier_window).grid(row=1, column=0,
                                                                                                    padx=50, pady=80,
                                                                                                    sticky=W)





        ######## ****************************************Manage Employee***************************************########



        F8 = LabelFrame(self.root, text="Manage Employee", bg=bg_color, fg="silver", font=("times new roman", 15, "bold"))
        F8.place(x=1290, y=390, width=200, height=150)
        subcat_search = Button(F8, text="Click Here", width=10, bg='white',relief="solid",borderwidth=1,font=("times new roman", 12, "bold"),command=emp_window).grid(row=0, column=0,sticky=W,
                                                                                                    padx=50, pady=80)




        ########****************************************Logout***************************************########


        F9 = LabelFrame(self.root, text="Logout", bg=bg_color, fg="silver", font=("times new roman", 15, "bold"))
        F9.place(x=1290, y=545, width=200,height=150)
        prod_search = Button(F9, text="Click Here", width=10, bg='white',relief="solid",borderwidth=1,font=("times new roman", 12, "bold"),command=root.destroy).grid(row=0, column=0,
                                                                                                      sticky=W,
                                                                                                      padx=50, pady=80)





        ############################********************Centre frame**********************############################
        F10 = LabelFrame(self.root, bg="light grey", fg="silver", font=("times new roman", 15, "bold"))
        F10.place(x=220, y=80, width=1060, height=615)

        user = PhotoImage(file="C:/Users/hi/Desktop/retailpic.gif")

        cicon_label = Label(F10, image=user)
        cicon_label.image = user  # keep a reference!
        cicon_label.pack(pady=50)










