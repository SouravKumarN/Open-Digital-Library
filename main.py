import smtplib, ssl
from tkinter import *
from PIL import Image, ImageTk
#import pymysql
import mysql.connector
from tkinter import messagebox
from AddBook import *
from DeleteBook import *
from ViewBooks import *
from IssueBook import *
from ReturnBook import *
from borrow import *
import os
# Add your own database name and password here to reflect in the code
mypass = "mypass"
mydatabase="db"

conn = mysql.connector.connect(host="localhost",user="root",password=mypass)
cur = conn.cursor()  
cur.execute("CREATE DATABASE IF NOT EXISTS db") 
conn.close

conn = mysql.connector.connect(host="localhost",user="root",password=mypass,database=mydatabase)#, port=3306)
cur = conn.cursor()
 
def main(): 
	root = Tk()
	root.title("Open Library Admin")
	root.minsize(width=400,height=400)
	root.geometry("1152x640")

	# Take n greater than 0.25 and less than 5
	same=True
	n=0.3

	# Adding a background image
	background_image =Image.open("e.jpg")
	[imageSizeWidth, imageSizeHeight] = background_image.size

	newImageSizeWidth = int(imageSizeWidth*n)
	if same:
	    newImageSizeHeight = int(imageSizeHeight*n) 
	else:
	    newImageSizeHeight = int(imageSizeHeight/n) 
	    
	background_image = background_image.resize((newImageSizeWidth,newImageSizeHeight),Image.ANTIALIAS)
	img = ImageTk.PhotoImage(background_image)

	Canvas1 = Canvas(root)

	Canvas1.create_image(650,400,image = img)      
	Canvas1.config(bg="white",width = newImageSizeWidth, height = newImageSizeHeight)
	Canvas1.pack(expand=True,fill=BOTH)

	headingFrame1 = Frame(root,bg="#ededed",bd=5)
	headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.12)

	headingLabel = Label(headingFrame1, text="Welcome to Open Library Admin", bg='#292929', fg='white', font=('calibri',18))
	headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)




	cur.execute("CREATE TABLE IF NOT EXISTS history(his VARCHAR(255), id INT, hist VARCHAR(255))")
	#conn.commit()
	
	cur.execute("CREATE TABLE IF NOT EXISTS requests(user VARCHAR(255), bid INT)")
	conn.commit()

	#v = Scrollbar(root, orient='vertical')
	#v.pack(side = RIGHT, fill = Y)
	#headingLabel2 = Label(root, text="History - \n___________________________________________\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n", bg='#292929', fg='white', font=('calibri',12), xyscrollcommand = v.set)
	#headingLabel2.place(relx=0.4,rely=0.4, relwidth=0.52, relheight=0.5)
	mylist = Listbox(root,bg='#292929', fg='white', font=('calibri',16))#, yscrollcommand = v.set )

	 #   Label(labelFrame, text="%-10s%-30s%-30s%-20s"%(i[0],i[1],i[2],i[3]),bg='black',fg='white').place(relx=0.07,rely=y)
	  #  y += 0.1

	#for line in range(100):
	 #  mylist.insert(END, "This is line number " + str(line))
	#v.config(command=t.yview)
	mylist.place(relx=0.4,rely=0.3, relwidth=0.55, relheight=0.6)
	#v.config( command = mylist.yview )



	def get_data():
		cur.execute("select * from history")
		mylist.insert(0, "")
		mylist.insert(1, "                                                      HISTORY")
		mylist.insert(2, "                 ------------------------------------------------------------------")
		#mylist.config(font=bolded)
		mylist.delete(3,END)
		
		for i in cur:
		    mylist.insert(3, "    ->      "+"%-10s%-4s%-10s"%(i[0],i[1],i[2]))
		conn.commit()

		root.after(2000, get_data)
	
	def logout():
		os.remove("acred")
		#cur.execute("drop table actusr")
		#con.commit()
		cur.execute("drop table history")
		con.commit()
		root.destroy()

	get_data()
	btn1 = Button(root,text="Add Book Details",bg='#292929', fg='white', font=('calibri',12), command=addBook)
	btn1.place(relx=0.1,rely=0.35, relwidth=0.25,relheight=0.1)
	    
	btn2 = Button(root,text="Delete Book",bg='#292929', fg='white', font=('calibri',12), command=delete)
	btn2.place(relx=0.1,rely=0.45, relwidth=0.25,relheight=0.1)
	    
	btn3 = Button(root,text="View Book List",bg='#292929', fg='white', font=('calibri',12), command=View)
	btn3.place(relx=0.1,rely=0.55, relwidth=0.25,relheight=0.1)
	    
	btn4 = Button(root,text="Issue Book",bg='#292929', fg='white', font=('calibri',12), command = issueBook)
	btn4.place(relx=0.1,rely=0.65, relwidth=0.13,relheight=0.1)
	    
	btn5 = Button(root,text="Return Book",bg='#292929', fg='white', font=('calibri',12), command = returnBook)
	btn5.place(relx=0.1,rely=0.75, relwidth=0.25,relheight=0.1)

	btn6 = Button(root,text="Logout",bg='#292929', fg='white', font=('calibri',12), command = logout)
	btn6.place(relx=0.87,rely=0.925, relwidth=0.1,relheight=0.05)
	
	btn7 = Button(root,text="Requests",bg='#292929', fg='white', font=('calibri',12), command = vreqbook)
	btn7.place(relx=0.23,rely=0.65, relwidth=0.12,relheight=0.1)
	
	root.mainloop()
