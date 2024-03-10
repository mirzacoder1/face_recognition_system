from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk

class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login Page")
        self.root.geometry("1530x790+0+0")

        # Background Image
        self.bg=ImageTk.PhotoImage(file=r"./Images/LoginBackground.jpeg")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="black")
        frame.place(x=610,y=170,width=340,height=450)



if __name__=="__main__":
    root=Tk()
    app=Login_Window(root)
    root.mainloop()