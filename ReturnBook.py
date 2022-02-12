import smtplib, ssl
from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import mysql.connector

# Add your own database name and password here to reflect in the code
mypass = "mypass"
mydatabase="db"


conn = mysql.connector.connect(host="localhost",user="root",password=mypass)
cur = conn.cursor()  
cur.execute("CREATE DATABASE IF NOT EXISTS db") 
conn.close

con = mysql.connector.connect(host="localhost",user="root",password=mypass,database=mydatabase)
cur = con.cursor()

# Enter Table Names here
issueTable = "books_issued" #Issue Table
bookTable = "books" #Book Table
    
def sendmail(bid, recev):
	cur.execute("select title from "+bookTable+" where bid = '"+str(bid)+"'")
	for i in cur:	
		title=(i[0])
	port = 587  # For starttls
	smtp_server = "smtp.gmail.com"
	sender_email = "techaround18@gmail.com"
	receiver_email = recev #"souravkumarnagal@gmail.com"
	password = "Sknmaa08"#input("Type your password and press enter:")
	subject="Book returned"
	text="You have successfully returned the book "+str(title)+", with id "+str(bid)+".\n\nOpen Library Admin,\nRegards"
	message = 'Subject: {}\n\n{}'.format(subject, text)
	"""\
	Subject: Book issued

	You have successfully issued the book """+str(title)+""", with id """+str(bid)+"""."""

	context = ssl.create_default_context()
	with smtplib.SMTP(smtp_server, port) as server:
	    server.ehlo()  # Can be omitted
	    server.starttls(context=context)
	    server.ehlo()  # Can be omitted
	    server.login(sender_email, password)
	    server.sendmail(sender_email, receiver_email, message)


allBid = [] #List To store all Book IDs
checklist = []
def returnn():
    
    global SubmitBtn,labelFrame,lb1,bookInfo1,quitBtn,root,Canvas1,status
    
    bid = bookInfo1.get()
    issueto = bookInfo2.get()
   # sendmail(bid,issueto)
    print (bid)
    extractBid = "select bid from "+issueTable
    try:
        cur.execute(extractBid)

        for i in cur:
            allBid.append(i[0])
        con.commit()
        #print(allBid) 
        if int(bid) in allBid:
            checkAvail = "select issuedto from "+issueTable+" where bid = '"+bid+"'"
            cur.execute(checkAvail)

            for i in cur:
                #check = i[0] 
                checklist.append(i[0]) 
            con.commit()
            #if check == 'issued':
            print(checklist)
            if issueto in checklist:
                status = True
            else:
                status = False
            con.commit()
        else:
            messagebox.showinfo("Error","Book ID not present")
    except:
        messagebox.showinfo("Error","Can't fetch Book IDs")
  #  print(allBid)
   
    
    issueSql = "delete from "+issueTable+" where bid = '"+bid+"' AND issuedto = '"+issueto+"'"
  
   # print(bid in allBid)
  #  print(status)
    updateStatus = "UPDATE books SET copies = copies + 1 WHERE bid = '"+str(bid)+"'"
    try:
        if int(bid) in allBid and status == True:
            cur.execute(issueSql)
            con.commit()
            cur.execute(updateStatus)
            con.commit()
            messagebox.showinfo('Success',"Book Returned Successfully")
           # cur.execute("UPDATE books SET copies = copies + 1 WHERE bid = '"+str(bid)+"'")
            cur.execute("insert into history values('Book with id - ','"+bid+"','has been successfully returned.')")
            con.commit()
            sendmail(bid,issueto)
        else:
            allBid.clear()
            messagebox.showinfo('Message',"Please check details carefully")
            root.destroy()
            return
    except:
        messagebox.showinfo("Search Error","The value entered is wrong, Try again")
    
    
    allBid.clear()
    root.destroy()
    
def returnBook(): 
    
    global bookInfo1,bookInfo2,SubmitBtn,quitBtn,Canvas1,con,cur,root,labelFrame, lb1
    
    root = Tk()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("500x450")

    
    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="#292929")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="#ededed",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Return Book", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.4)   
        
    # Book ID to Delete
    lb1 = Label(labelFrame,text="Book ID : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.25)
        
    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3,rely=0.25, relwidth=0.62)
    
    lb2 = Label(labelFrame,text="Returned by : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.6)
    
    bookInfo2 = Entry(labelFrame)
    bookInfo2.place(relx=0.3,rely=0.6, relwidth=0.62)
    
    #Submit Button
    SubmitBtn = Button(root,text="Return",bg='#d1ccc0', fg='black',command=returnn)
    SubmitBtn.place(relx=0.28,rely=0.87, relwidth=0.18,relheight=0.065)
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.87, relwidth=0.18,relheight=0.065)
    
    root.mainloop()
