from tkinter import *
from PIL import ImageTk, Image
import webview
import tkinter as tk
from borrow import *
import mysql.connector
import os
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


def digimain():
	root = tk.Tk()
	root.title("Open Digital Library")
	root.minsize(width=400,height=400)
	root.geometry("1920x1080")
	root.grid_rowconfigure(0, weight=1)
	root.columnconfigure(0, weight=1)
	
	fernet = Fernet(key)
	with open('cred', 'rb') as enc_file:
		encrypted = enc_file.read()
	decrypted = fernet.decrypt(encrypted)
	with open('cred', 'wb') as dec_file:
		dec_file.write(decrypted)
	f = open("cred", "r")
	f.readline()
	uname = f.readline()
	uname = uname.rstrip()
	with open('cred', 'rb') as file:
		original = file.read()
	encrypted = fernet.encrypt(original)
	with open('cred', 'wb') as encrypted_file:
		encrypted_file.write(encrypted)
	frame_main = tk.Frame(root, bg="#262626")
	#frame_main.grid(sticky='news')
	frame_main.pack(fill="both", expand=1)


	tk.Label(frame_main, text="Open Digital Library", bg='#262626', fg='white', font=('calibri',16)).grid(row=0,column=0,pady=10,padx=10, sticky='nw')
	"""
	label1 = tk.Label(frame_main, text="Label 1", fg="green")
	label1.grid(row=0, column=0, pady=(5, 0), sticky='nw')

	label2 = tk.Label(frame_main, text="Label 2", fg="blue")
	label2.grid(row=1, column=0, pady=(5, 0), sticky='nw')

	label3 = tk.Label(frame_main, text="Label 3", fg="red")
	label3.grid(row=3, column=0, pady=5, sticky='nw')
	"""

	# Create a frame for the canvas with non-zero row&column weights
	frame_canvas = tk.Frame(frame_main)
	frame_canvas.grid(row=2, column=0, pady=(5, 0), sticky='nw')
	frame_canvas.grid_rowconfigure(0, weight=1)
	frame_canvas.grid_columnconfigure(0, weight=1)
	# Set grid_propagate to False to allow 5-by-5 buttons resizing later
	frame_canvas.grid_propagate(False)

	# Add a canvas in that frame
	canvas = tk.Canvas(frame_canvas, bg="#262626")
	canvas.grid(row=0, column=0, sticky="news")
	# Link a scrollbar to the canvas
	vsb = tk.Scrollbar(frame_canvas, orient="vertical", command=canvas.yview)
	vsb.grid(row=0, column=1, sticky='ns')
	canvas.configure(yscrollcommand=vsb.set)

	# Create a frame to contain the buttons
	frame_buttons = tk.Frame(canvas, bg="#262626")
	canvas.create_window((0, 0), window=frame_buttons, anchor='nw')

	#tk.Label(frame_buttons, text="Welcome !", bg='#262626', fg='white',font=('calibri',94)).grid(row=1, column=0,pady=100,padx=100, sticky='news')

	#img1 = ImageTk.PhotoImage(Image.open("img/OL19374060M-M.jpg"))
	"""
	def web():
		webview.create_window('ebook', 'https://www.gutenberg.org/files/65304/65304-h/65304-h.htm')
		webview.start()
		
	#button_qwer = tk.Button(frame_buttons, text="asdfasdf", image=img1, command=web)
	#button_qwer.place(relx=0.1,rely=0.45)
	"""

	img1 = ImageTk.PhotoImage(Image.open("img/home/Pride and Prejudice.jpg"))
	img2 = ImageTk.PhotoImage(Image.open("img/home/The Great Gatsby.jpg"))
	img3 = ImageTk.PhotoImage(Image.open("img/home/A Tale of Two Cities.jpg"))
	img4 = ImageTk.PhotoImage(Image.open("img/home/The Importance of Being Earnest.jpg"))
	img5 = ImageTk.PhotoImage(Image.open("img/home/Alice in Wonderland.jpg"))
	img6 = ImageTk.PhotoImage(Image.open("img/home/A Doll's House.jpg"))
	img8 = ImageTk.PhotoImage(Image.open("img/home/Metamorphosis.jpg"))
	img7 = ImageTk.PhotoImage(Image.open("img/home/The Picture of Dorian Gray.jpg"))
	img9 = ImageTk.PhotoImage(Image.open("img/home/The Adventures of Sherlock Holmes.jpg"))
	img10 = ImageTk.PhotoImage(Image.open("img/home/Moby Dick; Or, The Whale.jpg"))


	def home():

		tk.Label(frame_buttons, text="Top Picks : ", bg='#262626', fg='white', font=('calibri',24)).grid(row=0,column=0,pady=30,padx=30,ipadx=29, ipady=145, sticky='nw')
		tk.Label(frame_buttons, bg='#262626', fg='white').grid(row=1, column=0,ipadx=80, ipady=14, sticky='n')
		
		tk.Button(frame_buttons, image=img1, command=lambda :(webview.create_window('Pride and Prejudice', 'https://www.gutenberg.org/files/1342/1342-h/1342-h.htm'),webview.start())).grid(row=0, column=1, pady=30,padx=30, sticky='news')
		tk.Label(frame_buttons, text="Pride and Prejudice", bg='#262626', fg='white').grid(row=1, column=1,ipadx=40, ipady=14, sticky='n')
		
		tk.Button(frame_buttons, image=img2, command=lambda :(webview.create_window('The Great Gatsby', 'https://www.gutenberg.org/files/64317/64317-h/64317-h.htm'),webview.start())).grid(row=0, column=2,pady=30,padx=30, sticky='news')
		tk.Label(frame_buttons, text="The Great Gatsby", bg='#262626', fg='white').grid(row=1, column=2,ipadx=40, ipady=14, sticky='n')
		
		tk.Button(frame_buttons, image=img3, command=lambda :(webview.create_window('A Tale of Two Cities', 'https://www.gutenberg.org/files/98/98-h/98-h.htm'),webview.start())).grid(row=0, column=3,pady=30,padx=30, sticky='news')
		tk.Label(frame_buttons, text="A Tale of Two Cities", bg='#262626', fg='white').grid(row=1, column=3,ipadx=40, ipady=14, sticky='n')
		
		tk.Button(frame_buttons, image=img4, command=lambda :(webview.create_window('The Importance of Being Earnest', 'https://www.gutenberg.org/files/844/844-h/844-h.htm'),webview.start())).grid(row=0, column=4,pady=30,padx=30, sticky='news')
		tk.Label(frame_buttons, text="The Importance of Being\n Earnest", bg='#262626', fg='white').grid(row=1, column=4,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=img5, command=lambda :(webview.create_window('Alice in Wonderland', 'https://openlibrary.org/borrow/ia/stonesofvenice01year1851rusk?ref=ol'),webview.start())).grid(row=2, column=0,pady=30,padx=30, sticky='news')
		tk.Label(frame_buttons, text="Alice in Wonderland", bg='#262626', fg='white').grid(row=3, column=0,ipadx=40, ipady=14, sticky='n')
		
		tk.Button(frame_buttons, image=img6, command=lambda :(webview.create_window("A Doll's House", 'https://www.gutenberg.org/files/2542/2542-h/2542-h.htm'),webview.start())).grid(row=2, column=1,pady=30,padx=30, sticky='news')
		tk.Label(frame_buttons, text="A Doll's House\n Stylarten", bg='#262626', fg='white').grid(row=3, column=1,ipadx=45, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=img7, command=lambda :(webview.create_window('The Picture of Dorian Gray', 'https://www.gutenberg.org/files/174/174-h/174-h.htm'),webview.start())).grid(row=2, column=2,pady=30,padx=30, sticky='news')
		tk.Label(frame_buttons, text="The Picture of Dorian Gray", bg='#262626', fg='white').grid(row=3, column=2,ipadx=40, ipady=14, sticky='n')
		
		tk.Button(frame_buttons, image=img8, command=lambda :(webview.create_window('Metamorphosis', 'https://www.gutenberg.org/files/5200/5200-h/5200-h.htm'),webview.start())).grid(row=2, column=3,pady=30,padx=30, sticky='news')
		tk.Label(frame_buttons, text="Metamorphosis", bg='#262626', fg='white').grid(row=3, column=3,ipadx=40, ipady=14, sticky='n')
		
		tk.Button(frame_buttons, image=img9, command=lambda :(webview.create_window('The Adventures of Sherlock Holmes', 'https://www.gutenberg.org/files/1661/1661-h/1661-h.htm'),webview.start())).grid(row=2, column=4,pady=30,padx=30, sticky='news')
		tk.Label(frame_buttons, text="The Adventures of\n Sherlock Holmes", bg='#262626', fg='white').grid(row=3, column=4,ipadx=40, ipady=14, sticky='n')
		
		tk.Button(frame_buttons, image=img10, command=lambda :(webview.create_window('Moby Dick; Or, The Whale', 'Moby'),webview.start())).grid(row=4, column=0,pady=30,padx=30, sticky='news')
		tk.Label(frame_buttons, text="Moby Dick; Or, The Whale", bg='#262626', fg='white').grid(row=5, column=0,ipadx=40, ipady=14, sticky='n')

		
		frame_buttons.update_idletasks()
		canvas.config(scrollregion=canvas.bbox("all"))
		
	home()




	ima1 = ImageTk.PhotoImage(Image.open("img/art/Architektonischen Stylarten.jpg"))
	ima2 = ImageTk.PhotoImage(Image.open("img/art/The stones of Venice.jpg"))
	ima3 = ImageTk.PhotoImage(Image.open("img/art/Constantinople.jpg"))
	ima4 = ImageTk.PhotoImage(Image.open("img/art/Die architektonischen Stylarten.jpg"))
	ima5 = ImageTk.PhotoImage(Image.open("img/art/Die Mode.jpg"))
	ima6 = ImageTk.PhotoImage(Image.open("img/art/The portrait of a lady.jpg"))
	ima7 = ImageTk.PhotoImage(Image.open("img/art/Die Bau- und Kunstdenkmäler des Kreises Münster-Land.jpg"))
	ima8 = ImageTk.PhotoImage(Image.open("img/art/Le château de Pau.jpg"))
	ima9 = ImageTk.PhotoImage(Image.open("img/art/Petits édifices historiques.jpg"))
	ima10 = ImageTk.PhotoImage(Image.open("img/art/Bicknell's village builder.jpg"))
	ima11 = ImageTk.PhotoImage(Image.open("img/art/A short history of japanese architecture.jpg"))
	ima12 = ImageTk.PhotoImage(Image.open("img/art/Official Congressional Director 107th Congress.jpg"))
	ima13 = ImageTk.PhotoImage(Image.open("img/art/The Seven Lamps of Architecture.jpg"))
	ima14 = ImageTk.PhotoImage(Image.open("img/art/The historical growth of the English parish church.jpg"))
	ima15 = ImageTk.PhotoImage(Image.open("img/art/Dublin.jpg"))
	ima16 = ImageTk.PhotoImage(Image.open("img/art/Photography.jpg"))
	ima17 = ImageTk.PhotoImage(Image.open("img/art/Rembrandt.jpg"))
	ima18 = ImageTk.PhotoImage(Image.open("img/art/The vocal preceptor, or, Key to sacred music from celebrated authors.jpg"))
	ima19 = ImageTk.PhotoImage(Image.open("img/art/Poetics.jpg"))
	ima20 = ImageTk.PhotoImage(Image.open("img/art/Essay concerning human understanding.jpg"))



	def art():
		tk.Button(frame_buttons, image=ima1, command=lambda :(webview.create_window("Architektonischen Stylarten", 'https://openlibrary.org/borrow/ia/handbookofarchit00rose?ref=ol'),webview.start())).grid(row=0, column=0,pady=30,padx=30, sticky='news')
		tk.Label(frame_buttons, text="Architektonischen \nStylarten", bg='#262626', fg='white').grid(row=1, column=0,ipadx=40, ipady=14, sticky='n')
		
		tk.Button(frame_buttons, image=ima2, command=lambda :(webview.create_window("The stones of Venice", 'https://openlibrary.org/borrow/ia/stonesofvenice01year1851rusk?ref=ol'),webview.start())).grid(row=0, column=1,pady=30,padx=30, sticky='news')
		tk.Label(frame_buttons, text="The stones of Venice", bg='#262626', fg='white').grid(row=1, column=1,ipadx=40, ipady=14, sticky='n')
		
		tk.Button(frame_buttons, image=ima3, command=lambda :(webview.create_window("Constantinople", 'https://openlibrary.org/borrow/ia/constantinople02grosiala?ref=ol'),webview.start())).grid(row=0, column=2,pady=30,padx=30, sticky='news')
		tk.Label(frame_buttons, text="Constantinople", bg='#262626', fg='white').grid(row=1, column=2,ipadx=45, ipady=14, sticky='n')
		
		tk.Button(frame_buttons, image=ima4, command=lambda :(webview.create_window("Die architektonischen Stylarten", 'https://openlibrary.org/borrow/ia/diearchitektoni00rosegoog?ref=ol'),webview.start())).grid(row=0, column=3,pady=30,padx=30, sticky='news')
		tk.Label(frame_buttons, text="Die Architektonischen\n Stylarten", bg='#262626', fg='white').grid(row=1, column=3,ipadx=40, ipady=14, sticky='n')
		
		tk.Button(frame_buttons, image=ima5, command=lambda :(webview.create_window("Die Mode", 'https://openlibrary.org/borrow/ia/diemodemenschenu00boeh?ref=ol'),webview.start())).grid(row=0, column=4,pady=30,padx=30, sticky='news')
		tk.Label(frame_buttons, text="Die Mode", bg='#262626', fg='white').grid(row=1, column=4,ipadx=50, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=ima6, command=lambda :(webview.create_window("The portrait of a lady", 'https://openlibrary.org/borrow/ia/portraitoflady00jamerich?ref=ol'),webview.start())).grid(row=2, column=0,pady=30,padx=30, sticky='news')
		tk.Label(frame_buttons, text="The portrait of a lady", bg='#262626', fg='white').grid(row=3, column=0,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=ima7, command=lambda :(webview.create_window("Die Bau- und Kunstdenkmäler des Kreises Münster-Land", 'https://openlibrary.org/borrow/ia/diebauundkunstde00ludo_0?ref=ol'),webview.start())).grid(row=2, column=1,pady=30,padx=30, sticky='news')
		tk.Label(frame_buttons, text="Die Bau-und Kunstdenkmäler\n des Kreises Münster-Land", bg='#262626', fg='white').grid(row=3, column=1,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=ima8, command=lambda :(webview.create_window("Le château de Pau", 'https://openlibrary.org/borrow/ia/lechateaudepauhi00lafo?ref=ol'),webview.start())).grid(row=2, column=2,pady=30,padx=30, sticky='news')
		tk.Label(frame_buttons, text="Le château de Pau", bg='#262626', fg='white').grid(row=3, column=2,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=ima9, command=lambda :(webview.create_window("Petits édifices historiques", 'https://openlibrary.org/borrow/ia/petitsedificeshi04ragu?ref=ol'),webview.start())).grid(row=2, column=3,pady=30,padx=30, sticky='news')
		tk.Label(frame_buttons, text="Petits édifices historiques", bg='#262626', fg='white').grid(row=3, column=3,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=ima10, command=lambda :(webview.create_window("Bicknell's village builder", 'https://openlibrary.org/borrow/ia/bicknellsvillage00bick?ref=ol'),webview.start())).grid(row=2, column=4,pady=30,padx=30, sticky='news')
		tk.Label(frame_buttons, text="Bicknell's village builder", bg='#262626', fg='white').grid(row=3, column=4,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=ima11, command=lambda :(webview.create_window("A short history of japanese architecture", 'https://openlibrary.org/borrow/ia/cu31924084250137?ref=ol'),webview.start())).grid(row=4, column=0,pady=30,padx=30, sticky='news')
		tk.Label(frame_buttons, text="A short history of\n japanese architecture", bg='#262626', fg='white').grid(row=5, column=0,ipadx=40, ipady=14, sticky='n')
		
		tk.Button(frame_buttons, image=ima12, command=lambda :(webview.create_window("Official Congressional Director 107th Congress", 'https://openlibrary.org/borrow/ia/officialcongress00join?ref=ol'),webview.start())).grid(row=4, column=1,pady=30,padx=30, sticky='news')
		tk.Label(frame_buttons, text="Official Congressional\n Director 107th Congress", bg='#262626', fg='white').grid(row=5, column=1,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=ima13, command=lambda :(webview.create_window("The Seven Lamps of Architecture", 'https://openlibrary.org/borrow/ia/sevenlampsarchitec00rusk?ref=ol'),webview.start())).grid(row=4, column=2,pady=30,padx=30, sticky='news')
		tk.Label(frame_buttons, text="The Seven Lamps of \nArchitecture", bg='#262626', fg='white').grid(row=5, column=2,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=ima14, command=lambda :(webview.create_window("The historical growth of the English parish church", 'https://openlibrary.org/borrow/ia/historicalgrowth00thomuoft?ref=ol'),webview.start())).grid(row=4, column=3,pady=30,padx=30, sticky='news')
		tk.Label(frame_buttons, text="The historical growth of \nthe English parish church", bg='#262626', fg='white').grid(row=5, column=3,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=ima15, command=lambda :(webview.create_window("Dublin", 'https://openlibrary.org/borrow/ia/dublinhistorical00fitz?ref=ol'),webview.start())).grid(row=4, column=4,pady=30,padx=30, sticky='news')
		tk.Label(frame_buttons, text="Dublin", bg='#262626', fg='white').grid(row=5, column=4,ipadx=50, ipady=25, sticky='n')

		tk.Button(frame_buttons, image=ima16, command=lambda :(webview.create_window("Photography", 'https://openlibrary.org/borrow/ia/photographyitshi00brotuoft?ref=ol'),webview.start())).grid(row=6, column=0,pady=30,padx=30, sticky='news')
		tk.Label(frame_buttons, text="Photography", bg='#262626', fg='white').grid(row=7, column=0,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=ima17, command=lambda :(webview.create_window("Rembrandt", 'https://openlibrary.org/borrow/ia/complete00schi?ref=ol'),webview.start())).grid(row=6, column=1,pady=30,padx=30, sticky='news')
		tk.Label(frame_buttons, text="Rembrandt", bg='#262626', fg='white').grid(row=7, column=1,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=ima18, command=lambda :(webview.create_window("The vocal preceptor, or, Key to sacred music from celebrated authors", 'https://openlibrary.org/borrow/ia/cihm_57310?ref=ol'),webview.start())).grid(row=6, column=2,pady=30,padx=30, sticky='news')
		tk.Label(frame_buttons, text="The vocal preceptor,\n or, Key to sacred music\n from celebrated authors", bg='#262626', fg='white').grid(row=7, column=2,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=ima19, command=lambda :(webview.create_window("Poetics", 'https://openlibrary.org/borrow/ia/aristotlestreati00aris?ref=ol'),webview.start())).grid(row=6, column=3,pady=30,padx=30, sticky='news')
		tk.Label(frame_buttons, text="Poetics", bg='#262626', fg='white').grid(row=7, column=3,ipadx=45, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=ima20, command=lambda :(webview.create_window("Essay concerning human understanding", 'https://openlibrary.org/borrow/ia/concerninghumanu00lockuoft?ref=ol'),webview.start())).grid(row=6, column=4,pady=30,padx=30, sticky='news')
		tk.Label(frame_buttons, text="Essay concerning\n human understanding", bg='#262626', fg='white').grid(row=7, column=4,ipadx=40, ipady=14, sticky='n')


		frame_buttons.update_idletasks()
		canvas.config(scrollregion=canvas.bbox("all"))


		

		
	imb1 = ImageTk.PhotoImage(Image.open("img/fiction/Hamlet.jpg"))
	imb2 = ImageTk.PhotoImage(Image.open("img/fiction/Alice's Adventures in Wonderland.jpg"))
	imb3 = ImageTk.PhotoImage(Image.open("img/fiction/A Midsummer Night's Dream.jpg"))
	imb4 = ImageTk.PhotoImage(Image.open("img/fiction/The Scarlet Letter.jpg"))
	imb5 = ImageTk.PhotoImage(Image.open("img/fiction/Oliver Twist.jpg"))
	imb6 = ImageTk.PhotoImage(Image.open("img/fiction/Dr Jekyll and Mr. Hyde.jpg"))
	imb7 = ImageTk.PhotoImage(Image.open("img/fiction/In a glass darkly.jpg"))
	imb8 = ImageTk.PhotoImage(Image.open("img/fiction/Don Quxite.jpg"))
	imb9 = ImageTk.PhotoImage(Image.open("img/fiction/Gulliver's Travels.jpg"))
	imb10 = ImageTk.PhotoImage(Image.open("img/fiction/Iliad.jpg"))
	imb11 = ImageTk.PhotoImage(Image.open("img/fiction/Odyssey.jpg"))
	imb12 = ImageTk.PhotoImage(Image.open("img/fiction/The golden bough.jpg"))
	imb13 = ImageTk.PhotoImage(Image.open("img/fiction/Macbeth.jpg"))
	imb14 = ImageTk.PhotoImage(Image.open("img/fiction/Adventures of Sherlock Holmes.jpg"))
	imb15 = ImageTk.PhotoImage(Image.open("img/fiction/The Red House Mystery.jpg"))
	imb16 = ImageTk.PhotoImage(Image.open("img/fiction/Poems.jpg"))
	imb17 = ImageTk.PhotoImage(Image.open("img/fiction/Romeo and Juliet.jpg"))
	imb18 = ImageTk.PhotoImage(Image.open("img/fiction/Tempest.jpg"))
	imb19 = ImageTk.PhotoImage(Image.open("img/fiction/Sonnets.jpg"))
	imb20 = ImageTk.PhotoImage(Image.open("img/fiction/Metamorphoses.jpg"))
	def fiction():
		tk.Button(frame_buttons, image=imb1, command=lambda :(webview.create_window("Hamlet", 'https://openlibrary.org/borrow/ia/shakespearestrag00shakesp?ref=ol'),webview.start())).grid(row=0, column=0,pady=30,padx=30, sticky='news')
		tk.Label(frame_buttons, text="Hamlet", bg='#262626', fg='white').grid(row=1, column=0,ipadx=45, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=imb2, command=lambda :(webview.create_window("Alice's Adventures in Wonderland", 'https://openlibrary.org/borrow/ia/alicesadventures00carr_10?ref=ol'),webview.start())).grid(row=0, column=1,pady=30,padx=30, sticky='news')
		tk.Label(frame_buttons, text="Alice's Adventures in\n Wonderland", bg='#262626', fg='white').grid(row=1, column=1,ipadx=40, ipady=14, sticky='n')
		
		tk.Button(frame_buttons, image=imb3, command=lambda :(webview.create_window("A Midsummer Night's Dream", 'https://openlibrary.org/borrow/ia/midsummernightsd00shak_12?ref=ol'),webview.start())).grid(row=0, column=2,pady=30,padx=30, sticky='news')
		tk.Label(frame_buttons, text="A Midsummer Night's Dream", bg='#262626', fg='white').grid(row=1, column=2,ipadx=40, ipady=14, sticky='n')
		
		tk.Button(frame_buttons, image=imb4, command=lambda :(webview.create_window("The Scarlet Letter", 'https://openlibrary.org/borrow/ia/completewritings06hawt?ref=ol'),webview.start())).grid(row=0, column=3,pady=30,padx=30, sticky='news')
		tk.Label(frame_buttons, text="The Scarlet Letter", bg='#262626', fg='white').grid(row=1, column=3,ipadx=40, ipady=14, sticky='n')
		
		tk.Button(frame_buttons, image=imb5, command=lambda :(webview.create_window("Oliver Twist", 'https://openlibrary.org/borrow/ia/olivertwist1900dick?ref=ol'),webview.start())).grid(row=0, column=4,pady=30,padx=30, sticky='news')
		tk.Label(frame_buttons, text="Oliver Twist", bg='#262626', fg='white').grid(row=1, column=4,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=imb6, command=lambda :(webview.create_window("Dr Jekyll and Mr. Hyde", 'https://openlibrary.org/borrow/ia/drjekyllmrhyde00stevuoft?ref=ol'),webview.start())).grid(row=2, column=0,pady=30,padx=30, sticky='news')
		tk.Label(frame_buttons, text="Dr Jekyll and Mr. Hyde", bg='#262626', fg='white').grid(row=3, column=0,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=imb7, command=lambda :(webview.create_window("In a glass darkly", 'https://openlibrary.org/borrow/ia/inglassdarkly02lefa?ref=ol'),webview.start())).grid(row=2, column=1,pady=30,padx=30, sticky='news')
		tk.Label(frame_buttons, text="In a glass darkly", bg='#262626', fg='white').grid(row=3, column=1,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=imb8, command=lambda :(webview.create_window("Don Quxite", 'https://openlibrary.org/borrow/ia/historyofingeni02cerv?ref=ol'),webview.start())).grid(row=2, column=2,pady=30,padx=30, sticky='news')
		tk.Label(frame_buttons, text="Don Quixote", bg='#262626', fg='white').grid(row=3, column=2,ipadx=50, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=imb9, command=lambda :(webview.create_window("Gulliver's Travels", 'https://openlibrary.org/borrow/ia/voyagesdegulliv00swif?ref=ol'),webview.start())).grid(row=2, column=3,pady=30,padx=30, sticky='news')
		tk.Label(frame_buttons, text="Gulliver's Travels", bg='#262626', fg='white').grid(row=3, column=3,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=imb10, command=lambda :(webview.create_window("Iliad", 'https://openlibrary.org/borrow/ia/lailiada00home?ref=ol'),webview.start())).grid(row=2, column=4,pady=30,padx=30, sticky='news')
		tk.Label(frame_buttons, text="Iliad", bg='#262626', fg='white').grid(row=3, column=4,ipadx=50, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=imb11, command=lambda :(webview.create_window("Odyssey", 'https://openlibrary.org/borrow/ia/odysseyhomer00homeiala?ref=ol'),webview.start())).grid(row=4, column=0,pady=30,padx=30, sticky='news')
		tk.Label(frame_buttons, text="Odyssey", bg='#262626', fg='white').grid(row=5, column=0,ipadx=40, ipady=14, sticky='n')
		
		tk.Button(frame_buttons, image=imb12, command=lambda :(webview.create_window("The golden bough", 'https://openlibrary.org/borrow/ia/goldenboughstudy05frazuoft?ref=ol'),webview.start())).grid(row=4, column=1,pady=30,padx=30, sticky='news')
		tk.Label(frame_buttons, text="The golden bough", bg='#262626', fg='white').grid(row=5, column=1,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=imb13, command=lambda :(webview.create_window("Macbeth", 'https://openlibrary.org/borrow/ia/tragedyofmacbeth23shak?ref=ol'),webview.start())).grid(row=4, column=2,pady=30,padx=30, sticky='news')
		tk.Label(frame_buttons, text="Macbeth", bg='#262626', fg='white').grid(row=5, column=2,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=imb14, command=lambda :(webview.create_window("Adventures of Sherlock Holmes", 'https://openlibrary.org/borrow/ia/theadventuresofs01661gut?ref=ol'),webview.start())).grid(row=4, column=3,pady=30,padx=30, sticky='news')
		tk.Label(frame_buttons, text="Adventures of \nSherlock Holmes", bg='#262626', fg='white').grid(row=5, column=3,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=imb15, command=lambda :(webview.create_window("The Red House Mystery", 'https://openlibrary.org/borrow/ia/redhousemystery00milngoog?ref=ol'),webview.start())).grid(row=4, column=4,pady=30,padx=30, sticky='news')
		tk.Label(frame_buttons, text="The Red House Mystery", bg='#262626', fg='white').grid(row=5, column=4,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=imb16, command=lambda :(webview.create_window("Poems", 'https://openlibrary.org/borrow/ia/talesedg00poeerich?ref=ol'),webview.start())).grid(row=6, column=0,pady=30,padx=30, sticky='news')
		tk.Label(frame_buttons, text="Poems", bg='#262626', fg='white').grid(row=7, column=0,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=imb17, command=lambda :(webview.create_window("Romeo and Juliet", 'https://openlibrary.org/borrow/ia/romeojuliettrage00shak?ref=ol'),webview.start())).grid(row=6, column=1,pady=30,padx=30, sticky='news')
		tk.Label(frame_buttons, text="Romeo and Juliet", bg='#262626', fg='white').grid(row=7, column=1,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=imb18, command=lambda :(webview.create_window("Tempest", 'https://openlibrary.org/borrow/ia/in.ernet.dli.2015.202578?ref=ol'),webview.start())).grid(row=6, column=2,pady=30,padx=30, sticky='news')
		tk.Label(frame_buttons, text="Tempest", bg='#262626', fg='white').grid(row=7, column=2,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=imb19, command=lambda :(webview.create_window("Sonnets", 'https://openlibrary.org/borrow/ia/cu31924013143338?ref=ol'),webview.start())).grid(row=6, column=3,pady=30,padx=30, sticky='news')
		tk.Label(frame_buttons, text="Sonnets", bg='#262626', fg='white').grid(row=7, column=3,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=imb20, command=lambda :(webview.create_window("Metamorphoses", 'https://openlibrary.org/borrow/ia/lesmetamorphoses04ovid?ref=ol'),webview.start())).grid(row=6, column=4,pady=30,padx=30, sticky='news')
		tk.Label(frame_buttons, text="Metamorphoses", bg='#262626', fg='white').grid(row=7, column=4,ipadx=40, ipady=14, sticky='n')
		
		frame_buttons.update_idletasks()
		canvas.config(scrollregion=canvas.bbox("all"))
		
		
		
		
	imc1 = ImageTk.PhotoImage(Image.open("img/scimat/Taxonomic literature.jpg"))
	imc2 = ImageTk.PhotoImage(Image.open("img/scimat/On the Nature of the Universe.jpg"))
	imc3 = ImageTk.PhotoImage(Image.open("img/scimat/Biology and its makers.jpg"))
	imc4 = ImageTk.PhotoImage(Image.open("img/scimat/Natural salvation the message of science.jpg"))
	imc5 = ImageTk.PhotoImage(Image.open("img/scimat/Principles of animal biology.jpg"))
	imc6 = ImageTk.PhotoImage(Image.open("img/scimat/The Ontario high school chemistry.jpg"))
	imc7 = ImageTk.PhotoImage(Image.open("img/scimat/High school chemistry consisting of directions for performing a series of experiments with test questions on the experiments and simple problems for investigation.jpg"))
	imc8 = ImageTk.PhotoImage(Image.open("img/scimat/Chemical discovery and invention in the twentieth century.jpg"))
	imc9 = ImageTk.PhotoImage(Image.open("img/scimat/Principles of chemistry, founded on modern theories.jpg"))
	imc10 = ImageTk.PhotoImage(Image.open("img/scimat/Elements.jpg"))
	imc11 = ImageTk.PhotoImage(Image.open("img/scimat/The metaphysical foundations of modern physical science.jpg"))
	imc12 = ImageTk.PhotoImage(Image.open("img/scimat/Philosophiae naturalis principia mathematica.jpg"))
	imc13 = ImageTk.PhotoImage(Image.open("img/scimat/Flatland- A Romance of Many Dimensions.jpg"))
	imc14 = ImageTk.PhotoImage(Image.open("img/scimat/Gillies' arithmetical and miscellaneous tables of decimal currency, weights & measures, &c.jpg"))
	imc15 = ImageTk.PhotoImage(Image.open("img/scimat/The teaching of mathematics in the elementary and the secondary school.jpg"))
	imc16 = ImageTk.PhotoImage(Image.open("img/scimat/Elementary treatise on natural philosophy.jpg"))
	imc17 = ImageTk.PhotoImage(Image.open("img/scimat/Physics.jpg"))
	imc18 = ImageTk.PhotoImage(Image.open("img/scimat/A text-book of physics.jpg"))
	imc19 = ImageTk.PhotoImage(Image.open("img/scimat/Les expériences récréatives, ou, La physique en action.jpg"))
	imc20 = ImageTk.PhotoImage(Image.open("img/scimat/The BASIC Conversions Handbook- for Apple, TRS 80 and Pet Users.jpg"))
	def scimat():
		tk.Button(frame_buttons, image=imc1, command=lambda :(webview.create_window("Taxonomic literature", 'https://openlibrary.org/borrow/ia/taxonomicliteratur00staf?ref=ol'),webview.start())).grid(row=0, column=0,pady=30,padx=30, sticky='news')
		tk.Label(frame_buttons, text="Taxonomic literature", bg='#262626', fg='white').grid(row=1, column=0,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=imc2, command=lambda :(webview.create_window("On the Nature of the Universe", 'https://openlibrary.org/borrow/ia/dererumnaturalib00lucruoft?ref=ol'),webview.start())).grid(row=0, column=1,pady=30,padx=30, sticky='news')
		tk.Label(frame_buttons, text="On the Nature of \nthe Universe", bg='#262626', fg='white').grid(row=1, column=1,ipadx=40, ipady=14, sticky='n')
		
		tk.Button(frame_buttons, image=imc3, command=lambda :(webview.create_window("Biology and its makers", 'https://openlibrary.org/borrow/ia/biologyitsmakers1928locy?ref=ol'),webview.start())).grid(row=0, column=2,pady=30,padx=30, sticky='news')
		tk.Label(frame_buttons, text="Biology and its makers", bg='#262626', fg='white').grid(row=1, column=2,ipadx=40, ipady=14, sticky='n')
		
		tk.Button(frame_buttons, image=imc4, command=lambda :(webview.create_window("Natural salvation: the message of science; outlining the first principles of immortal life on the earth", 'https://openlibrary.org/borrow/ia/cu31924024753471?ref=ol'),webview.start())).grid(row=0, column=3,pady=30,padx=30, sticky='news')
		tk.Label(frame_buttons, text="Natural salvation", bg='#262626', fg='white').grid(row=1, column=3,ipadx=40, ipady=14, sticky='n')
		
		tk.Button(frame_buttons, image=imc5, command=lambda :(webview.create_window("Principles of animal biology", 'https://openlibrary.org/borrow/ia/principlesofanim00shul?ref=ol'),webview.start())).grid(row=0, column=4,pady=30,padx=30, sticky='news')
		tk.Label(frame_buttons, text="Principles of animal\n biology", bg='#262626', fg='white').grid(row=1, column=4,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=imc6, command=lambda :(webview.create_window("The Ontario high school chemistry", 'https://openlibrary.org/borrow/ia/cihm_71468?ref=ol'),webview.start())).grid(row=2, column=0,pady=30,padx=30, sticky='news')
		tk.Label(frame_buttons, text="The Ontario high \nschool chemistry", bg='#262626', fg='white').grid(row=3, column=0,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=imc7, command=lambda :(webview.create_window("High school chemistry: consisting of directions for performing a series of experiments with test questions on the experiments and simple problems for investigation", 'https://openlibrary.org/borrow/ia/highschoolchemwest00knig?ref=ol'),webview.start())).grid(row=2, column=1,pady=30,padx=30, sticky='news')
		tk.Label(frame_buttons, text="High school chemistry", bg='#262626', fg='white').grid(row=3, column=1,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=imc8, command=lambda :(webview.create_window("Chemical discovery and invention in the twentieth century", 'https://openlibrary.org/borrow/ia/chemicaldiscover00tildrich?ref=ol'),webview.start())).grid(row=2, column=2,pady=30,padx=30, sticky='news')
		tk.Label(frame_buttons, text="Chemical discovery \nand invention in the \ntwentieth century", bg='#262626', fg='white').grid(row=3, column=2,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=imc9, command=lambda :(webview.create_window("Principles of chemistry, founded on modern theories", 'https://openlibrary.org/borrow/ia/b21520677?ref=ol'),webview.start())).grid(row=2, column=3,pady=30,padx=30, sticky='news')
		tk.Label(frame_buttons, text="Principles of chemistry,\n founded on modern theories", bg='#262626', fg='white').grid(row=3, column=3,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=imc10, command=lambda :(webview.create_window("Elements", 'https://openlibrary.org/borrow/ia/cihm_59096?ref=ol'),webview.start())).grid(row=2, column=4,pady=30,padx=30, sticky='news')
		tk.Label(frame_buttons, text="Elements", bg='#262626', fg='white').grid(row=3, column=4,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=imc11, command=lambda :(webview.create_window("The metaphysical foundations of modern physical science", 'https://openlibrary.org/borrow/ia/metaphysicalfoun00burtuoft?ref=ol'),webview.start())).grid(row=4, column=0,pady=30,padx=30, sticky='news')
		tk.Label(frame_buttons, text="Metaphysical foundations\n of modern physical science", bg='#262626', fg='white').grid(row=5, column=0,ipadx=40, ipady=14, sticky='n')
		
		tk.Button(frame_buttons, image=imc12, command=lambda :(webview.create_window("Philosophiae naturalis principia mathematica", 'https://openlibrary.org/borrow/ia/philosophiaenatu02newt?ref=ol'),webview.start())).grid(row=4, column=1,pady=30,padx=30, sticky='news')
		tk.Label(frame_buttons, text="Philosophiae naturalis\n principia mathematica", bg='#262626', fg='white').grid(row=5, column=1,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=imc13, command=lambda :(webview.create_window("Flatland- A Romance of Many Dimensions", 'https://openlibrary.org/borrow/ia/flatlandromanceo00abbouoft?ref=ol'),webview.start())).grid(row=4, column=2,pady=30,padx=30, sticky='news')
		tk.Label(frame_buttons, text="Flatland- A Romance of \nMany Dimensions", bg='#262626', fg='white').grid(row=5, column=2,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=imc14, command=lambda :(webview.create_window("Gillies' arithmetical and miscellaneous tables of decimal currency, weights & measures, &c", 'https://openlibrary.org/borrow/ia/gilliesarithmeti00unse?ref=ol'),webview.start())).grid(row=4, column=3,pady=30,padx=30, sticky='news')
		tk.Label(frame_buttons, text="Gillies' arithmetical and \nmiscellaneous tables", bg='#262626', fg='white').grid(row=5, column=3,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=imc15, command=lambda :(webview.create_window("The teaching of mathematics in the elementary and the secondary school", 'https://openlibrary.org/borrow/ia/teachingofmathem00younrich?ref=ol'),webview.start())).grid(row=4, column=4,pady=30,padx=30, sticky='news')
		tk.Label(frame_buttons, text="The teaching of mathematics\n in the elementary and the \nsecondary school", bg='#262626', fg='white').grid(row=5, column=4,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=imc16, command=lambda :(webview.create_window("Elementary treatise on natural philosophy", 'https://openlibrary.org/borrow/ia/treatielementary00privrich?ref=ol'),webview.start())).grid(row=6, column=0,pady=30,padx=30, sticky='news')
		tk.Label(frame_buttons, text="Elementary treatise on\n natural philosophy", bg='#262626', fg='white').grid(row=7, column=0,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=imc17, command=lambda :(webview.create_window("Physics", 'https://openlibrary.org/borrow/ia/in.ernet.dli.2015.183610?ref=ol'),webview.start())).grid(row=6, column=1,pady=30,padx=30, sticky='news')
		tk.Label(frame_buttons, text="Aristotle Physics", bg='#262626', fg='white').grid(row=7, column=1,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=imc18, command=lambda :(webview.create_window("A text-book of physics", 'https://openlibrary.org/borrow/ia/textbookofphysic00duffuoft?ref=ol'),webview.start())).grid(row=6, column=2,pady=30,padx=30, sticky='news')
		tk.Label(frame_buttons, text="A text-book of physics", bg='#262626', fg='white').grid(row=7, column=2,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=imc19, command=lambda :(webview.create_window("Les expériences récréatives, ou, La physique en action", 'https://openlibrary.org/borrow/ia/lesexperiencesre00cast?ref=ol'),webview.start())).grid(row=6, column=3,pady=30,padx=30, sticky='news')
		tk.Label(frame_buttons, text="Les expériences récréatives,\n ou, La physique en action", bg='#262626', fg='white').grid(row=7, column=3,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=imc20, command=lambda :(webview.create_window("The BASIC Conversions Handbook: for Apple, TRS 80 and Pet Users", 'https://openlibrary.org/borrow/ia/brain-bank-1981-basic-conversions-handbook?ref=ol'),webview.start())).grid(row=6, column=4,pady=30,padx=30, sticky='news')
		tk.Label(frame_buttons, text="The BASIC Conversions \nHandbook: for Apple, TRS 80\n and Pet Users", bg='#262626', fg='white').grid(row=7, column=4,ipadx=40, ipady=14, sticky='n')
		frame_buttons.update_idletasks()
		canvas.config(scrollregion=canvas.bbox("all"))
		
		
		
	imd1 = ImageTk.PhotoImage(Image.open("img/busifi/Roughing It.jpg"))
	imd2 = ImageTk.PhotoImage(Image.open("img/busifi/The Wealth of Nations.jpg"))
	imd3 = ImageTk.PhotoImage(Image.open("img/busifi/A Backward Glance at Eighty.jpg"))
	imd4 = ImageTk.PhotoImage(Image.open("img/busifi/Sixteenth census of the United States 1940.jpg"))
	imd5 = ImageTk.PhotoImage(Image.open("img/busifi/Men and memories of San Francisco, in the spring of 50.jpg"))
	imd6 = ImageTk.PhotoImage(Image.open("img/busifi/Price maintenance.jpg"))
	imd7 = ImageTk.PhotoImage(Image.open("img/busifi/First lessons in business.jpg"))
	imd8 = ImageTk.PhotoImage(Image.open("img/busifi/Business--a profession.jpg"))
	imd9 = ImageTk.PhotoImage(Image.open("img/busifi/Small talk about business.jpg"))
	imd10 = ImageTk.PhotoImage(Image.open("img/busifi/Organizing for increased business.jpg"))
	imd11 = ImageTk.PhotoImage(Image.open("img/busifi/Applied office practice.jpg"))
	imd12 = ImageTk.PhotoImage(Image.open("img/busifi/Putnam's handbook of buying and selling.jpg"))
	imd13 = ImageTk.PhotoImage(Image.open("img/busifi/Recollections of a newspaperman.jpg"))
	imd14 = ImageTk.PhotoImage(Image.open("img/busifi/Reminiscences of a Ranger.jpg"))
	imd15 = ImageTk.PhotoImage(Image.open("img/busifi/The theory of the leisure class.jpg"))
	imd16 = ImageTk.PhotoImage(Image.open("img/busifi/How to make a living.jpg"))
	imd17 = ImageTk.PhotoImage(Image.open("img/busifi/Making a Business Woman.jpg"))
	imd18 = ImageTk.PhotoImage(Image.open("img/busifi/A practical treatise on business.jpg"))
	imd19 = ImageTk.PhotoImage(Image.open("img/busifi/Census of business 1935.jpg"))
	imd20 = ImageTk.PhotoImage(Image.open("img/busifi/Efficiency as a basis for operation and wages.jpg"))
	def busifi():
		tk.Button(frame_buttons, image=imd1, command=lambda :(webview.create_window("Roughing It", 'https://openlibrary.org/borrow/ia/roughingit1913twai?ref=ol'),webview.start())).grid(row=0, column=0,pady=32,padx=32, sticky='news')
		tk.Label(frame_buttons, text="Roughing It", bg='#262626', fg='white').grid(row=1, column=0,ipadx=45, ipady=14, sticky='n')
		
		tk.Button(frame_buttons, image=imd2, command=lambda :(webview.create_window("The Wealth of Nations", 'https://openlibrary.org/borrow/ia/inquiryintonatur03smituoft?ref=ol'),webview.start())).grid(row=0, column=1,pady=32,padx=32, sticky='news')
		tk.Label(frame_buttons, text="The Wealth of Nations", bg='#262626', fg='white').grid(row=1, column=1,ipadx=40, ipady=14, sticky='n')
	    
		tk.Button(frame_buttons, image=imd3, command=lambda :(webview.create_window("A Backward Glance at Eighty", 'https://openlibrary.org/borrow/ia/abackwardglance00murdgoog?ref=ol'),webview.start())).grid(row=0, column=2,pady=32,padx=32, sticky='news')
		tk.Label(frame_buttons, text="A Backward Glance \nat Eighty", bg='#262626', fg='white').grid(row=1, column=2,ipadx=40, ipady=14, sticky='n')
	    
		tk.Button(frame_buttons, image=imd4, command=lambda :(webview.create_window("Sixteenth census of the United States 1940", 'https://openlibrary.org/borrow/ia/sixteenthcensuso00unit?ref=ol'),webview.start())).grid(row=0, column=3,pady=32,padx=32, sticky='news')
		tk.Label(frame_buttons, text="Sixteenth census of \nthe United States 1940", bg='#262626', fg='white').grid(row=1, column=3,ipadx=40, ipady=14, sticky='n')
	    
		tk.Button(frame_buttons, image=imd5, command=lambda :(webview.create_window("Men and memories of San Francisco, in the spring of 50", 'https://openlibrary.org/borrow/ia/cu31924097557015?ref=ol'),webview.start())).grid(row=0, column=4,pady=32,padx=32, sticky='news')
		tk.Label(frame_buttons, text="Men and memories\n of San Francisco, in\n the spring of 50", bg='#262626', fg='white').grid(row=1, column=4,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=imd6, command=lambda :(webview.create_window("Price maintenance", 'https://openlibrary.org/borrow/ia/pricemaintenance00fernuoft?ref=ol'),webview.start())).grid(row=2, column=0,pady=32,padx=32, sticky='news')
		tk.Label(frame_buttons, text="Price maintenance", bg='#262626', fg='white').grid(row=3, column=0,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=imd7, command=lambda :(webview.create_window("First lessons in business", 'https://openlibrary.org/borrow/ia/firstlessonsinb00hubbgoog?ref=ol'),webview.start())).grid(row=2, column=1,pady=32,padx=32, sticky='news')
		tk.Label(frame_buttons, text="First lessons in \nbusiness", bg='#262626', fg='white').grid(row=3, column=1,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=imd8, command=lambda :(webview.create_window("Business--a profession", 'https://openlibrary.org/borrow/ia/businessaprofess00bran?ref=ol'),webview.start())).grid(row=2, column=2,pady=32,padx=32, sticky='news')
		tk.Label(frame_buttons, text="Business--a profession", bg='#262626', fg='white').grid(row=3, column=2,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=imd9, command=lambda :(webview.create_window("Small talk about business", 'https://openlibrary.org/borrow/ia/smalltalkaboutb00ricegoog?ref=ol'),webview.start())).grid(row=2, column=3,pady=32,padx=32, sticky='news')
		tk.Label(frame_buttons, text="Small talk about business", bg='#262626', fg='white').grid(row=3, column=3,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=imd10, command=lambda :(webview.create_window("Organizing for increased business", 'https://openlibrary.org/borrow/ia/organizingforinc00shawrich?ref=ol'),webview.start())).grid(row=2, column=4,pady=32,padx=32, sticky='news')
		tk.Label(frame_buttons, text="Organizing for \nincreased business", bg='#262626', fg='white').grid(row=3, column=4,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=imd11, command=lambda :(webview.create_window("Applied office practice", 'https://openlibrary.org/borrow/ia/appliedofficepra00morr?ref=ol'),webview.start())).grid(row=4, column=0,pady=32,padx=32, sticky='news')
		tk.Label(frame_buttons, text="Applied office \npractice", bg='#262626', fg='white').grid(row=5, column=0,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=imd12, command=lambda :(webview.create_window("Putnam's handbook of buying and selling", 'https://openlibrary.org/borrow/ia/cu31924013909092?ref=ol'),webview.start())).grid(row=4, column=1,pady=32,padx=32, sticky='news')
		tk.Label(frame_buttons, text="Putnam's handbook of \nbuying and selling", bg='#262626', fg='white').grid(row=5, column=1,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=imd13, command=lambda :(webview.create_window("Recollections of a newspaperman", 'https://openlibrary.org/borrow/ia/recollectionsofn00leacuoft?ref=ol'),webview.start())).grid(row=4, column=2,pady=32,padx=32, sticky='news')
		tk.Label(frame_buttons, text="Recollections of a \nnewspaperman", bg='#262626', fg='white').grid(row=5, column=2,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=imd14, command=lambda :(webview.create_window("Reminiscences of a Ranger", 'https://openlibrary.org/borrow/ia/reminiscencesofr00bellrich?ref=ol'),webview.start())).grid(row=4, column=3,pady=32,padx=32, sticky='news')
		tk.Label(frame_buttons, text="Reminiscences of a \nRanger", bg='#262626', fg='white').grid(row=5, column=3,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=imd15, command=lambda :(webview.create_window("The theory of the leisure class", 'https://openlibrary.org/borrow/ia/theoryofleisurec01vebl?ref=ol'),webview.start())).grid(row=4, column=4,pady=32,padx=32, sticky='news')
		tk.Label(frame_buttons, text="The theory of the l\neisure class", bg='#262626', fg='white').grid(row=5, column=4,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=imd16, command=lambda :(webview.create_window("How to make a living", 'https://openlibrary.org/borrow/ia/howtomakelivinga00eggl?ref=ol'),webview.start())).grid(row=6, column=0,pady=32,padx=32, sticky='news')
		tk.Label(frame_buttons, text="How to make a living", bg='#262626', fg='white').grid(row=7, column=0,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=imd17, command=lambda :(webview.create_window("Making a Business Woman", 'https://openlibrary.org/borrow/ia/makingabusiness00monrgoog?ref=ol'),webview.start())).grid(row=6, column=1,pady=32,padx=32, sticky='news')
		tk.Label(frame_buttons, text="Making a Business Woman", bg='#262626', fg='white').grid(row=7, column=1,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=imd18, command=lambda :(webview.create_window("A practical treatise on business", 'https://openlibrary.org/borrow/ia/practicaltreatis00freerich?ref=ol'),webview.start())).grid(row=6, column=2,pady=32,padx=32, sticky='news')
		tk.Label(frame_buttons, text="A practical treatise\n on business", bg='#262626', fg='white').grid(row=7, column=2,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=imd19, command=lambda :(webview.create_window("Census of business 1935", 'https://openlibrary.org/borrow/ia/censusofbusiness340unit?ref=ol'),webview.start())).grid(row=6, column=3,pady=32,padx=32, sticky='news')
		tk.Label(frame_buttons, text="Census of business 1935", bg='#262626', fg='white').grid(row=7, column=3,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=imd20, command=lambda :(webview.create_window("Efficiency as a basis for operation and wages", 'https://openlibrary.org/borrow/ia/efficiencyasbasi00emerrich?ref=ol'),webview.start())).grid(row=6, column=4,pady=32,padx=32, sticky='news')
		tk.Label(frame_buttons, text="Efficiency as a basis\n for operation and wages", bg='#262626', fg='white').grid(row=7, column=4,ipadx=40, ipady=14, sticky='n')
								


		frame_buttons.update_idletasks()
		canvas.config(scrollregion=canvas.bbox("all"))
		
		
		
	ime1 = ImageTk.PhotoImage(Image.open("img/kids/Macbeth.jpg"))
	ime2 = ImageTk.PhotoImage(Image.open("img/kids/The Adventures of Tom Sawyer.jpg"))
	ime3 = ImageTk.PhotoImage(Image.open("img/kids/Little Women.jpg"))
	ime4 = ImageTk.PhotoImage(Image.open("img/kids/Oliver Twist.jpg"))
	ime5 = ImageTk.PhotoImage(Image.open("img/kids/David Copperfield.jpg"))
	ime6 = ImageTk.PhotoImage(Image.open("img/kids/A child's garden of verses.jpg"))
	ime7 = ImageTk.PhotoImage(Image.open("img/kids/The Wonderful Wizard of Oz.jpg"))
	ime8 = ImageTk.PhotoImage(Image.open("img/kids/Therapeutics Of Infancy And Childhood.jpg"))
	ime9 = ImageTk.PhotoImage(Image.open("img/kids/Domestic medicine.jpg"))
	ime10 = ImageTk.PhotoImage(Image.open("img/kids/Little Men.jpg"))
	ime11 = ImageTk.PhotoImage(Image.open("img/kids/My little primer.jpg"))
	ime12 = ImageTk.PhotoImage(Image.open("img/kids/The intestinal diseases of infancy and childhood.jpg"))
	ime13 = ImageTk.PhotoImage(Image.open("img/kids/Hygiene for young people.jpg"))
	ime14 = ImageTk.PhotoImage(Image.open("img/kids/The Ontario public school hygiene.jpg"))
	ime15 = ImageTk.PhotoImage(Image.open("img/kids/The town child.jpg"))
	ime16 = ImageTk.PhotoImage(Image.open("img/kids/All aboard for the lakes and mountains.jpg"))
	ime17 = ImageTk.PhotoImage(Image.open("img/kids/A bibliography of American children's books printed prior to 1821.jpg"))
	ime18 = ImageTk.PhotoImage(Image.open("img/kids/Somerville, past and present.jpg"))
	ime19 = ImageTk.PhotoImage(Image.open("img/kids/Medical inspection of schools and school children.jpg"))
	ime20 = ImageTk.PhotoImage(Image.open("img/kids/Principles of teaching.jpg"))
	def kids():
		tk.Button(frame_buttons, image=ime1, command=lambda :(webview.create_window("Macbeth", 'https://openlibrary.org/borrow/ia/tragedyofmacbeth23shak?ref=ol'),webview.start())).grid(row=0, column=0,pady=32,padx=32, sticky='news')
		tk.Label(frame_buttons, text="Macbeth", bg='#262626', fg='white').grid(row=1, column=0,ipadx=45, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=ime2, command=lambda :(webview.create_window("The Adventures of Tom Sawyer", 'https://openlibrary.org/borrow/ia/adventuresoftoms99twai?ref=ol'),webview.start())).grid(row=0, column=1,pady=32,padx=32, sticky='news')
		tk.Label(frame_buttons, text="The Adventures of \nTom Sawyer", bg='#262626', fg='white').grid(row=1, column=1,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=ime3, command=lambda :(webview.create_window("Little Women", 'https://openlibrary.org/borrow/ia/littlewomen00alcoiala?ref=ol'),webview.start())).grid(row=0, column=2,pady=32,padx=32, sticky='news')
		tk.Label(frame_buttons, text="Little Women", bg='#262626', fg='white').grid(row=1, column=2,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=ime4, command=lambda :(webview.create_window("Oliver Twist", 'https://openlibrary.org/borrow/ia/olivertwist1900dick?ref=ol'),webview.start())).grid(row=0, column=3,pady=32,padx=32, sticky='news')
		tk.Label(frame_buttons, text="Oliver Twist", bg='#262626', fg='white').grid(row=1, column=3,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=ime5, command=lambda :(webview.create_window("David Copperfield", 'https://openlibrary.org/borrow/ia/personalhistoryo001850dick?ref=ol'),webview.start())).grid(row=0, column=4,pady=32,padx=32, sticky='news')
		tk.Label(frame_buttons, text="David Copperfield", bg='#262626', fg='white').grid(row=1, column=4,ipadx=40, ipady=23, sticky='n')

		tk.Button(frame_buttons, image=ime6, command=lambda :(webview.create_window("A child's garden of verses", 'https://openlibrary.org/borrow/ia/childsgardenofve00stevuoft?ref=ol'),webview.start())).grid(row=2, column=0,pady=32,padx=32, sticky='news')
		tk.Label(frame_buttons, text="A child's garden\n of verses", bg='#262626', fg='white').grid(row=3, column=0,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=ime7, command=lambda :(webview.create_window("The Wonderful Wizard of Oz", 'https://openlibrary.org/borrow/ia/wonderfulwizardo00baumiala?ref=ol'),webview.start())).grid(row=2, column=1,pady=32,padx=32, sticky='news')
		tk.Label(frame_buttons, text="The Wonderful Wizard\n of Oz", bg='#262626', fg='white').grid(row=3, column=1,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=ime8, command=lambda :(webview.create_window("Therapeutics Of Infancy And Childhood", 'https://openlibrary.org/borrow/ia/therapeuticsofin00jacouoft?ref=ol'),webview.start())).grid(row=2, column=2,pady=32,padx=32, sticky='news')
		tk.Label(frame_buttons, text="Therapeutics Of Infancy\n And Childhood", bg='#262626', fg='white').grid(row=3, column=2,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=ime9, command=lambda :(webview.create_window("Domestic medicine", 'https://openlibrary.org/borrow/ia/domesticmedicine00buchuoft?ref=ol'),webview.start())).grid(row=2, column=3,pady=32,padx=32, sticky='news')
		tk.Label(frame_buttons, text="Domestic medicine", bg='#262626', fg='white').grid(row=3, column=3,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=ime10, command=lambda :(webview.create_window("Little Men", 'https://openlibrary.org/borrow/ia/littlemenalco00alco?ref=ol'),webview.start())).grid(row=2, column=4,pady=32,padx=32, sticky='news')
		tk.Label(frame_buttons, text="Little Men", bg='#262626', fg='white').grid(row=3, column=4,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=ime11, command=lambda :(webview.create_window("My little primer", 'https://openlibrary.org/borrow/ia/mylittleprimerwi00eaen?ref=ol'),webview.start())).grid(row=4, column=0,pady=32,padx=32, sticky='news')
		tk.Label(frame_buttons, text="My little primer", bg='#262626', fg='white').grid(row=5, column=0,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=ime12, command=lambda :(webview.create_window("The intestinal diseases of infancy and childhood", 'https://openlibrary.org/borrow/ia/intestinaldiseas00jacouoft?ref=ol'),webview.start())).grid(row=4, column=1,pady=32,padx=32, sticky='news')
		tk.Label(frame_buttons, text="The intestinal diseases\n of infancy and childhood", bg='#262626', fg='white').grid(row=5, column=1,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=ime13, command=lambda :(webview.create_window("Hygiene for young people", 'https://openlibrary.org/borrow/ia/hygieneforyowest00knig?ref=ol'),webview.start())).grid(row=4, column=2,pady=32,padx=32, sticky='news')
		tk.Label(frame_buttons, text="Hygiene for young people", bg='#262626', fg='white').grid(row=5, column=2,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=ime14, command=lambda :(webview.create_window("The Ontario public school hygiene", 'https://openlibrary.org/borrow/ia/ontariopub20west00kniguoft?ref=ol'),webview.start())).grid(row=4, column=3,pady=32,padx=32, sticky='news')
		tk.Label(frame_buttons, text="The Ontario public\n school hygiene", bg='#262626', fg='white').grid(row=5, column=3,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=ime15, command=lambda :(webview.create_window("The town child", 'https://openlibrary.org/borrow/ia/townchild00brayuoft?ref=ol'),webview.start())).grid(row=4, column=4,pady=32,padx=32, sticky='news')
		tk.Label(frame_buttons, text="The town child", bg='#262626', fg='white').grid(row=5, column=4,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=ime16, command=lambda :(webview.create_window("All aboard for the lakes and mountains", 'https://openlibrary.org/borrow/ia/allaboardforlake00rand?ref=ol'),webview.start())).grid(row=6, column=0,pady=32,padx=32, sticky='news')
		tk.Label(frame_buttons, text="All aboard for the\n lakes and mountains", bg='#262626', fg='white').grid(row=7, column=0,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=ime17, command=lambda :(webview.create_window("A bibliography of American children's books printed prior to 1821", 'https://openlibrary.org/borrow/ia/bibliographyofam00welc?ref=ol'),webview.start())).grid(row=6, column=1,pady=32,padx=32, sticky='news')
		tk.Label(frame_buttons, text="A bibliography of American\n children's books printed\n prior to 1821", bg='#262626', fg='white').grid(row=7, column=1,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=ime18, command=lambda :(webview.create_window("Somerville, past and present", 'https://openlibrary.org/borrow/ia/somervillepast00samu?ref=ol'),webview.start())).grid(row=6, column=2,pady=32,padx=32, sticky='news')
		tk.Label(frame_buttons, text="Somerville, past and present", bg='#262626', fg='white').grid(row=7, column=2,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=ime19, command=lambda :(webview.create_window("Medical inspection of schools and school children", 'https://openlibrary.org/borrow/ia/medicalinspectio00ferr?ref=ol'),webview.start())).grid(row=6, column=3,pady=32,padx=32, sticky='news')
		tk.Label(frame_buttons, text="Medical inspection of\n schools and school children", bg='#262626', fg='white').grid(row=7, column=3,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=ime20, command=lambda :(webview.create_window("Principles of teaching", 'https://openlibrary.org/borrow/ia/principlesofteac00harvuoft?ref=ol'),webview.start())).grid(row=6, column=4,pady=32,padx=32, sticky='news')
		tk.Label(frame_buttons, text="Principles of teaching", bg='#262626', fg='white').grid(row=7, column=4,ipadx=40, ipady=14, sticky='n')

		frame_buttons.update_idletasks()
		canvas.config(scrollregion=canvas.bbox("all"))
		
		
		
	imf1 = ImageTk.PhotoImage(Image.open("img/history/Don Quxite.jpg"))
	imf2 = ImageTk.PhotoImage(Image.open("img/history/Pride and Prejudice.jpg"))
	imf3 = ImageTk.PhotoImage(Image.open("img/history/Book of common prayer.jpg"))
	imf4 = ImageTk.PhotoImage(Image.open("img/history/The Merchant of Venice.jpg"))
	imf5 = ImageTk.PhotoImage(Image.open("img/history/The Adventures of Tom Sawyer.jpg"))
	imf6 = ImageTk.PhotoImage(Image.open("img/history/Ab Urbe Condita Libri.jpg"))
	imf7 = ImageTk.PhotoImage(Image.open("img/history/Candide.jpg"))
	imf8 = ImageTk.PhotoImage(Image.open("img/history/Robinson Crusoe.jpg"))
	imf9 = ImageTk.PhotoImage(Image.open("img/history/The Divine Comedy.jpg"))
	imf10 = ImageTk.PhotoImage(Image.open("img/history/King Henry V.jpg"))
	imf11 = ImageTk.PhotoImage(Image.open("img/history/The Aeneid.jpg"))
	imf12 = ImageTk.PhotoImage(Image.open("img/history/Madame Bovary.jpg"))
	imf13 = ImageTk.PhotoImage(Image.open("img/history/The Scarlet Letter.jpg"))
	imf14 = ImageTk.PhotoImage(Image.open("img/history/King Henry IV. Part 1.jpg"))
	imf15 = ImageTk.PhotoImage(Image.open("img/history/Jane Eyre.jpg"))
	imf16 = ImageTk.PhotoImage(Image.open("img/history/On the Nature of the Universe.jpg"))
	imf17 = ImageTk.PhotoImage(Image.open("img/history/Antony and Cleopatra.jpg"))
	imf18 = ImageTk.PhotoImage(Image.open("img/history/The Call of the Wild.jpg"))
	imf19 = ImageTk.PhotoImage(Image.open("img/history/The Secret Garden.jpg"))
	imf20 = ImageTk.PhotoImage(Image.open("img/history/Oliver Twist.jpg"))
	def history():
		tk.Button(frame_buttons, image=imf1, command=lambda :(webview.create_window("Don Quxite", 'https://openlibrary.org/borrow/ia/historyofingeni02cerv?ref=ol'),webview.start())).grid(row=0, column=0,pady=32,padx=32, sticky='news')
		tk.Label(frame_buttons, text="Don Quixote", bg='#262626', fg='white').grid(row=1, column=0,ipadx=45, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=imf2, command=lambda :(webview.create_window("Pride and Prejudice", 'https://openlibrary.org/borrow/ia/in.ernet.dli.2015.46179?ref=ol'),webview.start())).grid(row=0, column=1,pady=32,padx=32, sticky='news')
		tk.Label(frame_buttons, text="Pride and Prejudice", bg='#262626', fg='white').grid(row=1, column=1,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=imf3, command=lambda :(webview.create_window("Book of common prayer", 'https://openlibrary.org/borrow/ia/firstprayerbooko00churiala?ref=ol'),webview.start())).grid(row=0, column=2,pady=32,padx=32, sticky='news')
		tk.Label(frame_buttons, text="Book of common prayer", bg='#262626', fg='white').grid(row=1, column=2,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=imf4, command=lambda :(webview.create_window("The Merchant of Venice", 'https://openlibrary.org/borrow/ia/merchantofvenice0000shak_w7v4?ref=ol'),webview.start())).grid(row=0, column=3,pady=32,padx=32, sticky='news')
		tk.Label(frame_buttons, text="The Merchant of Venice", bg='#262626', fg='white').grid(row=1, column=3,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=imf5, command=lambda :(webview.create_window("The Adventures of Tom Sawyer", 'https://openlibrary.org/borrow/ia/adventuresoftoms99twai?ref=ol'),webview.start())).grid(row=0, column=4,pady=32,padx=32, sticky='news')
		tk.Label(frame_buttons, text="The Adventures of \nTom Sawyer", bg='#262626', fg='white').grid(row=1, column=4,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=imf6, command=lambda :(webview.create_window("Ab Urbe Condita Libri", 'https://openlibrary.org/borrow/ia/booksvvivii02livy?ref=ol'),webview.start())).grid(row=2, column=0,pady=32,padx=32, sticky='news')
		tk.Label(frame_buttons, text="Ab Urbe Condita Libri", bg='#262626', fg='white').grid(row=3, column=0,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=imf7, command=lambda :(webview.create_window("Candide", 'https://openlibrary.org/borrow/ia/candideorallfort00voltuoft?ref=ol'),webview.start())).grid(row=2, column=1,pady=32,padx=32, sticky='news')
		tk.Label(frame_buttons, text="Candide", bg='#262626', fg='white').grid(row=3, column=1,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=imf8, command=lambda :(webview.create_window("Robinson Crusoe", 'https://openlibrary.org/borrow/ia/wonderfullifesur00defo?ref=ol'),webview.start())).grid(row=2, column=2,pady=32,padx=32, sticky='news')
		tk.Label(frame_buttons, text="Robinson Crusoe", bg='#262626', fg='white').grid(row=3, column=2,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=imf9, command=lambda :(webview.create_window("The Divine Comedy", 'https://openlibrary.org/borrow/ia/divinecomedyofda00dantiala?ref=ol'),webview.start())).grid(row=2, column=3,pady=32,padx=32, sticky='news')
		tk.Label(frame_buttons, text="The Divine Comedy", bg='#262626', fg='white').grid(row=3, column=3,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=imf10, command=lambda :(webview.create_window("King Henry V", 'https://openlibrary.org/borrow/ia/henryfifthhistor00shak?ref=ol'),webview.start())).grid(row=2, column=4,pady=32,padx=32, sticky='news')
		tk.Label(frame_buttons, text="King Henry V", bg='#262626', fg='white').grid(row=3, column=4,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=imf11, command=lambda :(webview.create_window("The Aeneid", 'https://openlibrary.org/borrow/ia/aeneidosliberxi00virguoft?ref=ol'),webview.start())).grid(row=4, column=0,pady=32,padx=32, sticky='news')
		tk.Label(frame_buttons, text="The Aeneid", bg='#262626', fg='white').grid(row=5, column=0,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=imf12, command=lambda :(webview.create_window("Madame Bovary", 'https://openlibrary.org/borrow/ia/dli.ernet.544206?ref=ol'),webview.start())).grid(row=4, column=1,pady=32,padx=32, sticky='news')
		tk.Label(frame_buttons, text="Madame Bovary", bg='#262626', fg='white').grid(row=5, column=1,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=imf13, command=lambda :(webview.create_window("The Scarlet Letter", 'https://openlibrary.org/borrow/ia/completewritings06hawt?ref=ol'),webview.start())).grid(row=4, column=2,pady=32,padx=32, sticky='news')
		tk.Label(frame_buttons, text="The Scarlet Letter", bg='#262626', fg='white').grid(row=5, column=2,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=imf14, command=lambda :(webview.create_window("King Henry IV. Part 1", 'https://openlibrary.org/borrow/ia/firstpartofshake00shak?ref=ol'),webview.start())).grid(row=4, column=3,pady=32,padx=32, sticky='news')
		tk.Label(frame_buttons, text="King Henry IV.\n Part 1", bg='#262626', fg='white').grid(row=5, column=3,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=imf15, command=lambda :(webview.create_window("Jane Eyre", 'https://openlibrary.org/borrow/ia/janeeyrewithintr01bronuoft?ref=ol'),webview.start())).grid(row=4, column=4,pady=32,padx=32, sticky='news')
		tk.Label(frame_buttons, text="Jane Eyre", bg='#262626', fg='white').grid(row=5, column=4,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=imf16, command=lambda :(webview.create_window("On the Nature of the Universe", 'https://openlibrary.org/borrow/ia/dererumnaturalib00lucruoft?ref=ol'),webview.start())).grid(row=6, column=0,pady=32,padx=32, sticky='news')
		tk.Label(frame_buttons, text="On the Nature of the \nUniverse", bg='#262626', fg='white').grid(row=7, column=0,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=imf17, command=lambda :(webview.create_window("Antony and Cleopatra", 'https://openlibrary.org/borrow/ia/antoniusjacleopa16618gut?ref=ol'),webview.start())).grid(row=6, column=1,pady=32,padx=32, sticky='news')
		tk.Label(frame_buttons, text="Antony and Cleopatra", bg='#262626', fg='white').grid(row=7, column=1,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=imf18, command=lambda :(webview.create_window("The Call of the Wild", 'https://openlibrary.org/borrow/ia/callofthewild00lond?ref=ol'),webview.start())).grid(row=6, column=2,pady=32,padx=32, sticky='news')
		tk.Label(frame_buttons, text="The Call of the Wild", bg='#262626', fg='white').grid(row=7, column=2,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=imf19, command=lambda :(webview.create_window("The Secret Garden", 'https://openlibrary.org/borrow/ia/secretgarden00burn?ref=ol'),webview.start())).grid(row=6, column=3,pady=32,padx=32, sticky='news')
		tk.Label(frame_buttons, text="The Secret Garden", bg='#262626', fg='white').grid(row=7, column=3,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=imf20, command=lambda :(webview.create_window("Oliver Twist", 'https://openlibrary.org/borrow/ia/olivertwist1900dick?ref=ol'),webview.start())).grid(row=6, column=4,pady=32,padx=32, sticky='news')
		tk.Label(frame_buttons, text="Oliver Twist", bg='#262626', fg='white').grid(row=7, column=4,ipadx=40, ipady=14, sticky='n')

		frame_buttons.update_idletasks()
		canvas.config(scrollregion=canvas.bbox("all"))
		
		
	imj1 = ImageTk.PhotoImage(Image.open("img/health/A Mind That Found Itself.jpg"))
	imj2 = ImageTk.PhotoImage(Image.open("img/health/Science And Health.jpg"))
	imj3= ImageTk.PhotoImage(Image.open("img/health/Health And Education.jpg"))
	imj4 = ImageTk.PhotoImage(Image.open("img/health/The Care And Feeding Of Childern.jpg"))
	imj5= ImageTk.PhotoImage(Image.open("img/health/Strength : A treatise on the development and use of muscle.jpg"))
	imj6= ImageTk.PhotoImage(Image.open("img/health/Anatomy Of Melancholy.jpg"))
	imj7= ImageTk.PhotoImage(Image.open("img/health/Power Through Repose.jpg"))
	imj8= ImageTk.PhotoImage(Image.open("img/health/Codex Alimentarius.jpg"))
	imj9= ImageTk.PhotoImage(Image.open("img/health/Doyle Drive.jpg"))
	imj10= ImageTk.PhotoImage(Image.open("img/health/Golden Bough.jpg"))
	imj11= ImageTk.PhotoImage(Image.open("img/health/History Of The Hebrew Commonwealth.jpg"))
	imj12= ImageTk.PhotoImage(Image.open("img/health/The Implications Of Medical Technology.jpg"))
	imj13= ImageTk.PhotoImage(Image.open("img/health/Health Care Reform.jpg"))
	imj14= ImageTk.PhotoImage(Image.open("img/health/Tokology.jpg"))
	imj15= ImageTk.PhotoImage(Image.open("img/health/The Evolution Of Public Health.jpg"))
	imj16= ImageTk.PhotoImage(Image.open("img/health/Our Seamen.jpg"))
	imj17= ImageTk.PhotoImage(Image.open("img/health/Plain Facts About Sexual Life.jpg"))
	imj18= ImageTk.PhotoImage(Image.open("img/health/What A Man Of Forty-Five Ought to Know.jpg"))
	imj19= ImageTk.PhotoImage(Image.open("img/health/Dental Formulary.jpg"))

	def health():
		tk.Button(frame_buttons, image=imj1, command=lambda :(webview.create_window("A Mind That Found Itself", 'https://openlibrary.org/borrow/ia/mindthatfoundits00beeruoft?ref=ol'),webview.start())).grid(row=0, column=0,pady=32,padx=32, sticky='news')
		tk.Label(frame_buttons, text="A Mind That Found Itself", bg='#262626', fg='white').grid(row=1, column=0,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=imj2, command=lambda :(webview.create_window("Science And Health", 'https://openlibrary.org/borrow/ia/sciencehealthwi000eddy?ref=ol'),webview.start())).grid(row=0, column=1,pady=32,padx=32, sticky='news')
		tk.Label(frame_buttons, text="Science And Health", bg='#262626', fg='white').grid(row=1, column=1,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=imj3, command=lambda :(webview.create_window("Health And Education", 'https://openlibrary.org/borrow/ia/healthandeducat00kinggoog?ref=ol'),webview.start())).grid(row=0, column=2,pady=32,padx=32, sticky='news')
		tk.Label(frame_buttons, text="Health And Education", bg='#262626', fg='white').grid(row=1, column=2,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=imj4, command=lambda :(webview.create_window("The Care And Feeding Of Children", 'https://openlibrary.org/borrow/ia/carefeedingof00holt?ref=ol'),webview.start())).grid(row=0, column=3,pady=32,padx=32, sticky='news')
		tk.Label(frame_buttons, text="The Care And Feeding\n Of Children", bg='#262626', fg='white').grid(row=1, column=3,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=imj5, command=lambda :(webview.create_window("Strength : A treatise on the development and use of muscle", 'https://openlibrary.org/borrow/ia/b2197777x?ref=ol'),webview.start())).grid(row=0, column=4,pady=32,padx=32, sticky='news')
		tk.Label(frame_buttons, text="Strength : A treatise on the \ndevelopment & use of muscle", bg='#262626', fg='white').grid(row=1, column=4,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=imj6, command=lambda :(webview.create_window("Anatomy Of Melancholy", 'https://openlibrary.org/borrow/ia/anatomyofmelancholy01burtuoft?ref=ol'),webview.start())).grid(row=2, column=0,pady=32,padx=32, sticky='news')
		tk.Label(frame_buttons, text="Anatomy Of Melancholy", bg='#262626', fg='white').grid(row=3, column=0,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=imj7, command=lambda :(webview.create_window("Power Through Repose", 'https://openlibrary.org/borrow/ia/powerthroughrepo00calliala?ref=ol'),webview.start())).grid(row=2, column=1,pady=32,padx=32, sticky='news')
		tk.Label(frame_buttons, text="Power Through Repose", bg='#262626', fg='white').grid(row=3, column=1,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=imj8, command=lambda :(webview.create_window("Codex ALimentarius", 'https://openlibrary.org/borrow/ia/bub_gb_Yj4EKS91wvgC?ref=ol'),webview.start())).grid(row=2, column=2,pady=32,padx=32, sticky='news')
		tk.Label(frame_buttons, text="Codex ALimentarius", bg='#262626', fg='white').grid(row=3, column=2,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=imj9, command=lambda :(webview.create_window("Doyle Drive", 'https://openlibrary.org/borrow/ia/doyledrivesoutha05sanf?ref=ol'),webview.start())).grid(row=2, column=3,pady=32,padx=32, sticky='news')
		tk.Label(frame_buttons, text="Doyle Drive", bg='#262626', fg='white').grid(row=3, column=3,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=imj10, command=lambda :(webview.create_window("Golden Bough", 'https://openlibrary.org/borrow/ia/goldenboughstudy05frazuoft?ref=ol'),webview.start())).grid(row=2, column=4,pady=32,padx=32, sticky='news')
		tk.Label(frame_buttons, text="Golden Bough", bg='#262626', fg='white').grid(row=3, column=4,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=imj11, command=lambda :(webview.create_window("History Of The Hebrew Commonwealth", 'https://openlibrary.org/borrow/ia/historyofhebrew00bail?ref=ol'),webview.start())).grid(row=4, column=0,pady=32,padx=32, sticky='news')
		tk.Label(frame_buttons, text="History Of The \nHebrew Commonwealth", bg='#262626', fg='white').grid(row=5, column=0,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=imj12, command=lambda :(webview.create_window("The Implications Of Medical Technology", 'https://openlibrary.org/borrow/ia/implicationsofco00unit?ref=ol'),webview.start())).grid(row=4, column=1,pady=32,padx=32, sticky='news')
		tk.Label(frame_buttons, text="The Implications Of\n Medical Technology", bg='#262626', fg='white').grid(row=5, column=1,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=imj13, command=lambda :(webview.create_window("Health Care Reform", 'https://openlibrary.org/borrow/ia/healthcarereform101994unit?ref=ol'),webview.start())).grid(row=4, column=2,pady=32,padx=32, sticky='news')
		tk.Label(frame_buttons, text="Health Care Reform", bg='#262626', fg='white').grid(row=5, column=2,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=imj14, command=lambda :(webview.create_window("Tokology", 'https://openlibrary.org/borrow/ia/tokologybookfor00stoc?ref=ol'),webview.start())).grid(row=4, column=3,pady=32,padx=32, sticky='news')
		tk.Label(frame_buttons, text="Tokology", bg='#262626', fg='white').grid(row=5, column=3,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=imj15, command=lambda :(webview.create_window("The Evoulution Of Public Health", 'https://openlibrary.org/borrow/ia/evolutionpublic01braigoog?ref=ol'),webview.start())).grid(row=4, column=4,pady=32,padx=32, sticky='news')
		tk.Label(frame_buttons, text="The Evolution Of \nPublic Health", bg='#262626', fg='white').grid(row=5, column=4,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=imj16, command=lambda :(webview.create_window("Our Seamen", 'https://openlibrary.org/borrow/ia/ourseamenappeal00plim?ref=ol'),webview.start())).grid(row=6, column=0,pady=32,padx=32, sticky='news')
		tk.Label(frame_buttons, text="Our Seamen", bg='#262626', fg='white').grid(row=7, column=0,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=imj17, command=lambda :(webview.create_window("Plain Facts About Sexual Life", 'https://openlibrary.org/borrow/ia/plainfactsforold01kell?ref=ol'),webview.start())).grid(row=6, column=1,pady=32,padx=32, sticky='news')
		tk.Label(frame_buttons, text="Plain Facts About\n Sexual Life", bg='#262626', fg='white').grid(row=7, column=1,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=imj18, command=lambda :(webview.create_window("What A Man Of Forty-Five Ought To Know", 'https://openlibrary.org/borrow/ia/whatmanoffortyfi00staluoft?ref=ol'),webview.start())).grid(row=6, column=2,pady=32,padx=32, sticky='news')
		tk.Label(frame_buttons, text="What A Man Of Forty-Five\n Ought To Know", bg='#262626', fg='white').grid(row=7, column=2,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=imj19, command=lambda :(webview.create_window("Dental Formulary", 'https://openlibrary.org/borrow/ia/dentalformularyp00prin?ref=ol'),webview.start())).grid(row=6, column=3,pady=32,padx=32, sticky='news')
		tk.Label(frame_buttons, text="Dental Formulary", bg='#262626', fg='white').grid(row=7, column=3,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=imj19, command=lambda :(webview.create_window("Food and feeding", 'https://openlibrary.org/borrow/ia/b28119587?ref=ol'),webview.start())).grid(row=6, column=4,pady=32,padx=32, sticky='news')
		tk.Label(frame_buttons, text="Food and feeding", bg='#262626', fg='white').grid(row=7, column=4,ipadx=40, ipady=14, sticky='n')

		
		frame_buttons.update_idletasks()
		canvas.config(scrollregion=canvas.bbox("all"))
			
			
	imh1 = ImageTk.PhotoImage(Image.open("img/biog/King Henry V.jpg"))
	imh2 = ImageTk.PhotoImage(Image.open("img/biog/Don Quxite.jpg"))
	imh3 = ImageTk.PhotoImage(Image.open("img/biog/Sonnets.jpg"))
	imh4 = ImageTk.PhotoImage(Image.open("img/biog/Gullivers Travels.jpg"))
	imh5 = ImageTk.PhotoImage(Image.open("img/biog/Paradise Lost.jpg"))
	imh6 = ImageTk.PhotoImage(Image.open("img/biog/Piligrim Progress.jpg"))
	imh7 = ImageTk.PhotoImage(Image.open("img/biog/Life.jpg"))
	imh8 = ImageTk.PhotoImage(Image.open("img/biog/Walden.jpg"))
	imh9 = ImageTk.PhotoImage(Image.open("img/biog/The Complete Poetical Works.jpg"))
	imh10 = ImageTk.PhotoImage(Image.open("img/biog/Confessions.jpg"))
	imh11 = ImageTk.PhotoImage(Image.open("img/biog/Dairy Of Samule Pepys.jpg"))
	imh12 = ImageTk.PhotoImage(Image.open("img/biog/The Life And Voyages Of Christopher Colombus.jpg"))
	imh13 = ImageTk.PhotoImage(Image.open("img/biog/Life On The Mississippi.jpg"))
	imh14 = ImageTk.PhotoImage(Image.open("img/biog/American Notes.jpg"))
	imh15 = ImageTk.PhotoImage(Image.open("img/biog/The Life Of Charlotte Bronte.jpg"))
	imh16 = ImageTk.PhotoImage(Image.open("img/biog/Childhood Boyhood And Youth.jpg"))
	imh17 = ImageTk.PhotoImage(Image.open("img/biog/Studies Of A Biographer.jpg"))
	imh18 = ImageTk.PhotoImage(Image.open("img/biog/The Life Of Colnel Paul Ravierie.jpg"))
	imh19 = ImageTk.PhotoImage(Image.open("img/biog/An Albama Student.jpg"))
	imh20 = ImageTk.PhotoImage(Image.open("img/biog/The Life Of Mozart.jpg"))
	def biog():
		tk.Button(frame_buttons, image=imh1, command=lambda :(webview.create_window("King Henry V", 'https://openlibrary.org/borrow/ia/henryfifthhistor00shak?ref=ol'),webview.start())).grid(row=0, column=0,pady=32,padx=32, sticky='news')
		tk.Label(frame_buttons, text="King Henry V", bg='#262626', fg='white').grid(row=1, column=0,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=imh2, command=lambda :(webview.create_window("Don Quxite", 'https://openlibrary.org/borrow/ia/historyofingeni02cerv?ref=ol'),webview.start())).grid(row=0, column=1,pady=32,padx=32, sticky='news')
		tk.Label(frame_buttons, text="Don Quixote", bg='#262626', fg='white').grid(row=1, column=1,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=imh3, command=lambda :(webview.create_window("Sonnets", 'https://openlibrary.org/borrow/ia/cu31924013143338?ref=ol'),webview.start())).grid(row=0, column=2,pady=32,padx=32, sticky='news')
		tk.Label(frame_buttons, text="Sonnets", bg='#262626', fg='white').grid(row=1, column=2,ipadx=42, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=imh4, command=lambda :(webview.create_window("Gullivers Travels", 'https://openlibrary.org/borrow/ia/voyagesdegulliv00swif?ref=ol'),webview.start())).grid(row=0, column=3,pady=32,padx=32, sticky='news')
		tk.Label(frame_buttons, text="Gullivers Travels", bg='#262626', fg='white').grid(row=1, column=3,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=imh5, command=lambda :(webview.create_window("Paradise Lost", 'https://openlibrary.org/borrow/ia/miltonsparadisel00miltuoft?ref=ol'),webview.start())).grid(row=0, column=4,pady=32,padx=32, sticky='news')
		tk.Label(frame_buttons, text="Paradise Lost", bg='#262626', fg='white').grid(row=1, column=4,ipadx=52, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=imh6, command=lambda :(webview.create_window("Piligrim's Progress", 'https://openlibrary.org/borrow/ia/pilgrimsprogress03bun?ref=ol'),webview.start())).grid(row=2, column=0,pady=32,padx=32, sticky='news')
		tk.Label(frame_buttons, text="Piligrim's Progress", bg='#262626', fg='white').grid(row=3, column=0,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=imh7, command=lambda :(webview.create_window("Life", 'https://openlibrary.org/borrow/ia/adt3936.0001.001.umich.edu?ref=ol'),webview.start())).grid(row=2, column=1,pady=32,padx=32, sticky='news')
		tk.Label(frame_buttons, text="Life", bg='#262626', fg='white').grid(row=3, column=1,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=imh8, command=lambda :(webview.create_window("Walden", 'https://openlibrary.org/borrow/ia/cu31924021445741?ref=ol'),webview.start())).grid(row=2, column=2,pady=32,padx=32, sticky='news')
		tk.Label(frame_buttons, text="Walden", bg='#262626', fg='white').grid(row=3, column=2,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=imh9, command=lambda :(webview.create_window("The Complete Poetical Works", 'https://openlibrary.org/borrow/ia/poeticalworksofr00burn?ref=ol'),webview.start())).grid(row=2, column=3,pady=32,padx=32, sticky='news')
		tk.Label(frame_buttons, text="The Complete Poetical\n Works", bg='#262626', fg='white').grid(row=3, column=3,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=imh10, command=lambda :(webview.create_window("Confessions", 'https://openlibrary.org/borrow/ia/confessionsofsai00augurich?ref=ol'),webview.start())).grid(row=2, column=4,pady=32,padx=32, sticky='news')
		tk.Label(frame_buttons, text="Confessions", bg='#262626', fg='white').grid(row=3, column=4,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=imh11, command=lambda :(webview.create_window("Dairy Of Samuel Papys", 'https://openlibrary.org/borrow/ia/diarycorresponde00pepy?ref=ol'),webview.start())).grid(row=4, column=0,pady=32,padx=32, sticky='news')
		tk.Label(frame_buttons, text="Dairy Of Samule Pepys", bg='#262626', fg='white').grid(row=5, column=0,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=imh12, command=lambda :(webview.create_window("The Life And Voyages Of Christopher Columbus", 'https://openlibrary.org/borrow/ia/lifeandvoyages00irviiala?ref=ol'),webview.start())).grid(row=4, column=1,pady=32,padx=32, sticky='news')
		tk.Label(frame_buttons, text="The Life And Voyages Of\n Christopher Columbus", bg='#262626', fg='white').grid(row=5, column=1,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=imh13, command=lambda :(webview.create_window("Life On The Mississippi", 'https://openlibrary.org/borrow/ia/writingsmark09twairich?ref=ol'),webview.start())).grid(row=4, column=2,pady=32,padx=32, sticky='news')
		tk.Label(frame_buttons, text="Life On The Mississippi", bg='#262626', fg='white').grid(row=5, column=2,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=imh14, command=lambda :(webview.create_window("American Notes", 'https://openlibrary.org/borrow/ia/americannotesdic00dickiala?ref=ol'),webview.start())).grid(row=4, column=3,pady=32,padx=32, sticky='news')
		tk.Label(frame_buttons, text="American Notes", bg='#262626', fg='white').grid(row=5, column=3,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=imh15, command=lambda :(webview.create_window("The Life Of Charlotte Bronte", 'https://openlibrary.org/borrow/ia/lifeofcharlotteb01gask?ref=ol'),webview.start())).grid(row=4, column=4,pady=32,padx=32, sticky='news')
		tk.Label(frame_buttons, text="The Life Of Charlotte Bronte", bg='#262626', fg='white').grid(row=5, column=4,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=imh16, command=lambda :(webview.create_window("Childhood, Boyhood And Youth", 'https://openlibrary.org/borrow/ia/nybc204937?ref=ol'),webview.start())).grid(row=6, column=0,pady=32,padx=32, sticky='news')
		tk.Label(frame_buttons, text="Childhood, Boyhood And\n Youth", bg='#262626', fg='white').grid(row=7, column=0,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=imh17, command=lambda :(webview.create_window("Studies Of A Biographer", 'https://openlibrary.org/borrow/ia/studiesofbiograp01stepiala?ref=ol'),webview.start())).grid(row=6, column=1,pady=32,padx=32, sticky='news')
		tk.Label(frame_buttons, text="Studies Of A Biographer", bg='#262626', fg='white').grid(row=7, column=1,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=imh18, command=lambda :(webview.create_window("The Life Of Colonel Paul Ravierie", 'https://openlibrary.org/borrow/ia/lifecolonelpaul01gossgoog?ref=ol'),webview.start())).grid(row=6, column=2,pady=32,padx=32, sticky='news')
		tk.Label(frame_buttons, text="The Life Of Colonel\n Paul Ravierie", bg='#262626', fg='white').grid(row=7, column=2,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=imh19, command=lambda :(webview.create_window("An Albama Student", 'https://openlibrary.org/borrow/ia/cu31924011944620?ref=ol'),webview.start())).grid(row=6, column=3,pady=32,padx=32, sticky='news')
		tk.Label(frame_buttons, text="An Albama Student", bg='#262626', fg='white').grid(row=7, column=3,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=imh20, command=lambda :(webview.create_window("The Life Of Mozart", 'https://openlibrary.org/borrow/ia/lifemozart00nohlgoog?ref=ol'),webview.start())).grid(row=6, column=4,pady=32,padx=32, sticky='news')
		tk.Label(frame_buttons, text="The Life Of Mozart", bg='#262626', fg='white').grid(row=7, column=4,ipadx=40, ipady=14, sticky='n')

		frame_buttons.update_idletasks()
		canvas.config(scrollregion=canvas.bbox("all"))
		
		
		
	imi1 = ImageTk.PhotoImage(Image.open("img/textbok/Elements.jpg"))
	imi2 = ImageTk.PhotoImage(Image.open("img/textbok/Physics By Aristotle.jpg"))
	imi3 = ImageTk.PhotoImage(Image.open("img/textbok/Principles Of Plant Culture.jpg"))
	imi4 = ImageTk.PhotoImage(Image.open("img/textbok/Botany For Young People.jpg"))
	imi5 = ImageTk.PhotoImage(Image.open("img/textbok/The Teachings Of Jesus.jpg"))
	imi6 = ImageTk.PhotoImage(Image.open("img/textbok/Oliver Twist.jpg"))
	imi7 = ImageTk.PhotoImage(Image.open("img/textbok/The Rules Of The Game.jpg"))
	imi8 = ImageTk.PhotoImage(Image.open("img/textbok/Andersens Stories.jpg"))
	imi9 = ImageTk.PhotoImage(Image.open("img/textbok/Short Stories.jpg"))
	imi10 = ImageTk.PhotoImage(Image.open("img/textbok/Silas Marner.jpg"))
	imi11 = ImageTk.PhotoImage(Image.open("img/textbok/The Plays Of Oscar Wilde.jpg"))
	imi12 = ImageTk.PhotoImage(Image.open("img/textbok/Ruy Blas.jpg"))
	imi13 = ImageTk.PhotoImage(Image.open("img/textbok/Colloquia.jpg"))
	imi14 = ImageTk.PhotoImage(Image.open("img/textbok/Faerie Queene.jpg"))
	imi15 = ImageTk.PhotoImage(Image.open("img/textbok/Abridgment Of Murrays English Grammer.jpg"))
	imi16 = ImageTk.PhotoImage(Image.open("img/textbok/Spelling Book.jpg"))
	imi17 = ImageTk.PhotoImage(Image.open("img/textbok/Middle March.jpg"))
	imi18 = ImageTk.PhotoImage(Image.open("img/textbok/Sense Of Sensibility.jpg"))
	imi19 = ImageTk.PhotoImage(Image.open("img/textbok/What We Hear In Music.jpg"))
	imi20 = ImageTk.PhotoImage(Image.open("img/textbok/Handbook Of Christian Religion.jpg"))
	
		
	def textbok():
		tk.Button(frame_buttons, image=imi1, command=lambda :(webview.create_window("Elements", 'https://openlibrary.org/borrow/ia/cihm_59096?ref=ol'),webview.start())).grid(row=0, column=0,pady=32,padx=32, sticky='news')
		tk.Label(frame_buttons, text="Elements", bg='#262626', fg='white').grid(row=1, column=0,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=imi2, command=lambda :(webview.create_window("Physics By Aristotle", 'https://openlibrary.org/borrow/ia/in.ernet.dli.2015.183610?ref=ol'),webview.start())).grid(row=0, column=1,pady=32,padx=32, sticky='news')
		tk.Label(frame_buttons, text="Physics By Aristotle", bg='#262626', fg='white').grid(row=1, column=1,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=imi3, command=lambda :(webview.create_window("Principles Of Plant Culture", 'https://openlibrary.org/borrow/ia/cu31924000414031?ref=ol'),webview.start())).grid(row=0, column=2,pady=32,padx=32, sticky='news')
		tk.Label(frame_buttons, text="Principles Of Plant Culture", bg='#262626', fg='white').grid(row=1, column=2,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=imi4, command=lambda :(webview.create_window("Botany For Young People", 'https://openlibrary.org/borrow/ia/cu31924031496734?ref=ol'),webview.start())).grid(row=0, column=3,pady=32,padx=32, sticky='news')
		tk.Label(frame_buttons, text="Botany For Young People", bg='#262626', fg='white').grid(row=1, column=3,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=imi5, command=lambda :(webview.create_window("The Teachings Of Jesus", 'https://openlibrary.org/borrow/ia/theteachingsofje00ralluoft?ref=ol'),webview.start())).grid(row=0, column=4,pady=32,padx=32, sticky='news')
		tk.Label(frame_buttons, text="The Teachings Of Jesus", bg='#262626', fg='white').grid(row=1, column=4,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=imi6, command=lambda :(webview.create_window("The Rules Of The Game", 'https://openlibrary.org/borrow/ia/MN41746ucmf_6?ref=ol'),webview.start())).grid(row=2, column=0,pady=32,padx=32, sticky='news')
		tk.Label(frame_buttons, text="The Rules Of The Game", bg='#262626', fg='white').grid(row=3, column=0,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=imi7, command=lambda :(webview.create_window("Oliver Twist", 'https://openlibrary.org/borrow/ia/olivertwist1900dick?ref=ol'),webview.start())).grid(row=2, column=1,pady=32,padx=32, sticky='news')
		tk.Label(frame_buttons, text="Oliver Twist", bg='#262626', fg='white').grid(row=3, column=1,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=imi8, command=lambda :(webview.create_window("Andersens Stories", 'https://openlibrary.org/borrow/ia/storiesforhouseh00ande?ref=ol'),webview.start())).grid(row=2, column=2,pady=32,padx=32, sticky='news')
		tk.Label(frame_buttons, text="Andersens Stories", bg='#262626', fg='white').grid(row=3, column=2,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=imi9, command=lambda :(webview.create_window("Short Stories", 'https://openlibrary.org/borrow/ia/duelotherstories00chek?ref=ol'),webview.start())).grid(row=2, column=3,pady=32,padx=32, sticky='news')
		tk.Label(frame_buttons, text="Short Stories", bg='#262626', fg='white').grid(row=3, column=3,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=imi10, command=lambda :(webview.create_window("Silas Marner", 'https://openlibrary.org/borrow/ia/silasmarnerweave00eliouoft?ref=ol'),webview.start())).grid(row=2, column=4,pady=32,padx=32, sticky='news')
		tk.Label(frame_buttons, text="Silas Marner", bg='#262626', fg='white').grid(row=3, column=4,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=imi11, command=lambda :(webview.create_window("The Plays Of Oscar Wilde", 'https://openlibrary.org/borrow/ia/playsofoscarwild01wild?ref=ol'),webview.start())).grid(row=4, column=0,pady=32,padx=32, sticky='news')
		tk.Label(frame_buttons, text="The Plays Of Oscar Wilde", bg='#262626', fg='white').grid(row=5, column=0,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=imh12, command=lambda :(webview.create_window("Ruy Blas", 'https://openlibrary.org/borrow/ia/lesiximeactedu00hugo?ref=ol'),webview.start())).grid(row=4, column=1,pady=32,padx=32, sticky='news')
		tk.Label(frame_buttons, text="Ruy Blas", bg='#262626', fg='white').grid(row=5, column=1,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=imh13, command=lambda :(webview.create_window("Colloquia", 'https://openlibrary.org/borrow/ia/twentytwocoll00erasuoft?ref=ol'),webview.start())).grid(row=4, column=2,pady=32,padx=32, sticky='news')
		tk.Label(frame_buttons, text="Colloquia", bg='#262626', fg='white').grid(row=5, column=2,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=imh14, command=lambda :(webview.create_window("Faerie Queene", 'https://openlibrary.org/borrow/ia/faeriequeene02spenuoft?ref=ol'),webview.start())).grid(row=4, column=3,pady=32,padx=32, sticky='news')
		tk.Label(frame_buttons, text="Faerie Queene", bg='#262626', fg='white').grid(row=5, column=3,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=imh15, command=lambda :(webview.create_window("Abridgment Of Murrays English Grammer", 'https://openlibrary.org/borrow/ia/cihm_53558?ref=ol'),webview.start())).grid(row=4, column=4,pady=32,padx=32, sticky='news')
		tk.Label(frame_buttons, text="Abridgment Of Murrays\n English Grammer", bg='#262626', fg='white').grid(row=5, column=4,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=imh16, command=lambda :(webview.create_window("Spelling Book", 'https://openlibrary.org/borrow/ia/americanspelling00webs?ref=ol'),webview.start())).grid(row=6, column=0,pady=32,padx=32, sticky='news')
		tk.Label(frame_buttons, text="Spelling Book", bg='#262626', fg='white').grid(row=7, column=0,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=imh17, command=lambda :(webview.create_window("Middle March", 'https://openlibrary.org/borrow/ia/middlemarchstudy01elioiala?ref=ol'),webview.start())).grid(row=6, column=1,pady=32,padx=32, sticky='news')
		tk.Label(frame_buttons, text="Middle March", bg='#262626', fg='white').grid(row=7, column=1,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=imh18, command=lambda :(webview.create_window("Sense Of Sensibility", 'https://openlibrary.org/borrow/ia/sensesensibility00austuoft?ref=ol'),webview.start())).grid(row=6, column=2,pady=32,padx=32, sticky='news')
		tk.Label(frame_buttons, text="Sense Of Sensibility", bg='#262626', fg='white').grid(row=7, column=2,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=imh19, command=lambda :(webview.create_window("What We Hear In Music", 'https://openlibrary.org/borrow/ia/whatwehearinmusi00ober?ref=ol'),webview.start())).grid(row=6, column=3,pady=32,padx=32, sticky='news')
		tk.Label(frame_buttons, text="What We Hear In Music", bg='#262626', fg='white').grid(row=7, column=3,ipadx=40, ipady=14, sticky='n')

		tk.Button(frame_buttons, image=imh20, command=lambda :(webview.create_window("Handbook Of Christian Religion", 'https://openlibrary.org/borrow/ia/handbookofchrist00wilm?ref=ol'),webview.start())).grid(row=6, column=4,pady=32,padx=32, sticky='news')
		tk.Label(frame_buttons, text="Handbook Of Christian\n Religion", bg='#262626', fg='white').grid(row=7, column=4,ipadx=40, ipady=14, sticky='n')

		frame_buttons.update_idletasks()
		canvas.config(scrollregion=canvas.bbox("all"))
		
		

	"""	
	def yrr():
		rows = 20
		columns = 6
		#buttons = [[tk.Button() for j in range(columns)] for i in range(rows)]
		for i in range(2, rows):
		    for j in range(0, columns):
			#tk.Button(frame_buttons, text=("hehe%d,%d" % (i+1, j+1)),command=newb).grid(row=i, column=j,pady=10,padx=10, sticky='news')
		    	tk.Button(frame_buttons, text="asdfasdf", image=img1).grid(row=i, column=j,pady=30,padx=30, sticky='news')
		frame_buttons.update_idletasks()
		canvas.config(scrollregion=canvas.bbox("all"))
	"""
	def logout():
		os.remove("cred")
		#cur.execute("drop table actusr")
		#con.commit()
		#cur.execute("drop table history")
		#con.commit()
		root.destroy()
		

	tk.Button(frame_main, text="Home",command=home, bg="#404040", fg="white").grid(row=1, column=0, padx=20, pady=10, sticky='nw')
	tk.Button(frame_main, text="Art",command=art, bg="#404040", fg="white").grid(row=1, column=0, padx=110, pady=10, sticky='nw')
	tk.Button(frame_main, text="Fiction",command=fiction, bg="#404040", fg="white").grid(row=1, column=0, padx=155, pady=10, sticky='nw')
	tk.Button(frame_main, text="Science & Mathematics",command=scimat, bg="#404040", fg="white").grid(row=1, column=0, padx=225, pady=10, sticky='nw')
	tk.Button(frame_main, text="Business & Finance",command=busifi, bg="#404040", fg="white").grid(row=1, column=0, padx=405, pady=10, sticky='nw')
	tk.Button(frame_main, text="Children's",command=kids, bg="#404040", fg="white").grid(row=1, column=0, padx=555, pady=10, sticky='nw')
	tk.Button(frame_main, text="History",command=history, bg="#404040", fg="white").grid(row=1, column=0, padx=645, pady=10, sticky='nw')
	tk.Button(frame_main, text="Health & Wellness",command=health, bg="#404040", fg="white").grid(row=1, column=0, padx=720, pady=10, sticky='nw')
	tk.Button(frame_main, text="Biography",command=biog, bg="#404040", fg="white").grid(row=1, column=0, padx=865, pady=10, sticky='nw')
	tk.Button(frame_main, text="Textbooks",command=textbok, bg="#404040", fg="white").grid(row=1, column=0, padx=955, pady=10, sticky='nw')
	
	tk.Label(frame_main, text="> "+uname, bg="#262626", fg="white").grid(row=0, column=0, padx=1200, pady=10, sticky='nw')
	tk.Button(frame_main, text="Logout",command=logout, bg="#404040", fg="white").grid(row=1, column=0, padx=1280, pady=0, sticky='nw')
	
	tk.Button(frame_main, text="Borrow Books",command=borrow, bg="#404040", fg="white").grid(row=3, column=0, padx=20, pady=10, sticky='nw')


	"""
	# Add 9-by-5 buttons to the frame
	rows = 10
	columns = 10
	#buttons = [[tk.Button() for j in range(columns)] for i in range(rows)]
	for i in range(0, rows):
	    for j in range(0, columns):
	    	tk.Button(frame_buttons, text=("%d,%d" % (i+1, j+1)),command=newb).grid(row=i, column=j,pady=10,padx=10, sticky='news')
	      #  buttons[i][j] = tk.Button(frame_buttons, text=("%d,%d" % (i+1, j+1)))
	       # buttons[i][j].grid(row=i, column=j,pady=10,padx=10, sticky='news')
	"""
	# Update buttons frames idle tasks to let tkinter calculate buttons sizes
	frame_buttons.update_idletasks()

	# Resize the canvas frame to show exactly 5-by-5 buttons and the scrollbar
	#first5columns_width = sum([buttons[0][j].winfo_width() for j in range(0, 5)])
	#first5rows_height = sum([buttons[i][0].winfo_height() for i in range(0, 5)])
	frame_canvas.config(width=1350 + vsb.winfo_width(), height=550)

	# Set the canvas scrolling region
	canvas.config(scrollregion=canvas.bbox("all"))

	# Launch the GUI
	root.mainloop()	
#digimain()			
