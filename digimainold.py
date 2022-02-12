import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import webview


root = Tk()
root.title("Open Digital Library")
#root.iconbitmap(r'/home/sourav/Downloads/favicon.ico')
root.minsize(width=400,height=400)
root.geometry("1920x1080")

same=True
n=1.0

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

Canvas1.create_image(300,340,image = img)      
Canvas1.config(bg="white",width = newImageSizeWidth, height = newImageSizeHeight)
Canvas1.pack(expand=True,fill=BOTH)

headingFrame1 = Frame(root,bg="#ededed",bd=2)
headingFrame1.place(relx=0.01,rely=0.01,relwidth=0.18,relheight=0.07)

headingLabel = Label(headingFrame1, text="Open Digital Library", bg='#292929', fg='white', font=('calibri',16))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)



img1 = ImageTk.PhotoImage(Image.open("img/OL19374060M-M.jpg"))
def web():
	webview.create_window('Hello world', 'https://www.gutenberg.org/files/65304/65304-h/65304-h.htm')
	webview.start()
button_qwer = Button(root, text="asdfasdf", image=img1, command=web)
button_qwer.place(relx=0.1,rely=0.45)


root.mainloop()
