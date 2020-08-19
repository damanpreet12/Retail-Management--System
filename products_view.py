from tkinter import *
from tkinter import ttk,messagebox
import databaseconnection
class View_Products:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1500x700+0+0")
        self.root.title("Products Details")

        bg_color= "#494949"
        # root.configure(background='#c8c3cc')
        heading= "#F5F5F5"
        sub_heading= "#C8C8C8"
        title=Label(self.root,text="View Products Page ",bd=12,bg=bg_color,fg=heading,font=("times new roman",30,"bold"),padx=10,pady=2).pack(fill=X)

        #########################*************************** Variables *******************************###########################

        self.productid = StringVar()


        #########################***************************Functions*******************************###########################
        def fetchdata():
            self.txtarea.delete('1.0', END)
            self.txtarea.insert(INSERT,fetch())

        def detailsdata():
            self.txtarea.delete('1.0', END)
            self.txtarea.insert(INSERT,details())
        def fetch():
            catname = []
            subcatname = []
            cprice = []
            sprice = []
            pqty = []
            pname = []
            pid = []
            data = databaseconnection.fetchdata_product(self.productid.get())

            for i in data:
                pid.append(i[0])
                pname.append(i[1])
                catname.append(i[2])
                subcatname.append(i[3])
                pqty.append(i[4])
                sprice.append(i[5])
                cprice.append(i[6])
            blist = ""

            for i in range(0, len(pid)):
                blist += '  {:<11}  {:<30} {:<30}  {:<30} {:<20} {:<20} {:<20}\n'.format(pid[i], pname[i], catname[i],
                                                                                         subcatname[i], pqty[i],
                                                                                         sprice[i], cprice[i])
            blist += "\n"
            return blist

        def details():
            catname = []
            subcatname = []
            cprice = []
            sprice = []
            pqty = []
            pname = []
            pid = []
            data=databaseconnection.products_view()

            for i in data:
                pid.append(i[0])
                pname.append(i[1])
                catname.append(i[2])
                subcatname.append(i[3])
                pqty.append(i[4])
                sprice.append(i[5])
                cprice.append(i[6])
            blist = ""

            for i in range(0, len(pid)):

                blist += '  {:<11}  {:<30} {:<30}  {:<30} {:<20} {:<20} {:<20}\n'.format(pid[i],pname[i],catname[i],subcatname[i],pqty[i],sprice[i],cprice[i])
            blist += "\n"
            return blist

        def cleardata():
            self.productid.set(" ")
            self.txtarea.delete('1.0', END)



        #########################********************************************************************############################
        F1 = LabelFrame(self.root, text="Search Products", bg=bg_color, fg="#F5F5F5",
                        font=("times new roman", 15, "bold"))
        F1.place(x=330, y=100, width=850)

        sup_label = Label(F1, text="Product No.", bd=12, bg=bg_color, fg=sub_heading,
                          font=("times new roman", 15, "bold"), pady=2).grid(row=0, column=0, padx=30, pady=5)
        sup_txt = Entry(F1, width=20, font=("times new roman", 15, "bold"), textvariable=self.productid).grid(row=0,
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

        F4 = LabelFrame(self.root, text="View Products", bg=bg_color, fg="silver", font=("times new roman", 15, "bold"))
        F4.place(x=50, y=210, width=1400, height=450)

        F5 = LabelFrame(F4, bg='white', fg="silver", font=("times new roman", 15, "bold"))
        F5.place(x=0, y=0, width=1380, height=60)
        Label(F5, text="Id", bd=12, bg='white', fg='black', font=("times new roman", 14, "bold"),pady=2).grid(row=0, column=0,sticky=W)
        Label(F5, text="Product Name", bd=12, bg='white', fg='black', font=("times new roman", 14, "bold"),padx=60, pady=2).grid(row=0, column=1,sticky=W)
        Label(F5, text="Category", bd=12, bg='white', fg='black', font=("times new roman", 14, "bold"),padx=50, pady=2).grid(row=0, column=2,sticky=W)
        Label(F5, text="Sub-Category", bd=12, bg='white', fg='black', font=("times new roman", 14, "bold"),padx=100 ,pady=2).grid(row=0, column=3,sticky=W)
        Label(F5, text="Quantity", bd=12, bg='white', fg='black', font=("times new roman", 14, "bold"),padx=5, pady=2).grid(row=0, column=4,sticky=W)
        Label(F5, text="Selling Price(Rs)", bd=12, bg='white', fg='black', font=("times new roman", 14, "bold"),padx=45, pady=2).grid(row=0, column=5,sticky=W)
        Label(F5, text="Cost Price(Rs)", bd=12, bg='white', fg='black', font=("times new roman", 14, "bold"), padx=0,pady=2).grid(row=0, column=6)


        F6 = LabelFrame(F4, bg='white', fg="silver", font=("times new roman", 15, "bold"))
        F6.place(x=0, y=59, width=1380, height=500)
        scroll_y = Scrollbar(F6, orient=VERTICAL)
        scroll_x = Scrollbar(F6, orient=HORIZONTAL)
        self.txtarea = Text(F6, yscrollcommand=scroll_y.set, xscrollcommand=scroll_x)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)


# root=Tk()
# obj=View_Products(root)
# root.mainloop()