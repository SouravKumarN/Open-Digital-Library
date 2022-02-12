import smtplib, ssl
from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import mysql.connector


conn = mysql.connector.connect(host="localhost",user="root",password="mypass")
cur = conn.cursor()  
cur.execute("CREATE DATABASE IF NOT EXISTS db") 
conn.close

def sendmail(name, recev):
	#cur.execute("select title from "+bookTable+" where bid = '"+str(bid)+"'")
	port = 587  # For starttls
	smtp_server = "smtp.gmail.com"
	sender_email = "techaround18@gmail.com"
	receiver_email = recev #"souravkumarnagal@gmail.com"
	password = "Sknmaa08"#input("Type your password and press enter:")
	subject="Registration Successful"
	text="Dear "+name+",\nYou have been successfully registered with the Open Digital Library.\n\nOpen Library Admin,\nRegards"
	message = 'Subject: {}\n\n{}'.format(subject, text)

	context = ssl.create_default_context()
	with smtplib.SMTP(smtp_server, port) as server:
	    server.ehlo()  # Can be omitted
	    server.starttls(context=context)
	    server.ehlo()  # Can be omitted
	    server.login(sender_email, password)
	    server.sendmail(sender_email, receiver_email, message)

def register():
    
    name = bookInfo1.get()
    phnum = bookInfo2.get()
    uid = bookInfo3.get()
    passw = bookInfo4.get()
    cred = "credentials"
    cur.execute("CREATE TABLE IF NOT EXISTS "+cred+" (name VARCHAR(255), phnum VARCHAR(255), uid VARCHAR(255) ,passw VARCHAR(255),PRIMARY KEY (uid))")
    con.commit()
    insertuser = "insert into "+cred+" values('"+name+"','"+phnum+"','"+uid+"','"+passw+"')"
    #sendmail(name,uid)    
    try:
        cur.execute(insertuser)
        con.commit()
        messagebox.showinfo('Success',"User registered successfully")
        sendmail(name,uid)    
    except:
        messagebox.showinfo("Error","Can't add data into Database")


    root.destroy()
    
def registerd(): 
    
    global bookInfo1,bookInfo2,bookInfo3,bookInfo4,Canvas1,con,cur,bookTable,root
    
    root = Tk()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("480x550")

    # Add your own database name and password here to reflect in the code
    mypass = "mypass"
    mydatabase="db"

    con = mysql.connector.connect(host="localhost",user="root",password=mypass,database=mydatabase)
    cur = con.cursor()
    
    # Enter Table Names here
    bookTable = "books" # Book Table

    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="#292929")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="#ededed",bd=2)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="Register", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.08,rely=0.3,relwidth=0.84,relheight=0.55)
        
    # Book ID
    lb1 = Label(labelFrame,text="Name : ", bg='black', fg='white')
    lb1.place(relx=0.035,rely=0.12, relheight=0.08)
        
    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3,rely=0.12, relwidth=0.62, relheight=0.08)
        
    # Title
    lb2 = Label(labelFrame,text="Ph. Number : ", bg='black', fg='white')
    lb2.place(relx=0.035,rely=0.32, relheight=0.08)
        
    bookInfo2 = Entry(labelFrame)
    bookInfo2.place(relx=0.3,rely=0.32, relwidth=0.62, relheight=0.08)
        
    # Book Author
    lb3 = Label(labelFrame,text="UserID(Email) : ", bg='black', fg='white')
    lb3.place(relx=0.035,rely=0.52, relheight=0.08)
        
    bookInfo3 = Entry(labelFrame)
    bookInfo3.place(relx=0.3,rely=0.52, relwidth=0.62, relheight=0.08)
        
    # Book Status
    lb4 = Label(labelFrame,text="Password : ", bg='black', fg='white')
    lb4.place(relx=0.035,rely=0.72, relheight=0.08)
        
    bookInfo4 = Entry(labelFrame)
    bookInfo4.place(relx=0.3,rely=0.72, relwidth=0.62, relheight=0.08)
        
    #Submit Button
    SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black',command=register)
    SubmitBtn.place(relx=0.41,rely=0.9, relwidth=0.18,relheight=0.06)
    

    
    root.mainloop()
