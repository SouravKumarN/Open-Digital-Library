import smtplib, ssl
from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
from main import *
from register import *
import mysql.connector
from cryptography.fernet import Fernet

# key generation
#key = Fernet.generate_key()
key = "X0FsvboiGPfFXNxeDQr7KqxDjF2qQpg_tF5p6-lrK48="
# string the key in a file

#with open('filekey.key', 'wb') as filekey:
#	filekey.write(key)



# Add your own database name and password here to reflect in the code
mypass = "mypass"
mydatabase="dbcred"


conn = mysql.connector.connect(host="localhost",user="root",password=mypass)
cur = conn.cursor()  
cur.execute("CREATE DATABASE IF NOT EXISTS "+mydatabase) 
conn.close

con = mysql.connector.connect(host="localhost",user="root",password=mypass,database=mydatabase)
cur = con.cursor()

# Enter Table Names here
issueTable = "books_issued" 
bookTable = "books"
    
#List To store all Book IDs
alluid = [] 

def login():
    
    global issueBtn,labelFrame,lb1,inf1,inf2,quitBtn,root,Canvas1,status
    
    uid = inf1.get()
    passw = inf2.get()

    issueBtn.destroy()
    labelFrame.destroy()
    lb1.destroy()
    inf1.destroy()
    inf2.destroy()
    acred = "acredentials"
    cur.execute("CREATE TABLE IF NOT EXISTS "+acred+" (name VARCHAR(255), phnum VARCHAR(255), uid VARCHAR(255) ,passw VARCHAR(255),PRIMARY KEY (uid))")
    con.commit()
    extractuid = "select uid from "+acred

#    try:
    cur.execute(extractuid)
    for i in cur:
        alluid.append(i[0])
    con.commit()
        #print(alluid)
    #print(bid)
 #   for x in allBid:
  #      if x==int(bid):
   # 	    print("dcddd")
    #    status=True
    if str(uid) in alluid:
        print(uid)
        checkAvail = "select passw from "+acred+" where uid = '"+(uid)+"'"
        cur.execute(checkAvail)
        for i in cur:
            check = i[0]
        #print(check)
        if check == passw:
            
# using the key
            fernet = Fernet(key)

  # f = open("acred", "r")
            f = open("acred", "w")
  


# opening the original file to encrypt
            with open('acred', 'rb') as file:
                original = file.read()
	
# encrypting the file
            encrypted = fernet.encrypt(original)

# opening the file in write mode and
# writing the encrypted data
            with open('acred', 'wb') as encrypted_file:
                encrypted_file.write(encrypted)
         #       status = True
         
         
         



# opening the encrypted file
            with open('acred', 'rb') as enc_file:
                encrypted = enc_file.read()

# decrypting the file
            decrypted = fernet.decrypt(encrypted)

# opening the file in write mode and
# writing the decrypted data
            with open('acred', 'wb') as dec_file:
                dec_file.write(decrypted)
	
	
            f.write("ucantcme")
         #   print(f.readline())
            f.close()





# opening the original file to encrypt
            with open('acred', 'rb') as file:
                original = file.read()
	
# encrypting the file
            encrypted = fernet.encrypt(original)

# opening the file in write mode and
# writing the encrypted data
            with open('acred', 'wb') as encrypted_file:
                encrypted_file.write(encrypted)
         #       status = True
                
            #cur.execute("CREATE TABLE IF NOT EXISTS actusr (name VARCHAR(255), phnum VARCHAR(255), uid VARCHAR(255) ,passw VARCHAR(255),PRIMARY KEY (uid))")
            #con.commit()
            #cur.execute("INSERT INTO actusr SELECT * FROM credentials WHERE uid = '"+(uid)+"'")
              #  cur.execute("CREATE TABLE actusr (name VARCHAR(255), phnum VARCHAR(255), uid VARCHAR(255) ,passw VARCHAR(255),PRIMARY KEY (uid))")
            #con.commit()
            
            root.destroy()
            main()
        else:
            root.destroy()
            logind()
        #        status = False
        con.commit()
    else:
        messagebox.showinfo("Error","User ID or Password is incorrect")
        root.destroy()
        logind()
            
 #   except:
  #      messagebox.showinfo("Error","Can't fetch User ID")

"""
    cur.execute("CREATE TABLE IF NOT EXISTS "+issueTable+" (bid INT,title VARCHAR(255))")
    issueSql = "insert into "+issueTable+" values ('"+bid+"','"+issueto+"')"
    #show = "select * from "+issueTable
    cur.execute(issueSql)
    con.commit()
    #cur.nextset()
  #  cur.execute(show)	
   # con.commit()	
   # cur.nextset()
    updateStatus = "update "+bookTable+" set status = 'issued' where bid = '"+bid+"'"
   # con.commit()
    try:
        if int(bid) in allBid and status == True:
            cur.execute(issueSql)
            con.commit()
            cur.execute(updateStatus)
            con.commit()
            messagebox.showinfo('Success',"Book Issued Successfully")
            cur.execute("insert into history values('Book with id - ','"+bid+"','has been successfully issued.')")
            con.commit()
            root.destroy()
        else:
            allBid.clear()
            messagebox.showinfo('Message',"Book Already Issued")
            root.destroy()
            return
    except:
        messagebox.showinfo("Search Error","The value entered is wrong, Try again")
    
    print(bid)
    print(issueto)
    
    allBid.clear()
"""
def logind(): 
    
    global issueBtn,labelFrame,lb1,inf1,inf2,quitBtn,root,Canvas1,status
    
    root = Tk()
    root.title("Library")
    root.minsize(width=200,height=200)
    root.geometry("420x300")
    
    Canvas1 = Canvas(root)
    Canvas1.config(bg="#292929")
    Canvas1.pack(expand=True,fill=BOTH)

    headingFrame1 = Frame(root,bg="#ededed",bd=2)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Admin Login", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)  
        
    # Book ID
    lb1 = Label(labelFrame,text="User ID : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.2)
        
    inf1 = Entry(labelFrame)
    inf1.place(relx=0.3,rely=0.2, relwidth=0.62)
    
    # Issued To Student name 
    lb2 = Label(labelFrame,text="Password : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.5)
        
    inf2 = Entry(labelFrame,show='*')
    inf2.place(relx=0.3,rely=0.5, relwidth=0.62)
    
    def regis():
    	messagebox.showinfo("Message","Kindly email us at techaround18@gmail.com to get your organization verified and registered for using Open Digital Admin")
    
    #Issue Button
    issueBtn = Button(root,text="Login",bg='#aaa69d', fg='black',command=login)
    issueBtn.place(relx=0.28,rely=0.85, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Register",bg='#aaa69d', fg='black', command=regis)
    quitBtn.place(relx=0.53,rely=0.85, relwidth=0.18,relheight=0.08)
    
    try:
	    fernet = Fernet(key)
	    with open('acred', 'rb') as enc_file:
	    	encrypted = enc_file.read()
	    decrypted = fernet.decrypt(encrypted)
	    with open('acred', 'wb') as dec_file:
	    	dec_file.write(decrypted)
	    	
	    f = open("acred", "r")
	   # print(f.readline())
	    check=(f.readline())
	    #print(check)
	    #check=check.rstrip()
	    
	    with open('acred', 'rb') as file:
	    	original = file.read()
	    encrypted = fernet.encrypt(original)
	    with open('acred', 'wb') as encrypted_file:
	    	encrypted_file.write(encrypted)
	    
	    if check == "ucantcme":
	    	root.destroy()
	    	main()
	    else:
	    	print("Please Login")
	    f.close()

    
    except:
	    print("Please Login")
    
    root.mainloop()
logind()
