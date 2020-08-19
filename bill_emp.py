from tkinter import *
from tkinter import ttk,messagebox

import databaseconnection
from random import randint
import datetime
import os

import email_sending
class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1500x700+0+0")
        self.root.title("Products Details")

        bg_color= "#494949"
        # root.configure(background='#c8c3cc')
        heading= "#F5F5F5"
        sub_heading= "#C8C8C8"
        title=Label(self.root,text=" Retail Billing System ",bd=12,bg=bg_color,fg=heading,font=("times new roman",30,"bold"),padx=10,pady=2).pack(fill=X)

        ######## ****************************************Variables***************************************########



        self.billsearch=StringVar()
        self.billcategory = StringVar()
        self.billscategory = StringVar()
        self.billproduct = StringVar()
        self.billqty= IntVar()
        self.cname = StringVar()
        self.cphone = StringVar()
        self.cemail = StringVar()
        self.total_bill=StringVar()
        self.bill_number=StringVar()
        self.custid=StringVar()
        self.custidnew = StringVar()
        self.dbcname = StringVar()
        self.dbcphone = StringVar()
        self.dbcemail = StringVar()
        self.emailsend=StringVar()
        self.billpop=StringVar()
        self.dbcustid=StringVar()
        self.dbdate=StringVar()

        # # ######## ****************************************Functions***************************************########

        def add_customer_details():
            if self.cname.get()!="" and self.cemail.get()!="" and self.cphone.get()!="":
                databaseconnection.insert_customer_details(self.cname.get(), self.cemail.get(),self.cphone.get())
                data=databaseconnection.fetchcustomer_id(self.cemail.get())
                for r in data:
                    self.custid.set(r[0])
                messagebox.showinfo("Success", "Successfully added and your customer id is %d" %int(self.custid.get()))
                self.custid.set(data)



            elif self.cname.get()=="" or self.cemail.get()=="" or self.cphone.get()=="":
                messagebox.showerror("Error", "Fill all details")

        def addproducts():
            if self.billproduct.get()!=" " and self.billcategory.get()!=" " and self.billscategory.get()!=" " and self.billqty.get()!=0  and self.custidnew.get()!=" ":
                messagebox.showinfo("Bill Management", "Successfully added")

                databaseconnection.insert_cust_prod(self.billproduct.get(), self.billcategory.get(),
                                                    self.billscategory.get(), self.billqty.get(), self.custidnew.get(),'0')
            else:
                messagebox.showerror("Error", "Fill all details")

        def bill_reference_number():
            count=randint(200,2000000)
            today = datetime.date.today()
            d1 = today.strftime("%d%m%Y")
            now = datetime.datetime.now()
            current_time = now.strftime("%H%M")
            bill_numb ='DK'+"-"+str(count)+str(d1)+str(current_time)
            return bill_numb

        def create_bill():

            today = datetime.date.today()
            d1 = today.strftime("%d%m%Y")
            now = datetime.datetime.now()
            current_time = now.strftime("%H%M")
            bill_txt =  str(d1) + str(current_time)
            billtitle='BILL'+self.custidnew.get() +bill_txt
            title =billtitle + ".txt"
            global path
            path = 'D:\\New folder'
            with open(os.path.join(path, title), "w") as file1:
                toFile = generate_bill()
                file1.write(toFile)
            qmsg = messagebox.showinfo("Information", "Bill Generated")
            data=databaseconnection.fetchdata_customer_details(int(self.custidnew.get()))

            for i in data:
                self.emailsend.set(i[1])

            email_sending.send_bill(path,billtitle,self.emailsend.get())

        def add_cart():
            self.textout.delete('1.0', END)
            self.textout.insert(INSERT,cart_view())
        def total_preview():
            self.txtarea.delete('1.0', END)
            self.txtarea.insert(INSERT,bill_preview())


        def billfetch():
            self.txtarea.delete('1.0', END)
            self.txtarea.insert(INSERT,fetchsearchbill())
        def cart_view():
            data = databaseconnection.fetch_cust_products(self.custidnew.get())
            products = []
            productscost = []
            qty = []
            for row in data:
                products.append(row[0])
                qty.append(row[1])

            billstring =""

            billstring +="======================================================="
            billstring +="\n"
            billstring += "{:<30}{:<10}{:<15}\n".format("Product Name","Quantity(Qty)","Price")
            billstring += "\n"
            billstring +="========================================================"
            billstring += "\n"
            for i in range(0, len(products)):
                data = databaseconnection.fetchdata_product_cost(products[i])
                for row in data:
                    productscost.append(row[0])


            blist = ""
            for i in range(0, len(products)):
                blist += '{:<30}  {:<10} {:<15}\n'.format(products[i], qty[i], productscost[i])
            blist +="\n"
            blist +="========================================================"

            return billstring + blist







        def generate_bill():
            data = databaseconnection.fetch_cust_products(self.custidnew.get())
            self.bill_number.set(bill_reference_number())
            products = []
            productscost = []
            qty = []
            for row in data:
                products.append(row[0])
                qty.append(row[1])
            cost = 0
            data1 = databaseconnection.fetchdata_customer_details(int(self.custidnew.get()))
            for row in data1:
                self.dbcname.set(row[0])
                self.dbcemail.set(row[1])
                self.dbcphone.set(row[2])

            billstring =""
            billstring = "           *************D.K Retailers**************        "
            billstring += "\n                  142 Your Address Blvd"
            billstring += "\n               Sangrur,Punjab,India,148001"
            billstring += "\n                Phone no. :8996895635"
            billstring += "\n                Email :dkaur4381@gmail.com"
            billstring += "\n\n\n"

            billstring += "\n Customer Name    : {} ".format(self.dbcname.get())

            billstring += "\n Phone Number     : {} ".format(self.dbcphone.get())
            billstring += "\n Email            : {} ".format(self.dbcemail.get())
            billstring += "\n Bill Number      : {} ".format(self.bill_number.get())

            billstring += "\n Date             : {} ".format(datetime.datetime.now())

            billstring += "\n\n"
            billstring += "==========================================================="
            billstring += "\n"
            billstring += "{:<30}{:<10}{:<15}\n".format("Product Name","Quantity","Price")
            billstring += "\n"
            billstring += "==========================================================="
            billstring += "\n"
            for i in range(0, len(products)):
                data = databaseconnection.fetchdata_product_cost(products[i])
                for row in data:
                    productscost.append(row[0])
            for i in range(0, len(products)):
                cost += int(productscost[i]) * qty[i]

            blist =""
            for i in range(0, len(products)):
                blist += '{:<30}  {:<10} {:<15}\n'.format(products[i], qty[i], productscost[i])
            blist += "\n"
            blist += "==========================================================="
            blist += "\nTotal                                     Rs." + str(cost)
            self.total_bill.set(cost)
            databaseconnection.insert_cust_details(self.bill_number.get(),self.custidnew.get(),self.dbcname.get(), self.dbcemail.get(), self.dbcphone.get(),self.total_bill.get(),datetime.date.today())
            databaseconnection.update_custproddetails("1",self.custidnew.get(),self.bill_number.get())


            messagebox.showinfo("Bill Management", "Successfully added")

            return billstring + blist

        def clearproducts():
            self.billproduct.set("Choose")
            self.billcategory.set("Choose")
            self.billscategory.set("Choose")
            self.billqty.set(" ")

        def bill_preview():
            data = databaseconnection.fetch_cust_products(self.custidnew.get())
            products = []
            productscost = []
            qty = []
            for row in data:
                products.append(row[0])
                qty.append(row[1])
            cost=0
            data1 = databaseconnection.fetchdata_customer_details(int(self.custidnew.get()))
            for row in data1:
                self.dbcname.set(row[0])
                self.dbcemail.set(row[1])
                self.dbcphone.set(row[2])
            print(self.dbcphone.get())
            billstring =""
            billstring = "           *************D.K Retailers**************        "
            billstring += "\n                  142 Your Address Blvd"
            billstring += "\n               Sangrur,Punjab,India,148001"
            billstring += "\n                Phone no. :8996895635"
            billstring += "\n                Email :dkaur4381@gmail.com"
            billstring += "\n\n\n"

            billstring += "\n Customer Name    : {} ".format(self.dbcname.get())


            billstring += "\n Email            : {} ".format(self.dbcemail.get())
            billstring += "\n Phone Number     : {} ".format(self.dbcphone.get())
            billstring += "\n Bill Number      :    "

            billstring += "\n Date             : {} ".format(datetime.datetime.now())

            billstring += "\n"
            billstring += "==========================================================="
            billstring += "\n"
            billstring += "{:<30}{:<10}{:<15}\n".format("Product Name","Quantity","Price")
            billstring += "\n"

            billstring += "==========================================================="
            billstring += "\n"
            for i in range(0, len(products)):
                data = databaseconnection.fetchdata_product_cost(products[i])
                for row in data:
                    productscost.append(row[0])
            for i in range(0, len(products)):

                cost += int(productscost[i]) * qty[i]

            blist =""
            for i in range(0, len(products)):
                blist += '{:<30}  {:<10} {:<15}\n'.format(products[i], qty[i], productscost[i])
            blist += "\n"
            blist += "==========================================================="
            blist += "\nTotal                                      Rs." + str(cost)
            qty.clear()
            productscost.clear()
            products.clear()
            return billstring + blist

        def fetchsearchbill():
            data1 = databaseconnection.fetchdata_cust_details(self.billsearch.get())
            for row in data1:
                self.dbcustid.set(row[0])
                self.dbcname.set(row[1])
                self.dbcemail.set(row[2])
                self.dbcphone.set(row[3])
                self.billpop.set(row[4])
                self.dbdate.set(row[5])

            data = databaseconnection.fetch_cust_products_details(self.dbcustid.get(),self.billsearch.get())

            products = []
            productscost = []
            qty = []
            for row in data:
                products.append(row[0])
                qty.append(row[1])
            cost = 0



            billstring = ""
            billstring = "           *************D.K Retailers**************        "
            billstring += "\n                  142 Your Address Blvd"
            billstring += "\n               Sangrur,Punjab,India,148001"
            billstring += "\n                Phone no. :8996895635"
            billstring += "\n                Email :dkaur4381@gmail.com"
            billstring += "\n\n\n"

            billstring += "\n Customer Name    : {} ".format(self.dbcname.get())

            billstring += "\n Phone Number     : {} ".format(self.dbcphone.get())
            billstring += "\n Email            : {} ".format(self.dbcemail.get())
            billstring += "\n Bill Number      : {} ".format(self.billsearch.get())

            billstring += "\n Date             : {} ".format(self.dbdate.get())

            billstring += "\n\n"
            billstring += "==========================================================="
            billstring += "\n"
            billstring += "{:<30}{:<10}{:<15}\n".format("Product Name", "Quantity", "Price")
            billstring += "\n"
            billstring += "==========================================================="
            billstring += "\n"
            for i in range(0, len(products)):
                data = databaseconnection.fetchdata_product_cost(products[i])
                for row in data:
                    productscost.append(row[0])
            for i in range(0, len(products)):
                cost += int(productscost[i]) * qty[i]

            blist = ""
            for i in range(0, len(products)):
                blist += '{:<30}  {:<10} {:<15}\n'.format(products[i], qty[i], productscost[i])
            blist += "\n"
            blist += "==========================================================="
            blist += "\n    Total                         Rs." + str(self.billpop.get())


            return billstring + blist

        def clearall():
            self.billproduct.set("Choose")
            self.billcategory.set("Choose")
            self.billscategory.set("Choose")
            self.billqty.set(" ")
            self.cname.set(" ")
            self.cemail.set(" ")
            self.cphone.set(" ")
            self.billsearch.set(" ")
            self.custidnew.set(" ")
            self.textout.delete('1.0', END)
            self.txtarea.delete('1.0', END)
        ######## ****************************************Billing details***************************************########


        F1=LabelFrame(self.root,text="Billing Details",bg=bg_color,fg="#F5F5F5",font=("times new roman",15,"bold"))
        F1.place(x=10,y=100,width=1475)

        bill_label=Label(F1, text=" Bill Number", bd=12, bg=bg_color, fg=sub_heading,
              font=("times new roman", 15, "bold"), pady=2).grid(row=0,column=0,padx=5,pady=5,sticky=W)
        bill_txt=Entry(F1,width=10,font=("times new roman", 15, "bold"),textvariable=self.billsearch).grid(row=0,column=1,padx=10,pady=5,sticky=W)
        search=Button(F1,text="Search",width=10,bg='white',relief="solid",borderwidth=1,font=("times new roman", 10, "bold"),command=billfetch).grid(row=0, column=2,padx=5,pady=5,sticky=W)

        cname_label = Label(F1, text="Customer Name", bd=12, bg=bg_color, fg=sub_heading,font=("times new roman", 15, "bold"), pady=2).grid(row=0,sticky=W, column=3,padx=10,pady=5)
        cname_txt = Entry(F1, width=17, font=("times new roman", 15, "bold"),textvariable=self.cname).grid(row=0, column=4, padx=10, pady=5,sticky=W)

        pnumb_label = Label(F1, text="Phone Number", bd=12, bg=bg_color, fg=sub_heading,
                            font=("times new roman", 15, "bold"), pady=2).grid(row=0, column=5, padx=10, pady=5,sticky=W)
        pnumb_txt = Entry(F1, width=17, font=("times new roman", 15, "bold"),textvariable=self.cphone).grid(row=0, column=6, padx=10, pady=5,sticky=W)

        pnumb_label = Label(F1, text="Customer Email", bd=12, bg=bg_color, fg=sub_heading,
                            font=("times new roman", 15, "bold"), pady=2).grid(row=0, column=7, padx=10, pady=5,
                                                                               sticky=W)
        pnumb_txt = Entry(F1, width=17, font=("times new roman", 15, "bold"),textvariable=self.cemail).grid(row=0, column=8, padx=10, pady=5,
                                                                                   sticky=W)

        ######## ****************************************Products details***************************************########


        F2 = LabelFrame(self.root, text="Products", bg=bg_color, fg="silver", font=("times new roman", 15, "bold"))
        F2.place(x=10, y=200, width=400,height=390)

        data = databaseconnection.fetchcatoptions("categoryDetails")
        cat_txt_v = []
        for row in data:
            cat_txt_v.append(row[0])


        data = databaseconnection.fetchsubcatoptions()
        sub_cat_txt_v = []
        for row in data:
            sub_cat_txt_v.append(row[0])

        data = databaseconnection.fetchproducts()
        prod = []
        for row in data:
            prod.append(row[0])



        cat_label = Label(F2,text="Select Category", bd=12, bg=bg_color, fg=sub_heading,
                          font=("times new roman", 15, "bold"), pady=2).grid(row=1, column=0, padx=10, pady=5,sticky=W)
        cat_txt = ttk.Combobox(F2, values= cat_txt_v,width=15, textvariable=self.billcategory,font=("times new roman", 15, "bold")).grid(row=1, column=1, padx=10, pady=5,sticky=W)




        self.billcategory.set('Choose')
        sub_cat_label = Label(F2, text="Sub Category", bd=12, bg=bg_color, fg=sub_heading,
                              font=("times new roman", 15, "bold"), pady=2).grid(row=2, column=0, padx=10, pady=5,sticky=W)
        sub_cat_txt = ttk.Combobox(F2, values=sub_cat_txt_v, width=15, font=("times new roman", 15, "bold"),textvariable=self.billscategory).grid(row=2,
                                                                                                              column=1,
                                                                                                              padx=10,
                                                                                                              pady=5,sticky=W)

        self.billscategory.set('Choose')
        product_label = Label(F2, text="Product", bd=12, bg=bg_color, fg=sub_heading,
                              font=("times new roman", 15, "bold"), pady=2).grid(row=3, column=0, padx=10, pady=5,sticky=W)
        product_txt = ttk.Combobox(F2, values=prod, width=15, font=("times new roman", 15, "bold"),textvariable=self.billproduct).grid(row=3,
                                                                                                              column=1,
                                                                                                              padx=10,
                                                                                                              pady=5,sticky=W)

        self.billproduct.set("Choose")
        quantity_label = Label(F2, text="Quantity", bd=12, bg=bg_color, fg=sub_heading,
                              font=("times new roman", 15, "bold"), pady=2).grid(row=4, column=0, padx=10, pady=5,sticky=W)
        quantity_txt = Entry(F2, width=15, font=("times new roman", 15, "bold"),textvariable=self.billqty).grid(row=4,
                                                                                                              column=1,
                                                                                                              padx=10,
                                                                                                              pady=5,sticky=W)

        self.billqty.set(" ")
        cid_label = Label(F2, text="Customer Id", bd=12, bg=bg_color, fg=sub_heading,
                               font=("times new roman", 15, "bold"), pady=2).grid(row=5, column=0, padx=10, pady=5,
                                                                                  sticky=W)
        cid_txt = Entry(F2, width=15, font=("times new roman", 15, "bold"), textvariable=self.custidnew).grid(row=5,
                                                                                                                 column=1,
                                                                                                                 padx=10,
                                                                                                                 pady=5,
                                                                                                                 sticky=W)

        self.custid.set(" ")

        cart = Button(F2, text="Add to Cart", width=10, bg='white',relief="solid",borderwidth=1,font=("times new roman", 12, "bold"),command=addproducts).grid(row=6, column=0,
                                                                                                padx=50, pady=15,sticky=W)
        clear = Button(F2, text="Clear", width=10,bg='white',relief="solid",borderwidth=1, font=("times new roman", 12, "bold"),command=clearproducts).grid(row=6, column=1,sticky=W, padx=30, pady=15,
                                                                                            )


        ######## ****************************************Calculator***************************************########

        F6 = LabelFrame(self.root, bg="#494949", fg="white",text="Cart" ,font=("times new roman", 15, "bold"))
        F6.place(x=440, y=200, width=500, height=360)

        # F5 = LabelFrame(self.root, bg="#494949", fg="white", text="Cart", font=("times new roman", 15, "bold"))
        # F5.place(x=440, y=220, width=500, height=70)
        #
        # quantity_txt = Entry(F5, width=15, font=("times new roman", 15, "bold"), textvariable=self.yesno).grid(row=4,
        #                                                                                                          column=1,
        #                                                                                                          padx=10,
        #                                                                                                          pady=5,
        #                                                                                                          sticky=W)

        scroll_y = Scrollbar(F6, orient=VERTICAL)

        self.textout = Text(F6, yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.textout.yview)
        self.textout.pack(fill=BOTH, expand=1)
        self.textout.delete('1.0', END)

        F8 = LabelFrame(self.root, bg="#494949", fg="white",  font=("times new roman", 15, "bold"))
        F8.place(x=440, y=540, width=500, height=50)
        clear = Button(F8, text="View Cart", width=10, bg='white', relief="solid", borderwidth=1,
                       font=("times new roman", 12, "bold"), command=add_cart).grid(row=0, column=0, sticky=W, padx=20,
                                                                                    pady=1,
                                                                                    )
        cid_label = Label(F8, text="Customer Id", bd=12, bg=bg_color, fg=sub_heading,
                          font=("times new roman", 15, "bold"), pady=2).grid(row=0, column=1, padx=10, pady=1,
                                                                             sticky=W)
        cid_txt = Entry(F8, width=15, font=("times new roman", 15, "bold"), textvariable=self.custid).grid(row=0,
                                                                                                           column=2,
                                                                                                           padx=10,
                                                                                                           pady=1,
                                                                                                           sticky=W)

        # num_7 = Button(F3, text="7", width=10, font=("times new roman", 12, "bold"),bg='white',relief="solid",borderwidth=1).grid(row=2, column=0,columnspan=2,padx=10,pady=17)
        # num_8= Button(F3, text="8", width=10, bg='white',relief="solid",borderwidth=1,font=("times new roman", 12, "bold")).grid(row=2, column=2,columnspan=2,padx=10,pady=15)
        #
        # num_9 = Button(F3, text="9", width=10, bg='white',relief="solid",borderwidth=1,font=("times new roman", 12, "bold")).grid(row=2, column=4,columnspan=2,padx=10,pady=15)
        #
        # num_plus = Button(F3, text="+", width=10,bg='white',relief="solid",borderwidth=1, font=("times new roman", 12, "bold")).grid(row=2, column=6, columnspan=2,
        #                                                                                   padx=10, pady=15)
        #
        # num_4 = Button(F3, text="4", width=10,bg='white',relief="solid",borderwidth=1, font=("times new roman", 12, "bold")).grid(row=3, column=0, columnspan=2,
        #                                                                                   padx=10, pady=15)
        # num_5 = Button(F3, text="5", width=10,bg='white',relief="solid",borderwidth=1, font=("times new roman", 12, "bold")).grid(row=3, column=2, columnspan=2,
        #                                                                                   padx=10, pady=15)
        #
        # num_6 = Button(F3, text="6", width=10,bg='white',relief="solid",borderwidth=1, font=("times new roman", 12, "bold")).grid(row=3, column=4, columnspan=2,
        #
        #
        #                                                                                   padx=10, pady=15)
        #
        # num_minus = Button(F3, text="-", width=10, bg='white',relief="solid",borderwidth=1,font=("times new roman", 12, "bold")).grid(row=3, column=6,
        #                                                                                      columnspan=2,
        #                                                                                      padx=10, pady=15)
        #
        # num_3 = Button(F3, text="3", width=10,bg='white',relief="solid",borderwidth=1, font=("times new roman", 12, "bold")).grid(row=4, column=0, columnspan=2,
        #                                                                                   padx=10, pady=15)
        # num_2 = Button(F3, text="2", width=10, bg='white',relief="solid",borderwidth=1,font=("times new roman", 12, "bold")).grid(row=4, column=2, columnspan=2,
        #                                                                                   padx=10, pady=15)
        #
        # num_1 = Button(F3, text="1", width=10, bg='white',relief="solid",borderwidth=1,font=("times new roman", 12, "bold")).grid(row=4, column=4, columnspan=2,
        #                                                                                   padx=10, pady=15)
        # num_mul= Button(F3, text="*", width=10,bg='white',relief="solid",borderwidth=1, font=("times new roman", 12, "bold")).grid(row=4, column=6,
        #                                                                                      columnspan=2,
        #                                                                                      padx=10, pady=15)
        #
        # num_0 = Button(F3, text="0", width=10,bg='white',relief="solid",borderwidth=1, font=("times new roman", 12, "bold")).grid(row=5, column=0, columnspan=2,
        #                                                                                   padx=10, pady=15)
        # num_c = Button(F3, text="C", width=10,bg='white',relief="solid",borderwidth=1, font=("times new roman", 12, "bold")).grid(row=5, column=2, columnspan=2,
        #                                                                                   padx=10, pady=15)
        #
        # num_equal= Button(F3, text="=", width=10, bg='white',relief="solid",borderwidth=1,font=("times new roman", 12, "bold")).grid(row=5, column=4, columnspan=2,
        #                                                                                   padx=10, pady=15)
        # num_div = Button(F3, text="/", width=10, bg='white',relief="solid",borderwidth=1,font=("times new roman", 12, "bold")).grid(row=5, column=6,
        #                                                                                     columnspan=2,
        #                                                                                     padx=10, pady=15)

        ######## ****************************************Customer Bill*************************************** ########

        F4 = LabelFrame(self.root, text="Customer Bill", bg=bg_color, fg="silver", font=("times new roman", 15, "bold"))
        F4.place(x=970, y=200, width=510, height=490)

        bill_label = Label(F4, text=" Customer Bill", bd=12, bg="white", fg=sub_heading,
                           font=("times new roman", 15, "bold"), pady=2).pack(fill=X)

        scroll_y = Scrollbar(F4, orient=VERTICAL)
        self.txtarea = Text(F4, yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)
        self.txtarea.delete('1.0', END)







        ######## ****************************************Customer Bill***************************************########

        F5 = LabelFrame(self.root, text="Bill Option", bg=bg_color, fg="silver", font=("times new roman", 15, "bold"))
        F5.place(x=10, y=600, width=930, height=90)

        total = Button(F5, text="Add Details", width=15, bg='white', relief="solid", borderwidth=1,
                       font=("times new roman", 12, "bold"), command=add_customer_details).grid(row=0, column=0, columnspan=2,
                                                                                         padx=20, pady=10)

        total = Button(F5, text="Total", width=15, bg='white',relief="solid",borderwidth=1,font=("times new roman", 12, "bold"),command=total_preview).grid(row=0, column=2,columnspan=2,padx=20,pady=10)
        generate= Button(F5, text="Generate Bill",bg='white',relief="solid",borderwidth=1, width=15, font=("times new roman", 12, "bold")
                         ,command=create_bill).grid(row=0, column=4,columnspan=2,padx=20,pady=10)

        clear_bill= Button(F5, text="Clear", bg='white',relief="solid",borderwidth=1,width=15, font=("times new roman", 12, "bold"),command=clearall).grid(row=0, column=6,columnspan=2,padx=20,pady=10)
        exit= Button(F5, text="Exit", width=15,bg='white',relief="solid",borderwidth=1, font=("times new roman", 12, "bold"),command=root.destroy).grid(row=0, column=8,columnspan=2,padx=20,pady=10)





# root=Tk()
# obj=Bill_App(root)
# root.mainloop()








