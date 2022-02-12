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
bookTable = "books" 
    
def View(): 
    
    root = Tk()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("700x600")


    Canvas1 = Canvas(root) 
    Canvas1.config(bg="#292929")
    Canvas1.pack(expand=True,fill=BOTH)
        
        
    headingFrame1 = Frame(root,bg="#ededed",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="View Books", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
  #  labelFrame = Frame(root,bg='black')
   # labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)
  #  y = 0.25
    
    
    vlist = Listbox(root,bg='black', fg='white', font=('calibri',13))#, yscrollcommand = v.set )
    vlist.place(relx=0.1,rely=0.3, relwidth=0.81, relheight=0.5)
    vlist.insert(0, "")
    vlist.insert(1, "          %-15s%-45s%-30s%-10s"%('BID','Title','Author','Copies'))
    vlist.insert(2, "----------------------------------------------------------------------------------------------------------------")
  #  Label(labelFrame, text="%-15s%-45s%-30s%-10s"%('BID','Title','Author','Status'),bg='black',fg='white').place(relx=0.07,rely=0.1)
 #   Label(labelFrame, 	text="----------------------------------------------------------------------------------------------------",bg='black',fg='white').place(relx=0.05,rely=0.2)
    getBooks = "select * from "+bookTable;
    try:
        cur.execute(getBooks)
        for i in cur:
            vlist.insert(END, "          %-15s%-45s%-30s%-10s"%(i[0],i[1],i[2],i[3]))
            #Label(labelFrame, text="%-15s%-45s%-30s%-10s"%(i[0],i[1],i[2],i[3]),bg='black',fg='white').place(relx=0.07,rely=y)
           # y += 0.1
        con.commit()
    except:
        messagebox.showinfo("Failed to fetch files from database")
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.4,rely=0.87, relwidth=0.18,relheight=0.065)
    
    root.mainloop()
