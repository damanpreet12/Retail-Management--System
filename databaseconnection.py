import mysql.connector
from tkinter import *


def db_connection():

    connection=mysql.connector.connect(host="127.0.0.1",
                                       user="root",
                                       password="insidara1234@",
                                       database="retaildb2"
                                       )
    print(connection)

    sql=connection.cursor()

    #############**********************create tables***********************#############################

    connection.commit()

db_connection()


    ##################************************Insert Into table**********************##########################


def supplier_table(SupplierDetails):
    connection = mysql.connector.connect(host="127.0.0.1",
                                         user="root",
                                         password="insidara1234@",
                                         database="retaildb2"
                                         )
    print(connection)
    sql = connection.cursor()
    sql.execute(
        "CREATE TABLE IF NOT EXISTS  SupplierDetails(invoice_numb_id varchar(30) primary key,supplier_name varchar(30),mobile varchar(30),"
        "quantity int,product_name varchar(30))")
    connection.commit()

supplier_table("SupplierDetails")

def emp_table():
    connection = mysql.connector.connect(host="127.0.0.1",
                                         user="root",
                                         password="insidara1234@",
                                         database="retaildb2"
                                         )
    print(connection)
    sql = connection.cursor()
    sql.execute("CREATE TABLE IF NOT EXISTS  EmployeeDetails (id int primary key,name varchar(30),email varchar(30),"
                "password varchar(30),mobile varchar(30) ,designation varchar(30),gender varchar(30),address varchar(30),proof varchar(30),proofnumb varchar(30))")

    connection.commit()

emp_table()

def product_table():
    connection = mysql.connector.connect(host="127.0.0.1",
                                         user="root",
                                         password="insidara1234@",
                                         database="retaildb2"
                                         )
    print(connection)
    sql = connection.cursor()
    sql.execute(
        "CREATE TABLE IF NOT EXISTS  ProductDetails (product_id int primary key AUTO_INCREMENT ,product_name varchar(30),cat_name varchar(30),"
        "subcat_name varchar(30),quantity int ,selling_price varchar(30),cost_price varchar(30))")

    connection.commit()


product_table()

def category_table():
    connection = mysql.connector.connect(host="127.0.0.1",
                                         user="root",
                                         password="insidara1234@",
                                         database="retaildb2"
                                         )
    print(connection)
    sql = connection.cursor()
    sql.execute(
        "CREATE TABLE IF NOT EXISTS  CategoryDetails(cat_id int PRIMARY KEY AUTO_INCREMENT,cat_name varchar(30))")
    connection.commit()

category_table()



def sub_category_table():
    connection = mysql.connector.connect(host="127.0.0.1",
                                         user="root",
                                         password="insidara1234@",
                                         database="retaildb2"
                                         )
    print(connection)
    sql = connection.cursor()
    sql.execute(
        "CREATE TABLE IF NOT EXISTS  SubCategoryDetails(subcat_id int primary key AUTO_INCREMENT,subcat_name varchar(30),categoryname varchar(30))")
    connection.commit()

sub_category_table()


def cust_products_table():
    connection = mysql.connector.connect(host="127.0.0.1",
                                         user="root",
                                         password="insidara1234@",
                                         database="retaildb2"
                                         )
    print(connection)
    sql = connection.cursor()
    sql.execute(
        "CREATE TABLE IF NOT EXISTS  CustProductsDetails(id int primary key AUTO_INCREMENT ,product_name varchar(30),cat_name varchar(30),"
        "subcat_name varchar(30),quantity int ,cust_id varchar(30),paid varchar(30),bill_number varchar(30))")
    connection.commit()

cust_products_table()

def cust_bill_table():
    connection = mysql.connector.connect(host="127.0.0.1",
                                         user="root",
                                         password="insidara1234@",
                                         database="retaildb2"
                                         )
    print(connection)
    sql = connection.cursor()
    sql.execute(
        "CREATE TABLE IF NOT EXISTS  CustBillDetails(Bill_id varchar(30) primary key ,cust_id varchar(30),customer_name varchar(30),email varchar(30),mobile varchar(30),total_bill varchar(30),date varchar(30))")
    connection.commit()

cust_bill_table()

def cust_details():
    connection = mysql.connector.connect(host="127.0.0.1",
                                         user="root",
                                         password="insidara1234@",
                                         database="retaildb2"
                                         )
    print(connection)
    sql = connection.cursor()
    sql.execute(
        "CREATE TABLE IF NOT EXISTS  CustomerDetails(cust_id int primary key AUTO_INCREMENT,customer_name varchar(30),email varchar(30),mobile varchar(30))")
    connection.commit()

cust_details()

def insert_emp_data(id=' ', name= '', email=' ', password=' ', mobile=' ', designation=' ', gender=' ', address=' ', proof=' ', proofnumb=' '):



    connection = mysql.connector.connect(host="127.0.0.1",
                                         user="root",
                                         password="insidara1234@",
                                         database="retaildb2"
                                         )
    print(connection)
    sql = connection.cursor()
    query = "INSERT INTO EmployeeDetails VALUES (%d,'%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (id, name, email, password, mobile, designation,
                                                                                                    gender, address, proof, proofnumb)

    sql.execute(query)
    connection.commit()

def insert_cat_data(cat_name= ' '):



    connection = mysql.connector.connect(host="127.0.0.1",
                                         user="root",
                                         password="insidara1234@",
                                         database="retaildb2"
                                         )
    print(connection)
    sql = connection.cursor()
    query = "INSERT INTO CategoryDetails(cat_name) VALUES ('%s')" %(cat_name)

    sql.execute(query)
    connection.commit()

def insert_subcat_data(subcat_name= ' ',categoryname=' '):



    connection = mysql.connector.connect(host="127.0.0.1",
                                         user="root",
                                         password="insidara1234@",
                                         database="retaildb2"
                                         )
    print(connection)
    sql = connection.cursor()
    query = "INSERT INTO SubCategoryDetails(subcat_name,categoryname) VALUES ('%s','%s')" % (subcat_name,categoryname)

    sql.execute(query)
    connection.commit()



def insert_prod_data(product_name=' ', cat_name=' ', subcat_name=' ', quantity=' ', selling_price=' ',cost_price=' '):

    connection = mysql.connector.connect(host="127.0.0.1",
                                         user="root",
                                         password="insidara1234@",
                                         database="retaildb2"
                                         )
    print(connection)
    sql = connection.cursor()
    query = "INSERT INTO ProductDetails(product_name, cat_name, subcat_name, quantity,selling_price, cost_price) VALUES ('%s','%s','%s',%d,'%s','%s')" % (product_name, cat_name, subcat_name, quantity,selling_price, cost_price)
    sql.execute(query)
    connection.commit()




def insert_cust_prod(product_name=' ', cat_name=' ', subcat_name=' ', quantity=' ', cust_id=' ',paid=' '):

    connection = mysql.connector.connect(host="127.0.0.1",
                                         user="root",
                                         password="insidara1234@",
                                         database="retaildb2"
                                         )
    print(connection)
    sql = connection.cursor()
    query = "INSERT INTO CustProductsDetails(product_name, cat_name, subcat_name, quantity,cust_id,paid) VALUES ('%s','%s','%s',%d,'%s','%s')" % (product_name, cat_name, subcat_name, quantity,cust_id,paid)
    sql.execute(query)
    connection.commit()


def insert_cust_details(Bill_id=' ' ,cust_id=' ',customer_name=' ', email=' ', mobile=' ',  total_bill=' ',date=' '):

    connection = mysql.connector.connect(host="127.0.0.1",
                                         user="root",
                                         password="insidara1234@",
                                         database="retaildb2"
                                         )
    print(connection)
    sql = connection.cursor()
    query = "INSERT INTO CustBillDetails(Bill_id,cust_id,customer_name, email,mobile,total_bill,date) VALUES ('%s','%s','%s','%s','%s','%s','%s')" % (Bill_id,cust_id,customer_name, email,mobile,total_bill,date)
    sql.execute(query)
    connection.commit()
def insert_customer_details(customer_name=' ', email=' ', mobile=' '):

    connection = mysql.connector.connect(host="127.0.0.1",
                                         user="root",
                                         password="insidara1234@",
                                         database="retaildb2"
                                         )
    print(connection)
    sql = connection.cursor()
    query = "INSERT INTO CustomerDetails(customer_name, email,mobile) VALUES ('%s','%s','%s')" % (customer_name, email,mobile)
    sql.execute(query)
    connection.commit()





def insert_supp_data(invoice=' ', sname=' ', contact=' ', qty=' ', product=' '):

    connection = mysql.connector.connect(host="127.0.0.1",
                                         user="root",
                                         password="insidara1234@",
                                         database="retaildb2"
                                         )
    print(connection)
    sql = connection.cursor()


    query = "INSERT INTO SupplierDetails VALUES ('%s','%s','%s',%d,'%s')" % (invoice, sname, contact, qty, product)
    sql.execute(query)
    connection.commit()





###################***********************fetch data********************************########################




def fetchcustomer_id(email):


    connection = mysql.connector.connect(host="127.0.0.1",
                                         user="root",
                                         password="insidara1234@",
                                         database="retaildb2"
                                         )
    print(connection)
    sql = connection.cursor()
    sql.execute("SELECT cust_id FROM CustomerDetails where email='%s'" %(email))
    data = sql.fetchall()

    return data

def fetchcatoptions(table_name):


    connection = mysql.connector.connect(host="127.0.0.1",
                                         user="root",
                                         password="insidara1234@",
                                         database="retaildb2"
                                         )
    print(connection)
    sql = connection.cursor()
    sql.execute("SELECT cat_name FROM "+ table_name)
    data = sql.fetchall()

    return data

def fetchsubcatoptions():


    connection = mysql.connector.connect(host="127.0.0.1",
                                         user="root",
                                         password="insidara1234@",
                                         database="retaildb2"
                                         )
    print(connection)
    sql = connection.cursor()
    sql.execute("SELECT subcat_name FROM subcategoryDetails")
    data = sql.fetchall()

    return data

def fetchproducts():


    connection = mysql.connector.connect(host="127.0.0.1",
                                         user="root",
                                         password="insidara1234@",
                                         database="retaildb2"
                                         )
    print(connection)
    sql = connection.cursor()
    sql.execute("SELECT product_name FROM productDetails")
    data = sql.fetchall()

    return data
def products_view():


    connection = mysql.connector.connect(host="127.0.0.1",
                                         user="root",
                                         password="insidara1234@",
                                         database="retaildb2"
                                         )
    print(connection)
    sql = connection.cursor()
    sql.execute("SELECT * FROM productDetails")
    data = sql.fetchall()

    return data
def fetchdata_supplier(id):


    connection = mysql.connector.connect(host="127.0.0.1",
                                         user="root",
                                         password="insidara1234@",
                                         database="retaildb2"
                                         )
    print(connection)
    sql = connection.cursor()
    sql.execute("SELECT * FROM supplierDetails where invoice_numb_id='%s'" %(id) )
    data = sql.fetchall()

    return data
def fetchdatasupplierinfo():


    connection = mysql.connector.connect(host="127.0.0.1",
                                         user="root",
                                         password="insidara1234@",
                                         database="retaildb2"
                                         )
    print(connection)
    sql = connection.cursor()
    sql.execute("SELECT * FROM supplierDetails")
    data = sql.fetchall()

    return data



def fetchdata_product(id):


    connection = mysql.connector.connect(host="127.0.0.1",
                                         user="root",
                                         password="insidara1234@",
                                         database="retaildb2"
                                         )
    print(connection)
    sql = connection.cursor()
    sql.execute("SELECT * FROM productDetails where product_id=" + str(id))
    data = sql.fetchall()
    return data




def fetchdata_product_cost(productname):


    connection = mysql.connector.connect(host="127.0.0.1",
                                         user="root",
                                         password="insidara1234@",
                                         database="retaildb2"
                                         )
    print(connection)
    sql = connection.cursor()
    sql.execute("SELECT selling_price FROM productDetails where product_name='%s' "%(productname))
    data = sql.fetchall()
    return data




def fetch_cust_products(id):


    connection = mysql.connector.connect(host="127.0.0.1",
                                         user="root",
                                         password="insidara1234@",
                                         database="retaildb2"
                                         )
    print(connection)
    sql = connection.cursor()
    sql.execute("SELECT product_name,quantity FROM custProductsDetails where cust_id='%s' and paid='0' " %(id))
    data = sql.fetchall()
    return data

def fetch_cust_products_details(id,billnumb):


    connection = mysql.connector.connect(host="127.0.0.1",
                                         user="root",
                                         password="insidara1234@",
                                         database="retaildb2"
                                         )
    print(connection)
    sql = connection.cursor()
    sql.execute("SELECT product_name,quantity FROM custProductsDetails where cust_id='%s' and bill_number='%s' " %(id,billnumb))
    data = sql.fetchall()
    return data
def fetchdata_emp(id):

    
    connection = mysql.connector.connect(host="127.0.0.1",
                                         user="root",
                                         password="insidara1234@",
                                         database="retaildb2"
                                         )
    print(connection)
    sql = connection.cursor()
    sql.execute("SELECT * FROM employeeDetails where id=" + str(id) )
    data = sql.fetchall()
    return data





def fetchdata_emp_details():
    connection = mysql.connector.connect(host="127.0.0.1",
                                         user="root",
                                         password="insidara1234@",
                                         database="retaildb2"
                                         )
    print(connection)
    sql = connection.cursor()
    sql.execute("SELECT * FROM employeeDetails")
    data = sql.fetchall()
    return data


def fetchdata_emp_login():
    connection = mysql.connector.connect(host="127.0.0.1",
                                         user="root",
                                         password="insidara1234@",
                                         database="retaildb2"
                                         )
    print(connection)
    sql = connection.cursor()
    sql.execute("SELECT name,designation,password,email FROM employeeDetails")
    data = sql.fetchall()
    return data

def fetchdata_cust_details(id):
    connection = mysql.connector.connect(host="127.0.0.1",
                                         user="root",
                                         password="insidara1234@",
                                         database="retaildb2"
                                         )
    print(connection)
    sql = connection.cursor()
    sql.execute("SELECT cust_id,customer_name,email,mobile,total_bill,date FROM CustBillDetails where Bill_id= '%s'" %(id))
    data = sql.fetchall()
    return data



def fetchdata_customer_details(id):
    connection = mysql.connector.connect(host="127.0.0.1",
                                         user="root",
                                         password="insidara1234@",
                                         database="retaildb2"
                                         )
    print(connection)
    sql = connection.cursor()
    sql.execute("SELECT customer_name,email,mobile FROM CustomerDetails where cust_id= %d" %(id))
    data = sql.fetchall()
    return data

def fetchdata_cat(id):
    connection = mysql.connector.connect(host="127.0.0.1",
                                         user="root",
                                         password="insidara1234@",
                                         database="retaildb2"
                                         )
    print(connection)
    sql = connection.cursor()
    sql.execute("SELECT cat_name FROM categoryDetails where cat_id= " + str(id) )
    data = sql.fetchall()
    return data


def fetchdata_subcat(id):
    connection = mysql.connector.connect(host="127.0.0.1",
                                         user="root",
                                         password="insidara1234@",
                                         database="retaildb2"
                                         )
    print(connection)
    sql = connection.cursor()
    sql.execute("SELECT subcat_name,categoryname FROM SubCategoryDetails where subcat_id=" + str(id))
    data = sql.fetchall()
    return data






#####################**********************delete*****************************########################





def delete_data_supp(supplier_table, id):
    connection = mysql.connector.connect(host="127.0.0.1",
                                         user="root",
                                         password="insidara1234@",
                                         database="retaildb2"
                                         )
    print(connection)
    sql = connection.cursor()
    sql.execute("DELETE  FROM supplierDetails where invoice_numb_id = '%s' " % (id))
    connection.commit()

def delete_data_emp(emp_table, id):
    connection = mysql.connector.connect(host="127.0.0.1",
                                         user="root",
                                         password="insidara1234@",
                                         database="retaildb2"
                                         )
    print(connection)
    sql = connection.cursor()
    sql.execute("DELETE  FROM employeeDetails where id = %d " % (id))
    connection.commit()

def delete_data_prod(id):
    connection = mysql.connector.connect(host="127.0.0.1",
                                         user="root",
                                         password="insidara1234@",
                                         database="retaildb2"
                                         )
    print(connection)
    sql = connection.cursor()
    sql.execute("DELETE  FROM productDetails where product_id = %d " % (id))
    connection.commit()

def delete_data_cat(category_table, id):
    connection = mysql.connector.connect(host="127.0.0.1",
                                         user="root",
                                         password="insidara1234@",
                                         database="retaildb2"
                                         )
    print(connection)
    sql = connection.cursor()
    sql.execute("DELETE  FROM categoryDetails where cat_id = %d " % (id))
    connection.commit()
def delete_data_subcat(sub_category_table, id):
    connection = mysql.connector.connect(host="127.0.0.1",
                                         user="root",
                                         password="insidara1234@",
                                         database="retaildb2"
                                         )
    print(connection)
    sql = connection.cursor()
    sql.execute("DELETE  FROM subCategoryDetails where subcat_id = %d " % (id))
    connection.commit()




#########***********************create database***********************########################

# def create_database(db_name):
#     query = "create database if not exists " + db_name
#     # print(query)
#     sql.execute(query)
#     print("Database Created")

# create_database("Retaildb")



#####################****************************update *****************################################



def update_custproddetails(paid=' ',id=' ',bnumb=' '):


    connection = mysql.connector.connect(host="127.0.0.1",
                                         user="root",
                                         password="insidara1234@",
                                         database="retaildb2"
                                         )
    print(connection)
    sql = connection.cursor()
    query="UPDATE CustProductsDetails SET paid='%s',bill_number='%s' WHERE cust_id='%s'" %(paid,bnumb,id)
    sql.execute(query)
    connection.commit()

def update_emp_data(id=' ',name=' ',email=' ',password=' ' ,mobile=' ',designation=' ',gender=' ',address=' ',proof=' ',proofnumb=' '):


    connection = mysql.connector.connect(host="127.0.0.1",
                                         user="root",
                                         password="insidara1234@",
                                         database="retaildb2"
                                         )
    print(connection)
    sql = connection.cursor()
    query="UPDATE EmployeeDetails SET name='%s',email='%s',password='%s' ,mobile=%d,designation='%s',gender='%s',address='%s',proof='%s',proofnumb='%s' " \
          "WHERE id=%d" %(name,email,password ,mobile,designation,gender,address,proof,proofnumb,id)
    sql.execute(query)
    connection.commit()

def update_prod_data(product_name=' ',cat_name=' ' ,subcat_name=' ' ,quantity=' ' ,selling_price=' ',cost_price=' ',product_id=' '):

    connection = mysql.connector.connect(host="127.0.0.1",
                                         user="root",
                                         password="insidara1234@",
                                         database="retaildb2"
                                         )
    print(connection)
    sql = connection.cursor()
    query="UPDATE ProductDetails SET product_name='%s',cat_name='%s',subcat_name='%s',quantity= %d,selling_price='%s',cost_price='%s' " \
          " WHERE product_id= %d" %(product_name,cat_name ,subcat_name,quantity,selling_price,cost_price,product_id)
    sql.execute(query)
    connection.commit()


def update_supp_data(supplier_name=' ',mobile=' ',quantity=' ',product_name=' ',invoice_numb=' '):

    connection = mysql.connector.connect(host="127.0.0.1",
                                         user="root",
                                         password="insidara1234@",
                                         database="retaildb2"
                                         )
    print(connection)
    sql = connection.cursor()
    query="UPDATE SupplierDetails SET supplier_name='%s',mobile='%s',quantity=%d,product_name='%s' WHERE invoice_numb_id='%s' " %(supplier_name,mobile,quantity,product_name,invoice_numb)
    sql.execute(query)
    connection.commit()


def update_cat_data(cat_name=' ',cat_id=' '):

    connection = mysql.connector.connect(host="127.0.0.1",
                                         user="root",
                                         password="insidara1234@",
                                         database="retaildb2"
                                         )
    print(connection)
    sql = connection.cursor()
    query="UPDATE CategoryDetails SET cat_name='%s' WHERE cat_id= %d" %(cat_name, cat_id)
    sql.execute(query)
    connection.commit()

def update_subcat_data(subcatname=' ',catname=' ',cat_id=' '):

    connection = mysql.connector.connect(host="127.0.0.1",
                                         user="root",
                                         password="insidara1234@",
                                         database="retaildb2"
                                         )
    print(connection)
    sql = connection.cursor()
    query="UPDATE subCategoryDetails SET subcat_name='%s',categoryname='%s' WHERE subcat_id=%d" %(subcatname,catname,cat_id)
    sql.execute(query)
    connection.commit()

def update_emp_details(id,password=' '):


    connection = mysql.connector.connect(host="127.0.0.1",
                                         user="root",
                                         password="insidara1234@",
                                         database="retaildb2"
                                         )
    print(connection)
    sql = connection.cursor()
    query="UPDATE EmployeeDetails SET password='%s' " \
          "WHERE email='%s'" %(password,id)
    sql.execute(query)
    connection.commit()















