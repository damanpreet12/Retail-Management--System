import os
import smtplib
from tkinter import *
from tkinter import ttk,messagebox
from email.message import EmailMessage
import os
def send_bill(path,title,email):
    msg = EmailMessage()
    msg['Subject'] = 'Your bill '
    msg['From'] ='vermashanaya1234@gmail.com'
    msg['To'] = email  # receiver email
    billtitle = title + '.txt'
    msg.set_content('This is your Total bill')
    with open(os.path.join(path, billtitle), "rb") as f:
        file_data = f.read()
        file_name = billtitle
    msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)
    qsend = messagebox.askyesno("Billing System", "Do you want to send the bill?")
    if qsend > 0:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login('vermashanaya1234@gmail.com', 'shanaya#*1234')
            smtp.send_message(msg)
        qsmsg = messagebox.showinfo("Information", "Bill send successfully")
    else:
        qnmsg = messagebox.showinfo("Information", "Bill not send")

