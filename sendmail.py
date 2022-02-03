
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import smtplib, ssl

def send():
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = usernameEmail.get()  # Enter your address
    receiver_email = recipientEmail.get()  # Enter receiver address
    password = usernamePassword.get()
    subject1 = subject.get()
    body1 = body.get()

 
    try:
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, ('Subject: ' + subject1 + '\n' + body1))
    except:
        messagebox.showerror('Error', "Check if both emails are correct and your password.")



root = Tk()
root.title("Login")
root.geometry("350x350")
root.minsize(350, 350)
root.maxsize(350, 350)


usernameEmail = StringVar()
recipientEmail = StringVar()
usernamePassword = StringVar()
subject = StringVar()
body = StringVar()


emailLabel = Label(root, text='Your Email:').grid(row=1, column =1,padx=10,sticky=(W))
emailEntry = ttk.Entry(root, textvariable=usernameEmail, width='20')
emailEntry.grid(row=1, column=2, padx=10, pady=10, sticky=(W))

recipientEmailLabel = Label(root, text='Recipient\'s Email:').grid(row=2, column =1,padx=10,sticky=(W))
recipientEmailEntry = ttk.Entry(root, textvariable=recipientEmail, width='20')
recipientEmailEntry.grid(row=2, column=2, padx=10, pady=10, sticky=(W))

passwordLabel = Label(root, text='Your Password:').grid(row=3, column =1,padx=10,sticky=(W))
passwordEntry = ttk.Entry(root, textvariable=usernamePassword, width='20',show='*')
passwordEntry.grid(row=3, column=2, padx=10, pady=10, sticky=(W))

messageLabel = Label(root, text='Your Message:').grid(row=4, column =1,pady=15,sticky=(W))

subjectLabel = Label(root, text='Subject:').grid(row=5, column =1,sticky=(W))
subjectEntry = ttk.Entry(root, textvariable=subject, width='20')
subjectEntry.grid(row=5, column=2, padx=10,pady=10, sticky=(W))

bodyLabel = Label(root, text='Body:').grid(row=6, column =1,sticky=(W))
bodyEntry = ttk.Entry(root, textvariable=body, width='20')
bodyEntry.grid(row=6, column=2, padx=10, sticky=(W))

loginButton = ttk.Button(root, text='Send Message',command=send)
loginButton.grid(row=7, column=2, padx=10,pady=3, sticky=(E))


root.mainloop()