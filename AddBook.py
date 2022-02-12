from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
from tkinter import messagebox
import mysql.connector


conn = mysql.connector.connect(host="localhost",user="root",password="mypass")
cur = conn.cursor()  
cur.execute("CREATE DATABASE IF NOT EXISTS db") 
conn.close

def bookRegister():
    
	bid = bookInfo1.get()
	title = bookInfo2.get()
	author = bookInfo3.get()
	#status = bookInfo4.get()
	copies = bookInfo5.get()
	section = bookInfo6.get()
	#status = status.lower()

	insertBooks = "insert into "+bookTable+" values('"+bid+"','"+title+"','"+author+"','"+copies+"','"+section+"')"
	try:
		cur.execute("CREATE TABLE IF NOT EXISTS books(bid INT,title VARCHAR(255),author VARCHAR(255),copies INT,section VARCHAR(255), PRIMARY KEY(bid))")
		cur.execute(insertBooks)
		con.commit()
		messagebox.showinfo('Success',"Book added successfully")
		cur.execute("insert into history values('Book with id - ','"+bid+"','has been successfully added.')")
		con.commit()
	except:
		messagebox.showinfo("Error","Can't add data into Database")
    
	print(bid)
	print(title)
	print(author)
	print(copies)
	root.destroy()
    
def addBook(): 
    
    global bookInfo1,bookInfo2,bookInfo3,bookInfo4,bookInfo5,bookInfo6,Canvas1,con,cur,bookTable,root
    
    root = Tk()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("600x500")

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
        
    headingFrame1 = Frame(root,bg="#ededed",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="Add Books", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.45)
        
    # Book ID
    lb1 = Label(labelFrame,text="Book ID : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.12, relheight=0.08)
        
    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.37,rely=0.12, relwidth=0.55)
        
    # Title
    lb2 = Label(labelFrame,text="Title : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.32, relheight=0.08)
        
    bookInfo2 = Entry(labelFrame)
    bookInfo2.place(relx=0.37,rely=0.32, relwidth=0.55)
        
    # Book Author
    lb3 = Label(labelFrame,text="Author : ", bg='black', fg='white')
    lb3.place(relx=0.05,rely=0.52, relheight=0.08)
        
    bookInfo3 = Entry(labelFrame)
    bookInfo3.place(relx=0.37,rely=0.52, relwidth=0.55)
        
    # Book Status
   # lb4 = Label(labelFrame,text="Status(Avail/issued) : ", bg='black', fg='white')
   # lb4.place(relx=0.05,rely=0.64, relheight=0.08)
        
   # bookInfo4 = Entry(labelFrame)
   # bookInfo4.place(relx=0.37,rely=0.64, relwidth=0.55)
    
    lb5 = Label(labelFrame,text="Number of copies : ", bg='black', fg='white')
    lb5.place(relx=0.05,rely=0.72, relheight=0.08)
        
    bookInfo5 = Entry(labelFrame)
    bookInfo5.place(relx=0.37,rely=0.72, relwidth=0.2)
    
    section = ('Engineering', 'Medical', 'Chemistry', 'Physics', 'Mathematics', 'Computer Science',
        'Arts', 'LAW', 'Biotech')

    # create a combobox
    sel_section = StringVar(labelFrame,'Section','sds')

    bookInfo6 = ttk.Combobox(labelFrame, textvariable=sel_section)
    bookInfo6['values'] = section
    bookInfo6['state'] = 'readonly'  # normal
    bookInfo6.place(relx=0.6,rely=0.72, relwidth=0.324)
    print(bookInfo6)
    #Submit Button
    SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black',command=bookRegister)
    SubmitBtn.place(relx=0.28,rely=0.87, relwidth=0.18,relheight=0.065)
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.87, relwidth=0.18,relheight=0.065)
    
    root.mainloop()
