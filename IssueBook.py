import smtplib, ssl
from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import mysql.connector

#urlopen(request, context=ssl.create_default_context(cafile=certifi.where()))
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
issueTable = "books_issued" 
bookTable = "books"
    
def sendmail(bid, recev):
	cur.execute("select title from "+bookTable+" where bid = '"+str(bid)+"'")
	for i in cur:	
		title=(i[0])
	port = 587  # For starttls
	smtp_server = "smtp.gmail.com"
	sender_email = "techaround18@gmail.com"
	receiver_email = recev #"souravkumarnagal@gmail.com"
	password = "Sknmaa08"#input("Type your password and press enter:")
	subject="Book issued"
	text="You have successfully issued the book "+str(title)+", with id "+str(bid)+".\n\nOpen Library Admin,\nRegards"
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
"""
	port = 465  # For SSL
	smtp_server = "smtp.gmail.com"
	sender_email = "techaround18@gmail.com"  # Enter your address
	receiver_email = "souravkumarnagal@gmail.com"  # Enter receiver address
	password = "Sknmaa08"#input("Type your password and press enter: ")
	message = """\
"""	Subject: Hi there

	This message is sent from Python."""

"""	context = ssl.create_default_context()
	with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
	    server.login(sender_email, password)
	    server.sendmail(sender_email, receiver_email, message)    
"""

#List To store all Book IDs
allBid = [] 
auid = [] 

def issue():
    
    global issueBtn,labelFrame,lb1,inf1,inf2,quitBtn,root,Canvas1,status,recev
    
    bid = inf1.get()
    issueto = inf2.get()

    issueBtn.destroy()
    labelFrame.destroy()
    lb1.destroy()
    inf1.destroy()
    inf2.destroy()
    
    
    extractBid = "select bid from "+bookTable
    try:
        cur.execute(extractBid)
        for i in cur:
            allBid.append(i[0])
        con.commit()
        #print(allBid)
    #print(bid)
 #   for x in allBid:
  #      if x==int(bid):
   # 	    print("dcddd")
    #    status=True
        if int(bid) in allBid:
            #print(bid)
            checkAvail = "select copies from "+bookTable+" where bid = '"+(bid)+"'"
            cur.execute(checkAvail)
            for i in cur:
                check = i[0]
            #print(check)
            #if check == 'avail':
            if check > 0:
                status = True
            else:
                status = False
            con.commit()
        else:
            messagebox.showinfo("Error","Book ID not present")
    except:
        messagebox.showinfo("Error","Can't fetch Book IDs")
    cur.execute("CREATE TABLE IF NOT EXISTS "+issueTable+" (bid INT,issuedto VARCHAR(255))")
    issueSql = "insert into "+issueTable+" values ('"+bid+"','"+issueto+"')"
    #show = "select * from "+issueTable
    #cur.execute(issueSql)
    con.commit()
    #cur.nextset()
  #  cur.execute(show)	
   # con.commit()	
   # cur.nextset()
    #updateStatus = "update "+bookTable+" set status = 'issued' where bid = '"+bid+"'"
    updateStatus = "UPDATE books SET copies = copies - 1 WHERE bid = '"+str(bid)+"'"
   # con.commit()
#    try:
    if int(bid) in allBid and status == True:
        cur.execute(issueSql)
        con.commit()
        cur.execute(updateStatus)
        con.commit()
        """
        cur.execute("select uid from actusr")
        for i in cur:
            auid.append(i[0])
        con.commit()
        recev = (str(auid[0]))
        print(recev+"this is ")
        recev = inf2.get()
        """
        messagebox.showinfo('Success',"Book Issued Successfully")
       # cur.execute("UPDATE books SET copies = copies - 1 WHERE bid = '"+str(bid)+"'")
        cur.execute("insert into history values('Book with id - ','"+bid+"','has been successfully issued.')")
        con.commit()   
        sendmail(bid,issueto)    

        root.destroy()
    else:
        allBid.clear()
        messagebox.showinfo('Message',"No more books available")
        root.destroy()
        return
#    except:
 #       messagebox.showinfo("Search Error","The value entered is wrong, Try again")
    
    print(bid)
    print(issueto)
    
    allBid.clear()
    
def issueBook(): 
    
    global issueBtn,labelFrame,lb1,inf1,inf2,quitBtn,root,Canvas1,status
    
    root = Tk()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("500x450")
    
    Canvas1 = Canvas(root)
    Canvas1.config(bg="#292929")
    Canvas1.pack(expand=True,fill=BOTH)

    headingFrame1 = Frame(root,bg="#ededed",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Issue Book", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.4)  
        
    # Book ID
    lb1 = Label(labelFrame,text="Book ID : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.26)
        
    inf1 = Entry(labelFrame)
    inf1.place(relx=0.3,rely=0.26, relwidth=0.63)
    
    # Issued To Student name 
    lb2 = Label(labelFrame,text="Issued To : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.55)
        
    inf2 = Entry(labelFrame)
    inf2.place(relx=0.3,rely=0.55, relwidth=0.63)
    
    
    #Issue Button
    issueBtn = Button(root,text="Issue",bg='#d1ccc0', fg='black',command=issue)
    issueBtn.place(relx=0.28,rely=0.825, relwidth=0.18,relheight=0.065)
    
    quitBtn = Button(root,text="Quit",bg='#aaa69d', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.825, relwidth=0.18,relheight=0.065)
    
    root.mainloop()
