from tkinter import *
from PIL import ImageTk, Image
import webview
#import tkinter as tk
from tkinter import messagebox
from tkinter.messagebox import askyesno
import mysql.connector
from cryptography.fernet import Fernet

key = "X0FsvboiGPfFXNxeDQr7KqxDjF2qQpg_tF5p6-lrK48="

mypass = "mypass"
mydatabase="db"


conn = mysql.connector.connect(host="localhost",user="root",password=mypass)
cur = conn.cursor()  
cur.execute("CREATE DATABASE IF NOT EXISTS db") 
conn.close

con = mysql.connector.connect(host="localhost",user="root",password=mypass,database=mydatabase)
cur = con.cursor()

bookTable = "books" 

def vreqbook():
	root = Tk()
	root.title("Requests")
	root.minsize(width=400,height=400)
	root.geometry("700x600")
	Canvas1 = Canvas(root) 
	Canvas1.config(bg="#292929")
	Canvas1.pack(expand=True,fill=BOTH)
        
        
	headingFrame1 = Frame(root,bg="#ededed",bd=5)
	headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
	headingLabel = Label(headingFrame1, text="Requests Received", bg='black', fg='white', font=('Courier',15))
	headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

	vlist = Listbox(root,bg='black', fg='white', font=('calibri',13))#, yscrollcommand = v.set )
	vlist.place(relx=0.1,rely=0.3, relwidth=0.81, relheight=0.5)
	vlist.insert(0, "")
	vlist.insert(1, "          %-85s%-85s"%('user','bid'))
	vlist.insert(2, "----------------------------------------------------------------------------------------------------------------")
	#  Label(labelFrame, text="%-15s%-45s%-30s%-10s"%('BID','Title','Author','Status'),bg='black',fg='white').place(relx=0.07,rely=0.1)
	#   Label(labelFrame, 	text="----------------------------------------------------------------------------------------------------",bg='black',fg='white').place(relx=0.05,rely=0.2)
	getBooks = "select * from requests";
	try:
		cur.execute(getBooks)
		for i in cur:
		    vlist.insert(3, "          %-65s%-35s"%(i[0],i[1]))
		    #Label(labelFrame, text="%-15s%-45s%-30s%-10s"%(i[0],i[1],i[2],i[3]),bg='black',fg='white').place(relx=0.07,rely=y)
		   # y += 0.1
		con.commit()
	except:
		messagebox.showinfo("Message","No requests received")
	
	def clear():
		cur.execute("drop table requests")
		root.refresh()
	
	clearBtn = Button(root,text="Clear",bg='#f7f1e3', fg='black', command=clear).place(relx=0.2,rely=0.87, relwidth=0.18,relheight=0.065)
	
	quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy).place(relx=0.6,rely=0.87, relwidth=0.18,relheight=0.065)
def borrow():
	try:
		root = Tk()
		root.title("Open Digital Library")
		root.minsize(width=400,height=400)
		root.geometry("1152x640")
		root.grid_rowconfigure(0, weight=1)
		root.columnconfigure(0, weight=1)
		cur.execute("select * from "+bookTable)
		for i in cur:	
			copi=(i[0])
		con.commit()
		cur.execute("CREATE TABLE IF NOT EXISTS requests(user VARCHAR(255), bid INT)")
		con.commit()
		
		fernet = Fernet(key)
		with open('cred', 'rb') as enc_file:
			encrypted = enc_file.read()
		decrypted = fernet.decrypt(encrypted)
		with open('cred', 'wb') as dec_file:
			dec_file.write(decrypted)
		f = open("cred", "r")
		uid = f.readline()
		uid = uid.rstrip()
		with open('cred', 'rb') as file:
			original = file.read()
		encrypted = fernet.encrypt(original)
		with open('cred', 'wb') as encrypted_file:
			encrypted_file.write(encrypted)
		frame_main = Frame(root, bg="#262626")
		#frame_main.grid(sticky='news')
		frame_main.pack(fill="both", expand=1)


		Label(frame_main, text="Local Library", bg='#262626', fg='white', font=('calibri',16)).grid(row=0,column=0,pady=10,padx=10, sticky='nw')

		# Create a frame for the canvas with non-zero row&column weights
		frame_canvas = Frame(frame_main)
		frame_canvas.grid(row=2, column=0, pady=(5, 0), sticky='nw')
		frame_canvas.grid_rowconfigure(0, weight=1)
		frame_canvas.grid_columnconfigure(0, weight=1)
		# Set grid_propagate to False to allow 5-by-5 buttons resizing later
		frame_canvas.grid_propagate(False)

		# Add a canvas in that frame
		canvas = Canvas(frame_canvas, bg="#262626")
		canvas.grid(row=0, column=0, sticky="news")
		# Link a scrollbar to the canvas
		vsb = Scrollbar(frame_canvas, orient="vertical", command=canvas.yview)
		vsb.grid(row=0, column=1, sticky='ns')
		canvas.configure(yscrollcommand=vsb.set)

		# Create a frame to contain the buttons
		frame_buttons = Frame(canvas, bg="#262626")
		canvas.create_window((0, 0), window=frame_buttons, anchor='nw')


		
		def req(bid,idx):
			cur.execute("select * from requests where user='"+str(uid)+"' AND bid='"+str(bid)+"'")
			msg = cur.fetchone()  
			# check if it is empty and print error
			checkAvail = "select copies from "+bookTable+" where bid = '"+str(bid)+"'"
			cur.execute(checkAvail)
			for i in cur:
				check = i[0]
			#print(check)
			#if check == 'avail':
			con.commit()
			if check > 0:
				if not msg:
					cur.execute("select copies from books where bid='"+str(bid)+"'")
					for i in cur:	
						copi=(i[0])
						print(copi)
					if copi>0:
						answer = askyesno(title='confirmation',
						message='Are you sure that you want to book it?')
						if answer:
							#Toplevel.message()
							#for i in bid:
							cur.execute("insert into requests values('"+str(uid)+"','"+str(bid)+"')")
							con.commit()
							print(bid)
							print(idx)
							#root.lift()
							root.destroy()
							borrow()
							#button["state"] = DISABLED
						#	buttons[idx].config(state=DISABLED)
						else:
							root.destroy()
							borrow()
						#root.lift()
					else:
						messagebox.showinfo("Error","No book left to be borrowed.")
						root.destroy()
						borrow()
				else:
					messagebox.showinfo("Error","You have already booked it.")
					root.destroy()
					borrow()
			else:
				messagebox.showinfo("Error","No more books available.")




		def home():
			
			copi=[]
			bid=[]
			title=[]
			
			#getcopies="select copies from "+bookTable;
			cur.execute("select * from "+bookTable)
			for i in cur:	
				bid.append(i[0])	
				title.append(i[1])
				copi.append(i[3])
			con.commit()
			#cur.execute(getcopies)
			

					
			#for i in cur:	
			#	copi.append(i[0])
				#copi[i]=(i[0])
			#	vlist.insert(END, "          %-15s%-45s%-30s%-10s%-10s"%(i[0],i[1],i[2],i[3],i[4]))
			    #Label(labelFrame, text="%-15s%-45s%-30s%-10s"%(i[0],i[1],i[2],i[3]),bg='black',fg='white').place(relx=0.07,rely=y)
			   # y += 0.1
			#con.commit()
			#print(cur)
			#print(getcopies)
			#print(copi)
			
		
			#for i in range(len(bid)):
				#Button(frame_buttons, text=str(title[i])+"\n\n\n\n"+str(copi[i])+" copies left",command=lambda i=i :req(bid[i],i), bg="#404040", fg="white", state=NORMAL).grid(row=3, column=i, padx=20, pady=10,ipadx=20, ipady=65, sticky='nw')
			for i in range(len(bid)):
				for j in range(6):
					Label(frame_buttons, bg='#262626', fg='white', font=('calibri',24)).grid(row=i,column=j,padx=10,pady=30,ipadx=85, ipady=110, sticky='nw')
					
			Label(frame_buttons, text="Welcome \n\n;-) ", bg='#262626', fg='white', font=('calibri',24)).grid(row=0,column=0,pady=30,padx=20,ipadx=10, ipady=70, sticky='nw')
			Label(frame_buttons, text="to your\nLocal\nLibrary", bg='#262626', fg='white', font=('calibri',24)).grid(row=0,column=1,pady=30,padx=20,ipadx=10, ipady=70, sticky='nw')
			#Label(frame_buttons, text="Local", bg='#262626', fg='white', font=('calibri',24)).grid(row=0,column=2,pady=30,padx=20,ipadx=10, ipady=70, sticky='nw')
			#Label(frame_buttons, text="Library", bg='#262626', fg='white', font=('calibri',24)).grid(row=0,column=3,pady=30,padx=20,ipadx=10, ipady=70, sticky='nw')
			
			frame_buttons.update_idletasks()
			#frame_canvas.config(width=1139 + vsb.winfo_width(), height=550)
			canvas.config(scrollregion=canvas.bbox("all"))
			
		home()

		def engi():
			copi=[]
			bid=[]
			title=[]
			#getcopies="select copies from "+bookTable;
			cur.execute("select * from "+bookTable+" where section='Engineering'")
			for i in cur:	
				bid.append(i[0])
				title.append(i[1])
				copi.append(i[3])
			con.commit()
			cnt=0
			for j in range(6):
				for i in range(len(bid)):
					cnt+=1
					if cnt>(len(bid)):
						break
					Button(frame_buttons, text=str(title[i])+"\n\n\n\n"+str(copi[i])+" copies left",command=lambda i=i :req(bid[i],i), bg="#404040", fg="white", state=NORMAL).grid(row=j, column=i, padx=20, pady=40,ipadx=20, ipady=65, sticky='nw')


			frame_buttons.update_idletasks()
			canvas.config(scrollregion=canvas.bbox("all"))

			
		def medi():
			copi=[]
			bid=[]
			title=[]
			#getcopies="select copies from "+bookTable;
			cur.execute("select * from "+bookTable+" where section='Medical'")
			for i in cur:	
				bid.append(i[0])
				title.append(i[1])
				copi.append(i[3])
			con.commit()
			cnt=0
			for j in range(6):
				for i in range(len(bid)):
					cnt+=1
					if cnt>(len(bid)):
						break
					Button(frame_buttons, text=str(title[i])+"\n\n\n\n"+str(copi[i])+" copies left",command=lambda i=i :req(bid[i],i), bg="#404040", fg="white", state=NORMAL).grid(row=j, column=i, padx=20, pady=40,ipadx=20, ipady=65, sticky='nw')


			frame_buttons.update_idletasks()
			canvas.config(scrollregion=canvas.bbox("all"))
			
		def chem():
			copi=[]
			bid=[]
			title=[]
			#getcopies="select copies from "+bookTable;
			cur.execute("select * from "+bookTable+" where section='Chemistry'")
			for i in cur:	
				bid.append(i[0])
				title.append(i[1])
				copi.append(i[3])
			con.commit()

			cnt=0
			for j in range(6):
				for i in range(len(bid)):
					cnt+=1
					if cnt>(len(bid)):
						break
					Button(frame_buttons, text=str(title[i])+"\n\n\n\n"+str(copi[i])+" copies left",command=lambda i=i :req(bid[i],i), bg="#404040", fg="white", state=NORMAL).grid(row=j, column=i, padx=20, pady=40,ipadx=20, ipady=65, sticky='nw')


			frame_buttons.update_idletasks()
			canvas.config(scrollregion=canvas.bbox("all"))
			
			
		def phys():
			copi=[]
			bid=[]
			title=[]
			#getcopies="select copies from "+bookTable;
			cur.execute("select * from "+bookTable+" where section='Physics'")
			for i in cur:	
				bid.append(i[0])
				title.append(i[1])
				copi.append(i[3])
			con.commit()

			cnt=0
			for j in range(6):
				for i in range(len(bid)):
					cnt+=1
					if cnt>(len(bid)):
						break
					Button(frame_buttons, text=str(title[i])+"\n\n\n\n"+str(copi[i])+" copies left",command=lambda i=i :req(bid[i],i), bg="#404040", fg="white", state=NORMAL).grid(row=j, column=i, padx=20, pady=40,ipadx=20, ipady=65, sticky='nw')


			frame_buttons.update_idletasks()
			canvas.config(scrollregion=canvas.bbox("all"))
			
			
		def math():
			copi=[]
			bid=[]
			title=[]
			#getcopies="select copies from "+bookTable;
			cur.execute("select * from "+bookTable+" where section='Mathematics'")
			for i in cur:	
				bid.append(i[0])
				title.append(i[1])
				copi.append(i[3])
			con.commit()

			cnt=0
			for j in range(6):
				for i in range(len(bid)):
					cnt+=1
					if cnt>(len(bid)):
						break
					Button(frame_buttons, text=str(title[i])+"\n\n\n\n"+str(copi[i])+" copies left",command=lambda i=i :req(bid[i],i), bg="#404040", fg="white", state=NORMAL).grid(row=j, column=i, padx=20, pady=40,ipadx=20, ipady=65, sticky='nw')


			frame_buttons.update_idletasks()
			canvas.config(scrollregion=canvas.bbox("all"))
			
			
		def comp():
			copi=[]
			bid=[]
			title=[]
			#getcopies="select copies from "+bookTable;
			cur.execute("select * from "+bookTable+" where section='Computer Science'")
			for i in cur:	
				bid.append(i[0])
				title.append(i[1])
				copi.append(i[3])
			con.commit()

			cnt=0
			for j in range(6):
				for i in range(len(bid)):
					cnt+=1
					if cnt>(len(bid)):
						break
					Button(frame_buttons, text=str(title[i])+"\n\n\n\n"+str(copi[i])+" copies left",command=lambda i=i :req(bid[i],i), bg="#404040", fg="white", state=NORMAL).grid(row=j, column=i, padx=20, pady=40,ipadx=20, ipady=65, sticky='nw')


			frame_buttons.update_idletasks()
			canvas.config(scrollregion=canvas.bbox("all"))
			
			
		def art():
			copi=[]
			bid=[]
			title=[]
			#getcopies="select copies from "+bookTable;
			cur.execute("select * from "+bookTable+" where section='Arts'")
			for i in cur:	
				bid.append(i[0])
				title.append(i[1])
				copi.append(i[3])
			con.commit()

			cnt=0
			for j in range(6):
				for i in range(len(bid)):
					cnt+=1
					if cnt>(len(bid)):
						break
					Button(frame_buttons, text=str(title[i])+"\n\n\n\n"+str(copi[i])+" copies left",command=lambda i=i :req(bid[i],i), bg="#404040", fg="white", state=NORMAL).grid(row=j, column=i, padx=20, pady=40,ipadx=20, ipady=65, sticky='nw')


			frame_buttons.update_idletasks()
			canvas.config(scrollregion=canvas.bbox("all"))
			
			
		def law():
			copi=[]
			bid=[]
			title=[]
			#getcopies="select copies from "+bookTable;
			cur.execute("select * from "+bookTable+" where section='LAW'")
			for i in cur:	
				bid.append(i[0])
				title.append(i[1])
				copi.append(i[3])
			con.commit()

			cnt=0
			for j in range(6):
				for i in range(len(bid)):
					cnt+=1
					if cnt>(len(bid)):
						break
					Button(frame_buttons, text=str(title[i])+"\n\n\n\n"+str(copi[i])+" copies left",command=lambda i=i :req(bid[i],i), bg="#404040", fg="white", state=NORMAL).grid(row=j, column=i, padx=20, pady=40,ipadx=20, ipady=65, sticky='nw')


			frame_buttons.update_idletasks()
			canvas.config(scrollregion=canvas.bbox("all"))
			
			
		def biot():
			copi=[]
			bid=[]
			title=[]
			#getcopies="select copies from "+bookTable;
			cur.execute("select * from "+bookTable+" where section='Biotech'")
			for i in cur:	
				bid.append(i[0])
				title.append(i[1])
				copi.append(i[3])
			con.commit()

			cnt=0
			for j in range(6):
				for i in range(len(bid)):
					cnt+=1
					if cnt>(len(bid)):
						break
					Button(frame_buttons, text=str(title[i])+"\n\n\n\n"+str(copi[i])+" copies left",command=lambda i=i :req(bid[i],i), bg="#404040", fg="white", state=NORMAL).grid(row=j, column=i, padx=20, pady=40,ipadx=20, ipady=65, sticky='nw')


			frame_buttons.update_idletasks()
			canvas.config(scrollregion=canvas.bbox("all"))
			
			

		"""	
		def yrr():
			rows = 20
			columns = 6
			#buttons = [[Button() for j in range(columns)] for i in range(rows)]
			for i in range(2, rows):
			    for j in range(0, columns):
				#Button(frame_buttons, text=("hehe%d,%d" % (i+1, j+1)),command=newb).grid(row=i, column=j,pady=10,padx=10, sticky='news')
			    	Button(frame_buttons, text="asdfasdf", image=img1).grid(row=i, column=j,pady=32,padx=32, sticky='news')
			frame_buttons.update_idletasks()
			canvas.config(scrollregion=canvas.bbox("all"))
		
		"""
		Button(frame_main, text="Home",command=home, bg="#404040", fg="white").grid(row=1, column=0, padx=20, pady=10, sticky='nw')
		Button(frame_main, text="Engineering",command=engi, bg="#404040", fg="white").grid(row=1, column=0, padx=110, pady=10, sticky='nw')
		Button(frame_main, text="Medical",command=medi, bg="#404040", fg="white").grid(row=1, column=0, padx=210, pady=10, sticky='nw')
		Button(frame_main, text="Mathematics",command=math, bg="#404040", fg="white").grid(row=1, column=0, padx=285, pady=10, sticky='nw')
		Button(frame_main, text="Physics",command=phys, bg="#404040", fg="white").grid(row=1, column=0, padx=395, pady=10, sticky='nw')
		Button(frame_main, text="Chemistry",command=chem, bg="#404040", fg="white").grid(row=1, column=0, padx=470, pady=10, sticky='nw')
		Button(frame_main, text="LAW",command=law, bg="#404040", fg="white").grid(row=1, column=0, padx=560, pady=10, sticky='nw')
		Button(frame_main, text="Arts",command=art, bg="#404040", fg="white").grid(row=1, column=0, padx=615, pady=10, sticky='nw')
		Button(frame_main, text="Computer Science",command=comp, bg="#404040", fg="white").grid(row=1, column=0, padx=667, pady=10, sticky='nw')
		Button(frame_main, text="Biotech",command=biot, bg="#404040", fg="white").grid(row=1, column=0, padx=810, pady=10, sticky='nw')
		
		#image1 = ImagePhotoImage(Image.open("img/textbok/Elements.jpg"))
		

		"""
		# Add 9-by-5 buttons to the frame
		rows = 10
		columns = 10
		#buttons = [[Button() for j in range(columns)] for i in range(rows)]
		for i in range(0, rows):
		    for j in range(0, columns):
		    	Button(frame_buttons, text=("%d,%d" % (i+1, j+1)),command=newb).grid(row=i, column=j,pady=10,padx=10, sticky='news')
		      #  buttons[i][j] = Button(frame_buttons, text=("%d,%d" % (i+1, j+1)))
		       # buttons[i][j].grid(row=i, column=j,pady=10,padx=10, sticky='news')
		"""
		# Update buttons frames idle tasks to let tkinter calculate buttons sizes
		frame_buttons.update_idletasks()

		# Resize the canvas frame to show exactly 5-by-5 buttons and the scrollbar
		#first5columns_width = sum([buttons[0][j].winfo_width() for j in range(0, 5)])
		#first5rows_height = sum([buttons[i][0].winfo_height() for i in range(0, 5)])
		frame_canvas.config(width=1139 + vsb.winfo_width(), height=550)

		# Set the canvas scrolling region
		canvas.config(scrollregion=canvas.bbox("all"))

		# Launch the GUI
		root.mainloop()
	except:
		root.destroy()
		messagebox.showinfo("Message","Either your organization haven't implemnted Open Library Admin in their library or you are out of your organization's network.")

#borrow()
