from tkinter import *
from main import main
root=Tk()
root.geometry('500x300')
root.resizable(0,0)
root.title("Handwriting Recognition")
Label(root,text='HANDWRITING RECOGNITION', font='arial 20 bold').pack()
link=StringVar()
Label(root, text='Paste Your link here', font='arial 15 bold').place(x=160,y=60)
link_enter=Entry(root, width=70, textvariable=link).place(x=32, y=90)
def Recognize():
     img_file=str(link.get())
     a=main(img_file)
     Label(root,text=a, font='arial 15 bold').place(x=180,y=210)
Button(root,text='Recognize', font='arial 15 bold', bg='pale violet red', padx=2,command=Recognize).place(x=120,y=150)
root.mainloop()