from tkinter import *
from tkinter import ttk,messagebox
import databaseconnection

class Emp_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1500x700+0+0")
        self.root.title("Employee Management")

        bg_color= "#494949"
        # root.configure(background='#c8c3cc')
        heading= "#F5F5F5"
        sub_heading= "#C8C8C8"
        title=Label(self.root,text=" Employee Management ",bd=12,bg=bg_color,fg=heading,font=("times new roman",30,"bold"),padx=10,pady=2).pack(fill=X)

        ##########************************************Variables*******************************************##############


        self.empsearch=IntVar()
        self.empid=IntVar()
        self.empname=StringVar()
        self.empemail=StringVar()
        self.emppass=StringVar()
        self.empcontact=IntVar()
        self.empdesign=StringVar()
        self.empgender=StringVar()
        self.empaddress=StringVar()
        self.empproof=StringVar()
        self.empproofid=StringVar()

        ##########************************************Functions*******************************************##############

        def add():
            messagebox.showinfo("Employee Management", "Successfully added")
            databaseconnection.insert_emp_data(self.empid.get(), self.empname.get(), self.empemail.get(),
                                               self.emppass.get(), self.empcontact.get(), self.empdesign.get(),
                                               self.empgender.get(), self.empaddress.get(), self.empproof.get(),
                                               self.empproofid.get())

        def update():
            messagebox.showinfo("Employee Management", "Successfully updated")
            databaseconnection.update_emp_data(self.empid.get(), self.empname.get(), self.empemail.get(),
                                               self.emppass.get(), self.empcontact.get(), self.empdesign.get(),
                                               self.empgender.get(), self.empaddress.get(), self.empproof.get(),
                                               self.empproofid.get())

        def fetch():
            data = databaseconnection.fetchdata_emp(self.empsearch.get())
            for row in data:
                self.empid.set(row[0])
                self.empname.set(row[1])
                self.empemail.set(row[2])
                self.emppass.set(row[3])
                self.empcontact.set(row[4])
                self.empdesign.set(row[5])
                self.empgender.set(row[6])
                self.empaddress.set(row[7])
                self.empproof.set(row[8])
                self.empproofid.set(row[9])

        def delete():
            messagebox.showinfo("Supplier Management", "Successfully deleted")
            databaseconnection.delete_data_emp("employeeDetails", self.empsearch.get())
            self.empid.set(" ")
            self.empname.set(" ")
            self.empemail.set(" ")
            self.emppass.set(" ")
            self.empcontact.set(" ")

            self.empaddress.set(" ")

            self.empproofid.set(" ")
            self.empsearch.set(" ")

        def clear():
            self.empid.set(" ")
            self.empname.set(" ")
            self.empemail.set(" ")
            self.emppass.set(" ")
            self.empcontact.set(" ")

            self.empaddress.set(" ")

            self.empproofid.set(" ")
            self.empsearch.set(" ")

        ######## ****************************************Search Employees***************************************########

        F1 = LabelFrame(self.root, text="Search Employees", bg=bg_color, fg="#F5F5F5",
                        font=("times new roman", 15, "bold"))
        F1.place(x=450, y=100,width=600)

        emp_label = Label(F1, text=" Employee Id", bd=12, bg=bg_color, fg=sub_heading,
                           font=("times new roman", 15, "bold"), pady=2).grid(row=0, column=0, padx=30, pady=5)
        emp_txt = Entry(F1, width=20, font=("times new roman", 15, "bold"),textvariable=self.empsearch).grid(row=0, column=1, padx=20, pady=5)
        emp_search = Button(F1, text="Search", width=10, font=("times new roman", 12, "bold"),bg='white',relief="solid",borderwidth=1,command=fetch).grid(row=0, column=2,
                                                                                                padx=20, pady=5)

        self.empsearch.set(" ")
        ######## **************************************** Employees Details***************************************########



        F2=LabelFrame(self.root,bg=bg_color,fg="#F5F5F5",font=("times new roman",15,"bold"))
        F2.place(x=250,y=200,width=1000)


        ############# **************************************zero row**********************************************###########


        bill_label = Label(F2, text="Employee Id", bd=12, bg=bg_color, fg=sub_heading,
                           font=("times new roman", 15, "bold"), pady=2).grid(row=0, column=0, padx=30, pady=5,sticky=W)
        bill_txt = Entry(F2, width=20, font=("times new roman", 15, "bold"),textvariable=self.empid).grid(row=0, column=1, padx=20, pady=5,sticky=W)


        self.empid.set(" ")

        id__label = Label(F2, text="Email Id", bd=12, bg=bg_color, fg=sub_heading,
                          font=("times new roman", 15, "bold"), pady=2).grid(row=0, column=3, padx=30, pady=5,sticky=W)
        id_txt = Entry(F2, width=20, font=("times new roman", 15, "bold"),textvariable=self.empemail).grid(row=0, column=4, padx=20, pady=5,sticky=W)


        ############************************************** first row **************************************************##########



        emp_name_label = Label(F2, text="Employee Name", bd=12, bg=bg_color, fg=sub_heading,font=("times new roman", 15, "bold"), pady=2).grid(row=1,sticky=W, column=0,padx=30,pady=5)
        emp_name_txt = Entry(F2, width=20, font=("times new roman", 15, "bold"),textvariable=self.empname).grid(row=1, column=1, padx=20, pady=5,sticky=W)
        passw_label = Label(F2, text="Password", bd=12, bg=bg_color, fg=sub_heading,
                               font=("times new roman", 15, "bold"), pady=2).grid(row=1, column=3, padx=30, pady=5,sticky=W)
        passw_name_txt = Entry(F2, width=20, font=("times new roman", 15, "bold"),textvariable=self.emppass).grid(row=1, column=4, padx=20, pady=5,sticky=W)




        ############*************************************** second row ************************************************##########



        phone_label = Label(F2, text="Contact Number", bd=12, bg=bg_color, fg=sub_heading,
                            font=("times new roman", 15, "bold"), pady=2).grid(row=2, column=0, padx=30, pady=5,sticky=W)
        phone_txt = Entry(F2, width=20, font=("times new roman", 15, "bold"),textvariable=self.empcontact).grid(row=2, column=1, padx=20, pady=5,sticky=W)

        self.empcontact.set(" ")

        design_v = ['Employee',
                     'Admin',

                     ]

        cat_label = Label(F2, text="Select Designation", bd=12, bg=bg_color, fg=sub_heading,
                          font=("times new roman", 15, "bold"), pady=2).grid(row=2, column=3, padx=30, pady=5,sticky=W)
        cat_txt = ttk.Combobox(F2, values=design_v, width=18, font=("times new roman", 15, "bold"),textvariable=self.empdesign).grid(row=2,
                                                                                                          column=4,
                                                                                                          padx=20,
                                                                                                          pady=5,sticky=W)
        self.empdesign.set('Choose')
        ############**************************************************** third row *************************************##########

        gender_v = [' Male',
                    ' Female',

                    ]

        cat_label = Label(F2, text="Select Gender", bd=12, bg=bg_color, fg=sub_heading,
                          font=("times new roman", 15, "bold"), pady=2).grid(row=3, column=0, padx=30, pady=5,sticky=W)
        cat_txt = ttk.Combobox(F2, values=gender_v, width=18, font=("times new roman", 15, "bold"),textvariable=self.empgender).grid(row=3,
                                                                                                         column=1,
                                                                                                         padx=20,
                                                                                                         pady=5,sticky=W)
        self.empgender.set('Choose')
        ############*************************************************** fourth row********************************** ##########

        address_label = Label(F2, text="Address", bd=12, bg=bg_color, fg=sub_heading,
                            font=("times new roman", 15, "bold"), pady=2).grid(row=4, column=0, padx=30, pady=5,sticky=W)
        address_txt = Entry(F2, width=20, font=("times new roman", 15, "bold"),textvariable=self.empaddress).grid(row=4, column=1, padx=20, pady=5,sticky=W)


        ############************************************************ fifth row ***************************************##########


        proof_v = [' Driving License',
                    'Adhar Card',
                   'Voter Card',
                   'Pan Card',

                    ]

        proof_label = Label(F2, text="ID Proof", bd=12, bg=bg_color, fg=sub_heading,
                          font=("times new roman", 15, "bold"), pady=2).grid(row=5, column=0, padx=30, pady=5,sticky=W)
        proof_txt = ttk.Combobox(F2, values=proof_v, width=18, font=("times new roman", 15, "bold"),textvariable=self.empproof).grid(row=5,
                                                                                                         column=1,
                                                                                                         padx=20,
                                                                                                         pady=5,sticky=W)
        self.empproof.set('Choose')
        ############************************************************* sixth row ****************************************##########

        phone_label = Label(F2, text="Proof Number", bd=12, bg=bg_color, fg=sub_heading,
                            font=("times new roman", 15, "bold"), pady=2).grid(row=6, column=0, padx=30, pady=5,sticky=W)
        phone_txt = Entry(F2, width=20, font=("times new roman", 15, "bold"),textvariable=self.empproofid).grid(row=6, column=1, padx=20, pady=5,sticky=W)


        ######## ****************************************************************************************************########

        F3 = LabelFrame(self.root, bg=bg_color, fg="#F5F5F5", font=("times new roman", 15, "bold"))
        F3.place(x=250, y=630, width=1000)

        #############************************************** Buttons************************************* ################3


        add = Button(F3, text="Add", width=10, font=("times new roman", 12, "bold"),bg='white',relief="solid",borderwidth=1,command=add).grid(row=0, column=0,columnspan=4,padx=80,pady=10)

        update= Button(F3, text="Update", width=10, font=("times new roman", 12, "bold"),bg='white',relief="solid",borderwidth=1,command=update).grid(row=0, column=4,columnspan=4,padx=80,pady=10)

        delete= Button(F3, text="Delete", width=10, font=("times new roman", 12, "bold"),bg='white',relief="solid",borderwidth=1,command=delete).grid(row=0, column=8,columnspan=4,padx=80,pady=10)

        clear= Button(F3, text="Clear", width=10, font=("times new roman", 12, "bold"),bg='white',relief="solid",borderwidth=1,command=clear).grid(row=0, column=12,columnspan=4,padx=80,pady=10)


    ###########################***************************Various Functions*******************************#######################33



# root=Tk()
# obj=Emp_App(root)
# root.mainloop()