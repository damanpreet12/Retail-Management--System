from tkinter import *
from tkinter import ttk,messagebox
import databaseconnection
import datetime
from random import randint
class Supplier_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1500x700+0+0")
        self.root.title("Supplier Management")

        bg_color= "#494949"
        # root.configure(background='#c8c3cc')
        heading= "#F5F5F5"
        sub_heading= "#C8C8C8"
        title=Label(self.root,text="Supplier Management ",bd=12,bg=bg_color,fg=heading,font=("times new roman",30,"bold"),padx=10,pady=2).pack(fill=X)

        ######## ****************************************Variables***************************************########

        self.invoice=StringVar()
        self.sname=StringVar()
        self.contact=StringVar()
        self.product=StringVar()
        self.qty=IntVar()
        self.searchinvoice=StringVar()

        ######## **************************************** Functions  ***************************************########

        def invoice():
            count=randint(2,200)
            today = datetime.date.today()
            d1 = today.strftime("%d%m%Y")
            now = datetime.datetime.now()
            current_time = now.strftime("%H%M")
            bill_numb ='#'+str(count)+str(d1)+str(current_time)
            self.invoice.set(bill_numb)
            return self.invoice.get()
        def add():

            messagebox.showinfo("Supplier Management", "Successfully added")
            databaseconnection.insert_supp_data(self.invoice.get(), self.sname.get(), self.contact.get(),
                                                self.qty.get(), self.product.get())

        def update():
            messagebox.showinfo("Supplier Management", "Successfully updated")
            databaseconnection.update_supp_data(self.sname.get(), self.contact.get(), self.qty.get(),
                                                self.product.get(), self.invoice.get())

        def fetch():

            data = databaseconnection.fetchdata_supplier(self.searchinvoice.get())
            for row in data:
                self.invoice.set(row[0])
                self.sname.set(row[1])
                self.contact.set(row[2])
                self.qty.set(row[3])
                self.product.set(row[4])

        def delete():
            messagebox.showinfo("Supplier Management", "Successfully deleted")
            databaseconnection.delete_data_supp("supplierDetails", self.searchinvoice.get())
            self.invoice.set(" ")
            self.sname.set(" ")
            self.contact.set(" ")
            self.qty.set(" ")
            self.product.set('Select')
            self.searchinvoice.set('')

        def clear():

            self.invoice.set(" ")
            self.sname.set(" ")
            self.contact.set(" ")
            self.qty.set(" ")
            self.product.set('Select')
            self.searchinvoice.set('')

        ######## ****************************************Search Suppliers***************************************########

        F1 = LabelFrame(self.root, text="Search Supplier", bg=bg_color, fg="#F5F5F5",
                        font=("times new roman", 15, "bold"))
        F1.place(x=450, y=120,width=600)

        sup_label = Label(F1, text="Invoice No.", bd=12, bg=bg_color, fg=sub_heading,
                           font=("times new roman", 15, "bold"), pady=2).grid(row=0, column=0, padx=30, pady=5)
        sup_txt = Entry(F1, width=20, font=("times new roman", 15, "bold"),textvariable=self.searchinvoice).grid(row=0, column=1, padx=20, pady=5)
        sup_search = Button(F1, text="Search", width=10,bg='white',relief="solid",borderwidth=1, font=("times new roman", 12, "bold"),command=fetch).grid(row=0, column=2,
                                                                                                padx=20, pady=5)
        ######## **************************************** Supplier Details***************************************########

        F2=LabelFrame(self.root,bg=bg_color,fg="#F5F5F5",font=("times new roman",15,"bold"))
        F2.place(x=450,y=250,width=600,height=320)

        supplier_label = Label(F2, text="Invoice No.", bd=12, bg=bg_color, fg=sub_heading,
                           font=("times new roman", 15, "bold"), pady=2).grid(row=0, column=0, padx=30, pady=5,sticky=W)
        supplier_txt = Entry(F2, width=20, font=("times new roman", 15, "bold"),textvariable=self.invoice).grid(row=0, column=1, padx=30, pady=5,sticky=W)

        generate = Button(F2, text="Generate Invoice", width=15, bg='white', relief="solid", borderwidth=1,
                     font=("times new roman", 10, "bold"), command=invoice).grid(row=0, column=2, padx=0,
                                                                             pady=10)

        sname__label = Label(F2, text="Supplier Name", bd=12, bg=bg_color, fg=sub_heading,
                          font=("times new roman", 15, "bold"), pady=2).grid(row=1, column=0, padx=30, pady=5,sticky=W)
        sname_txt = Entry(F2, width=20, font=("times new roman", 15, "bold"),textvariable=self.sname).grid(row=1, column=1, padx=30, pady=5,sticky=W)


        scont_label = Label(F2, text="Contact No.", bd=12, bg=bg_color, fg=sub_heading,font=("times new roman", 15, "bold"), pady=2).grid(row=2,sticky=W, column=0,padx=30,pady=5)
        scont_txt = Entry(F2, width=20, font=("times new roman", 15, "bold"),textvariable=self.contact).grid(row=2, column=1, padx=30, pady=5,sticky=W)

        data = databaseconnection.fetchproducts()
        sprod_v = []
        for row in data:
            sprod_v.append(row[0])


        sproduct_label = Label(F2, text="Select Product", bd=12, bg=bg_color, fg=sub_heading,
                          font=("times new roman", 15, "bold"), pady=2).grid(row=3, column=0, padx=30, pady=5, sticky=W)
        sproduct_txt = ttk.Combobox(F2, values=sprod_v, width=18, font=("times new roman", 15, "bold"),textvariable=self.product).grid(row=3,
                                                                                                         column=1,
                                                                                                         padx=30,
                                                                                                         pady=5,
                                                                                                         sticky=W)


        self.product.set('Select')
        qty_label = Label(F2, text="Quantity", bd=12, bg=bg_color, fg=sub_heading,
                            font=("times new roman", 15, "bold"), pady=2).grid(row=4, column=0, padx=30, pady=5,sticky=W)
        qty_txt = Entry(F2, width=20, font=("times new roman", 15, "bold"),textvariable=self.qty).grid(row=4, column=1, padx=30, pady=5,sticky=W)

        self.qty.set(" ")











        ######## ********************************************************************************************************########

        F3 = LabelFrame(self.root, bg=bg_color, fg="#F5F5F5", font=("times new roman", 15, "bold"))
        F3.place(x=450, y=610, width=600)

        ############# *********************************Buttons************************************************ ################




        add = Button(F3, text="Add", width=10,bg='white',relief="solid",borderwidth=1, font=("times new roman", 12, "bold"),command =add).grid(row=0, column=0,columnspan=4,padx=30,pady=10)

        update= Button(F3, text="Update", width=10, bg='white',relief="solid",borderwidth=1,font=("times new roman", 12, "bold"),command=update).grid(row=0, column=4,columnspan=4,padx=20,pady=10)



        delete = Button(F3, text="Delete", width=10, bg='white',relief="solid",borderwidth=1,font=("times new roman", 12, "bold"),command=delete).grid(row=0, column=8,columnspan=4,padx=20,pady=10)

        clear= Button(F3, text="Clear", width=10, bg='white',relief="solid",borderwidth=1,font=("times new roman", 12, "bold"),command=clear).grid(row=0, column=12,columnspan=4,padx=20,pady=10)


    ######################************************************Various functions***********************************#################33



# root=Tk()
# obj=Supplier_App(root)
#
# root.mainloop()