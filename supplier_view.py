from tkinter import *
from tkinter import ttk,messagebox
import databaseconnection
class View_Supplier:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1500x700+0+0")
        self.root.title("Products Details")

        bg_color= "#494949"
        # root.configure(background='#c8c3cc')
        heading= "#F5F5F5"
        sub_heading= "#C8C8C8"
        title=Label(self.root,text="View Suppliers Page ",bd=12,bg=bg_color,fg=heading,font=("times new roman",30,"bold"),padx=10,pady=2).pack(fill=X)

        #########################*************************** Variables *******************************###########################

        self.searchinvoice = StringVar()



        #########################***************************Functions*******************************###########################

        def fetchdata():
            self.txtarea.delete('1.0', END)
            self.txtarea.insert(INSERT,fetch())

        def detailsdata():
            self.txtarea.delete('1.0', END)
            self.txtarea.insert(INSERT,details())

        def fetch():
            invoice = []
            name = []
            mobile = []
            qty = []
            pname = []

            data = databaseconnection.fetchdata_supplier(self.searchinvoice.get())

            for i in data:
                invoice.append(i[0])
                name.append(i[1])

                mobile.append(i[2])
                qty.append(i[3])
                pname.append(i[4])

            blist = ""

            for i in range(0, len(invoice)):
                blist += '  {:<30}  {:<30} {:<30}  {:<30} {:<20} \n'.format(invoice[i], name[i], mobile[i], qty[i],
                                                                            pname[i])
            blist += "\n"
            return blist

        def details():
            invoice = []
            name = []
            mobile = []
            qty = []
            pname = []
            data=databaseconnection.fetchdatasupplierinfo()

            for i in data:
                invoice.append(i[0])
                name.append(i[1])

                mobile.append(i[2])
                qty.append(i[3])
                pname.append(i[4])


            blist = ""

            for i in range(0, len(invoice)):

                blist += '  {:<30}  {:<30} {:<30}  {:<30} {:<20} \n'.format( invoice[i],name[i],mobile[i],qty[i],pname[i])
            blist += "\n"
            return blist

        def cleardata():
             self.searchinvoice.set(" ")
             self.txtarea.delete('1.0', END)

        #########################********************************************************************############################

        F1 = LabelFrame(self.root, text="Search Suppliers", bg=bg_color, fg="#F5F5F5",
                        font=("times new roman", 15, "bold"))
        F1.place(x=330, y=100, width=850)

        sup_label = Label(F1, text="Invoice No.", bd=12, bg=bg_color, fg=sub_heading,
                          font=("times new roman", 15, "bold"), pady=2).grid(row=0, column=0, padx=30, pady=5)
        sup_txt = Entry(F1, width=20, font=("times new roman", 15, "bold"), textvariable=self.searchinvoice).grid(row=0,
                                                                                                                  column=1,
                                                                                                                  padx=20,
                                                                                                                  pady=5)
        sup_search = Button(F1, text="Search", width=10, bg='white', relief="solid", borderwidth=1,
                            font=("times new roman", 12, "bold"), command=fetchdata).grid(row=0, column=2,
                                                                                      padx=20, pady=5)
        sup_all_search = Button(F1, text="Show All", width=10, bg='white', relief="solid", borderwidth=1,
                            font=("times new roman", 12, "bold"), command=detailsdata).grid(row=0, column=3,
                                                                                          padx=20, pady=5)
        sup_clear = Button(F1, text="Clear", width=10, bg='white', relief="solid", borderwidth=1,
                            font=("times new roman", 12, "bold"), command=cleardata).grid(row=0, column=4,
                                                                                            padx=20, pady=5)

        F4 = LabelFrame(self.root, text="View Suppliers", bg=bg_color, fg="silver", font=("times new roman", 15, "bold"))
        F4.place(x=50, y=210, width=1400, height=450)




        F5 = LabelFrame(F4, bg='white', fg="silver", font=("times new roman", 15, "bold"))
        F5.place(x=0, y=0, width=1380, height=60)
        Label(F5, text="Id", bd=12, bg='white', fg='black', font=("times new roman", 14, "bold"),padx=70,pady=2).grid(row=0, column=0,sticky=W)
        Label(F5, text="Name", bd=12, bg='white', fg='black', font=("times new roman", 14, "bold"),padx=90, pady=2).grid(row=0, column=1,sticky=W)
        Label(F5, text="Mobile", bd=12, bg='white', fg='black', font=("times new roman", 14, "bold"),padx=90, pady=2).grid(row=0, column=2,sticky=W)
        Label(F5, text="Quantity", bd=12, bg='white', fg='black', font=("times new roman", 14, "bold"), padx=60,
              pady=2).grid(row=0, column=3, sticky=W)
        Label(F5, text="Product Name", bd=12, bg='white', fg='black', font=("times new roman", 14, "bold"), padx=90,pady=2).grid(row=0, column=4, sticky=W)



        F6 = LabelFrame(F4, bg='white', fg="silver", font=("times new roman", 15, "bold"))
        F6.place(x=0, y=59, width=1380, height=500)
        scroll_y = Scrollbar(F6, orient=VERTICAL)
        scroll_x = Scrollbar(F6, orient=HORIZONTAL)
        self.txtarea = Text(F6, yscrollcommand=scroll_y.set, xscrollcommand=scroll_x)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)




# root=Tk()
# obj=View_Supplier(root)
# root.mainloop()