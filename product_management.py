from tkinter import *
from tkinter import ttk,messagebox
import databaseconnection
class Product_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1500x700+0+0")
        self.root.title("Products Details")

        bg_color= "#494949"
        # root.configure(background='#c8c3cc')
        heading= "#F5F5F5"
        sub_heading= "#C8C8C8"
        title=Label(self.root,text="Product Management",bd=12,bg=bg_color,fg=heading,font=("times new roman",30,"bold"),padx=10,pady=2).pack(fill=X)



        ######## ****************************************Variables***************************************########

        self.catid = IntVar()
        self.catname = StringVar()
        self.subcatid = IntVar()
        self.subcatname = StringVar()
        self.subcatcat = StringVar()
        self.cprice=StringVar()
        self.sprice=StringVar()
        self.pqty=IntVar()
        self.pname=StringVar()
        self.selectsubcat=StringVar()
        self.selectcat=StringVar()
        self.pid=IntVar()

        ######## ****************************************Functions***************************************########

        def addcat():
            messagebox.showinfo("Add Category", "Successfully added")
            databaseconnection.insert_cat_data(self.catname.get())

        def updatecat():
            messagebox.showinfo("Add Category", "Successfully updated")
            databaseconnection.update_cat_data(self.catname.get(), self.catid.get())

        def fetchcat():
            data = databaseconnection.fetchdata_cat(self.catid.get())
            for row in data:
                self.catname.set(row[0])

        def deletecat():
            messagebox.showinfo("Add Category", "Successfully deleted")
            databaseconnection.delete_data_cat("supplierDetails", self.catid.get())
            self.catname.set(" ")
            self.catid.set(" ")

        def clearcat():
            self.catname.set(" ")
            self.catid.set(" ")

        def addsubcat():
            messagebox.showinfo("Add Sub-Category", "Successfully added")
            databaseconnection.insert_subcat_data(self.subcatname.get(), self.subcatcat.get())

        def updatesubcat():
            messagebox.showinfo("Add Category", "Successfully updated")
            databaseconnection.update_subcat_data(self.subcatname.get(), self.subcatcat.get(), self.subcatid.get())

        def fetchsubcat():
            data = databaseconnection.fetchdata_subcat(self.subcatid.get())
            for row in data:
                self.subcatname.set(row[0])
                self.subcatcat.set(row[1])

        def deletesubcat():
            messagebox.showinfo("Add Category", "Successfully deleted")
            databaseconnection.delete_data_subcat("supplierDetails", self.subcatid.get())
            self.subcatname.set(" ")

            self.subcatid.set(" ")

        def clearsubcat():
            self.subcatname.set(" ")

            self.subcatid.set(" ")

        def addprod():
            messagebox.showinfo("Add Products", "Successfully added")
            databaseconnection.insert_prod_data(self.pname.get(), self.selectcat.get(), self.selectsubcat.get(),
                                                self.pqty.get(), self.sprice.get(), self.cprice.get())

        def updateprod():
            messagebox.showinfo("Add Products", "Successfully updated")
            databaseconnection.update_prod_data(self.pname.get(), self.selectcat.get(), self.selectsubcat.get(),
                                                self.pqty.get(), self.sprice.get(), self.cprice.get(), self.pid.get())

        def fetchprod():
            data = databaseconnection.fetchdata_product(self.pid.get())
            for row in data:
                self.pname.set(row[1])
                self.selectcat.set(row[2])
                self.selectsubcat.set(row[3])
                self.pqty.set(row[4])
                self.sprice.set(row[5])
                self.cprice.set(row[6])

        def deleteprod():
            messagebox.showinfo("Add Products", "Successfully deleted")
            databaseconnection.delete_data_prod(self.pid.get())
            self.pname.set(" ")

            self.pqty.set(" ")
            self.sprice.set(" ")
            self.cprice.set(" ")
            self.pid.set(" ")

        def clearprod():
            self.pname.set(" ")

            self.pqty.set(" ")
            self.sprice.set(" ")
            self.cprice.set(" ")
            self.pid.set(" ")

        def lookupcategory():
            print(selcat_txt.get())

        ######## ****************************************Add Category***************************************########



        F1 = LabelFrame(self.root, text="Add Category", bg=bg_color, fg="silver", font=("times new roman", 15, "bold"))
        F1.place(x=50, y=120, width=625,height=150)


        acat_label=Label(F1, text="Category Id", bd=12, bg=bg_color, fg=sub_heading,
              font=("times new roman", 15, "bold"), pady=2).grid(row=0,column=0,padx=20,pady=5,sticky=W)
        acat_txt=Entry(F1,width=20,font=("times new roman", 15, "bold"),textvariable=self.catid).grid(row=0,column=1,padx=20,pady=5,sticky=W)
        cat_search=Button(F1,text="Search",width=10,font=("times new roman", 12, "bold"),bg='white',relief="solid",borderwidth=1,command=fetchcat).grid(row=0, column=2,padx=20,pady=5,sticky=W)

        self.catid.set(" ")

        catname_label = Label(F1, text="Category Name", bd=12, bg=bg_color, fg=sub_heading,font=("times new roman", 15, "bold"), pady=2).grid(row=1, sticky=W,column=0,padx=20,pady=5)
        catname_txt = Entry(F1, width=20, font=("times new roman", 15, "bold"),textvariable=self.catname).grid(row=1, column=1, padx=20, pady=5,sticky=W)

        F2 = LabelFrame(self.root, bg=bg_color, fg="silver", font=("times new roman", 15, "bold"))
        F2.place(x=50, y=280, width=625,height=80)



        ctotal = Button(F2, text="Add",width=15, font=("times new roman", 12, "bold"),bg='white',relief="solid",borderwidth=1,command=addcat).grid(row=2, column=0,padx=5, pady=20,sticky=W)

        cclear_bill= Button(F2, text="Update",width=15,font=("times new roman", 12, "bold"),bg='white',relief="solid",borderwidth=1,command=updatecat).grid(row=2, column=1,padx=5, pady=5,sticky=W)

        ctotal = Button(F2, text="Delete", width=15,font=("times new roman", 12, "bold"),bg='white',relief="solid",borderwidth=1,command=deletecat).grid(row=2, column=2,padx=5, pady=5,sticky=W)

        cclear_bill= Button(F2, text="Clear",width=15,font=("times new roman", 12, "bold"),bg='white',relief="solid",borderwidth=1,command=clearcat).grid(row=2, column=3,padx=5, pady=5,sticky=W)





        ######## ****************************************Add Sub-Category***************************************########

        F3 = LabelFrame(self.root, text="Add Sub Category", bg=bg_color, fg="silver", font=("times new roman", 15, "bold"))
        F3.place(x=50, y=380, width=625, height=220)

        subcat_label = Label(F3, text="Sub Category Id", bd=12, bg=bg_color, fg=sub_heading,
                           font=("times new roman", 15, "bold"), pady=2).grid(row=0, column=0, padx=20, pady=5,sticky=W)
        subcat_txt = Entry(F3, width=20, font=("times new roman", 15, "bold"),textvariable=self.subcatid).grid(row=0, column=1, padx=20, pady=5,sticky=W)
        subcat_search = Button(F3, text="Search", width=8, font=("times new roman", 12, "bold"),bg='white',relief="solid",borderwidth=1,command=fetchsubcat).grid(row=0, column=2,sticky=W,
                                                                                                    padx=10, pady=5)

        self.subcatid.set(" ")

        data = databaseconnection.fetchcatoptions("categoryDetails")
        cat_select_v =[]
        for row in data:
            cat_select_v.append(row[0])





        cat_label = Label(F3,text="Select Category", bd=12, bg=bg_color, fg=sub_heading,
                          font=("times new roman", 15, "bold"), pady=2).grid(row=1, column=0, padx=20, pady=5,sticky=W)
        cat_txt = ttk.Combobox(F3, values= cat_select_v,width=18, font=("times new roman", 15, "bold"),textvariable=self.subcatcat).grid(row=1, column=1, padx=20, sticky=W,pady=5)

        self.subcatcat.set('Choose')



        subcatname_label = Label(F3, text="Sub Category Name", bd=12, bg=bg_color, fg=sub_heading,
                              font=("times new roman", 15, "bold"), pady=2).grid(row=2, column=0, padx=20, pady=5,sticky=W)
        subcatname_txt = Entry(F3, width=20, font=("times new roman", 15, "bold"),textvariable=self.subcatname).grid(row=2, column=1, padx=20,sticky=W, pady=5)

        F4 = LabelFrame(self.root, bg=bg_color, fg="silver", font=("times new roman", 15, "bold"))
        F4.place(x=50, y=610, width=625, height=70)

        ctotal = Button(F4, text="Add", width=15, font=("times new roman", 12, "bold"),bg='white',relief="solid",borderwidth=1,command=addsubcat).grid(row=2, column=0, padx=5,sticky=W,
                                                                                             pady=20)

        cclear_bill = Button(F4, text="Update", width=15, font=("times new roman", 12, "bold"),bg='white',relief="solid",borderwidth=1,command=updatesubcat).grid(row=2, column=1,sticky=W,
                                                                                                     padx=5, pady=5)

        ctotal = Button(F4, text="Delete", width=15, font=("times new roman", 12, "bold"),bg='white',relief="solid",borderwidth=1,command=deletesubcat).grid(row=2, column=2, padx=5,sticky=W,
                                                                                                pady=5)

        cclear_bill = Button(F4, text="Clear", width=15, font=("times new roman", 12, "bold"),bg='white',relief="solid",borderwidth=1,command=clearsubcat).grid(row=2, column=3,sticky=W,
                                                                                                    padx=5, pady=5)


    ######## ****************************************Products Manage***************************************########


        F5 = LabelFrame(self.root, text="Product Manage", bg=bg_color, fg="silver", font=("times new roman", 15, "bold"))
        F5.place(x=740, y=120, width=700,height=480)


        prod_label = Label(F5, text="Product Id", bd=12, bg=bg_color, fg=sub_heading,
                           font=("times new roman", 15, "bold"), pady=2).grid(row=0, column=0, padx=30, pady=5,
                                                                              sticky=W)
        prod_txt = Entry(F5, width=20, font=("times new roman", 15, "bold"),textvariable=self.pid).grid(row=0, column=1, padx=20, pady=5,
                                                                                  sticky=W)
        self.pid.set(" ")
        prod_search = Button(F5, text="Search", width=8, font=("times new roman", 12, "bold"),bg='white',relief="solid",borderwidth=1,command=fetchprod).grid(row=0, column=2,
                                                                                                      sticky=W,
                                                                                                      padx=10, pady=5)
        data = databaseconnection.fetchcatoptions("categoryDetails")
        selcat_v = []
        for row in data:
            selcat_v.append(row[0])

        selcat_label = Label(F5, text="Select Category", bd=12, bg=bg_color, fg=sub_heading,
                          font=("times new roman", 15, "bold"), pady=2).grid(row=1, column=0, padx=30, pady=5, sticky=W)
        selcat_txt = ttk.Combobox(F5, values=selcat_v, width=18, font=("times new roman", 15, "bold"),textvariable=self.selectcat).grid(row=1,
                                                                                                         column=1,
                                                                                                         padx=20,
                                                                                                         pady=5,
                                                                                                         sticky=W)
        self.selectcat.set('Choose')

        data = databaseconnection.fetchsubcatoptions()
        selsubcat_v = []
        for row in data:
            selsubcat_v.append(row[0])


        selsubcat_label = Label(F5, text="Select Sub Category", bd=12, bg=bg_color, fg=sub_heading,
                             font=("times new roman", 15, "bold"), pady=2).grid(row=2, column=0, padx=30, pady=5,
                                                                                sticky=W)
        selsubcat_txt = ttk.Combobox(F5, values=selsubcat_v, width=18, font=("times new roman", 15, "bold"),textvariable=self.selectsubcat).grid(row=2,
                                                                                                            column=1,
                                                                                                            padx=20,
                                                                                                            pady=5,
                                                                                                            sticky=W)

        self.selectsubcat.set('Choose')
        pname_label = Label(F5, text="Product Name", bd=12, bg=bg_color, fg=sub_heading,
                          font=("times new roman", 15, "bold"), pady=2).grid(row=3, column=0, padx=30, pady=5, sticky=W)
        pname_txt = Entry(F5, width=20, font=("times new roman", 15, "bold"),textvariable=self.pname).grid(row=3, column=1, padx=20, pady=5,
                                                                                sticky=W)


        pqty_label = Label(F5, text="Product QTY", bd=12, bg=bg_color, fg=sub_heading,
                               font=("times new roman", 15, "bold"), pady=2).grid(row=4, sticky=W, column=0, padx=30,
                                                                                  pady=5)
        pqty_txt = Entry(F5, width=20, font=("times new roman", 15, "bold"),textvariable=self.pqty).grid(row=4, column=1, padx=20, pady=5,
                                                                                      sticky=W)
        self.pqty.set(" ")
        sprice_label = Label(F5, text="Selling Price", bd=12, bg=bg_color, fg=sub_heading,
                            font=("times new roman", 15, "bold"), pady=2).grid(row=5, column=0, padx=30, pady=5,
                                                                               sticky=W)
        sprice_name_txt = Entry(F5, width=20, font=("times new roman", 15, "bold"),textvariable=self.sprice).grid(row=5, column=1, padx=20,
                                                                                        pady=5, sticky=W)

        cost_label = Label(F5, text="Cost Price", bd=12, bg=bg_color, fg=sub_heading,
                            font=("times new roman", 15, "bold"), pady=2).grid(row=6, column=0, padx=30, pady=5,
                                                                               sticky=W)
        cost_txt = Entry(F5, width=20, font=("times new roman", 15, "bold"),textvariable=self.cprice).grid(row=6, column=1, padx=20, pady=5,
                                                                                   sticky=W)


        ######## ****************************************Products Manage Buttons***************************************########



        F6 = LabelFrame(self.root, bg=bg_color, fg="silver", font=("times new roman", 15, "bold"))
        F6.place(x=740, y=610, width=700, height=70)

        ctotal = Button(F6, text="Add", width=15, font=("times new roman", 12, "bold"),bg='white',relief="solid",borderwidth=1,command=addprod).grid(row=2, column=0, padx=28,
                                                                                             sticky=W,
                                                                                             pady=20)

        cclear_bill = Button(F6, text="Update", width=15, bg='white',relief="solid",borderwidth=1,font=("times new roman", 12, "bold"),command=updateprod).grid(row=2, column=1,
                                                                                                     sticky=W,
                                                                                                     padx=5, pady=5)

        ctotal = Button(F6, text="Delete", width=15,bg='white',relief="solid",borderwidth=1, font=("times new roman", 12, "bold"),command=deleteprod).grid(row=2, column=2, padx=5,
                                                                                                sticky=W,
                                                                                                pady=5)

        cclear_bill = Button(F6, text="Clear", width=15,bg='white',relief="solid",borderwidth=1, font=("times new roman", 12, "bold"),command=clearprod).grid(row=2, column=3,
                                                                                                    sticky=W,
                                                                                                padx=5, pady=5)




# root=Tk()
# obj=Product_App(root)
# root.mainloop()





