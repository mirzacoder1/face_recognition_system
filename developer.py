from tkinter import *
# from tkinter import ttk
from PIL import Image,ImageTk
# import os

class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")

        img4=Image.open(r"./Images/background.jpg")
        img4=img4.resize((1530,800),Image.Resampling.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        bg_img=Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=0,width=1530,height=800)

        title_lbl=Label(bg_img,text="Developer Window",font=("times new roman",35,"italic bold"),bg="silver",fg="black")
        title_lbl.place(x=0,y=120,width=1530,height=45)


        img6=Image.open(r"./Images/developer.jpeg")
        img6=img6.resize((330,330),Image.Resampling.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b2=Button(bg_img,image=self.photoimg6,cursor="hand2")
        b2.place(x=589,y=190,width=330,height=330)

        b2_1=Button(bg_img,text="Train Data",cursor="hand2", font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b2_1.place(x=589,y=520,width=330,height=40)






if __name__=="__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()