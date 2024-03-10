from tkinter import *
from tkinter import messagebox
from time import strftime
from PIL import Image,ImageTk
from face_recognition import Face_Recognition
from student import Student
from train import Train
from attendance import Attendance
import os

class Face_recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")
        
        # First Image
        img1=Image.open(r"./Images/heading1.jpg")
        img1=img1.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=0,y=0,width=500,height=130)

        # Second Image
        img2=Image.open(r"./Images/heading2.jpg")
        img2=img2.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=500,y=0,width=500,height=130)

        # Third Image
        img3=Image.open(r"./Images/heading1.jpg")
        img3=img3.resize((560,130),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        f_lbl=Label(self.root,image=self.photoimg3)
        f_lbl.place(x=1000,y=0,width=560,height=130)
        

        # Background Image
        img4=Image.open(r"./Images/background.jpg")
        img4=img4.resize((1530,730),Image.Resampling.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        bg_img=Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=120,width=1530,height=730)


        # Title
        title_lbl=Label(bg_img,text="FACE RECOGNITION SYSTEM SOFTWARE",font=("times new roman",35,"italic bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        # ============Time==================
        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text = string)
            lbl.after(1000, time)

        lbl = Label(title_lbl, font=('times new roman',14,'bold'),background="white",foreground="blue")
        lbl.place(x=0,y=(-15),width=110,height=50)
        time()



        # student Button
        img5=Image.open(r"./Images/student.png")
        img5=img5.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2", font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=300,width=220,height=40)


        # face Detection Button
        img6=Image.open(r"./Images/faceDetector.jpeg")
        img6=img6.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b2=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.face_data)
        b2.place(x=500,y=100,width=220,height=220)

        b2_1=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data, font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b2_1.place(x=500,y=300,width=220,height=40)


        # Attendece face Button
        img7=Image.open(r"./Images/attendence.jpg")
        img7=img7.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b3=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.attendace_data)
        b3.place(x=800,y=100,width=220,height=220)

        b3_1=Button(bg_img,text="Attendance",cursor="hand2",command=self.attendace_data, font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b3_1.place(x=800,y=300,width=220,height=40)


        # HelpDesk Button
        img8=Image.open(r"./Images/helpDesk.png")
        img8=img8.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b4=Button(bg_img,image=self.photoimg8,cursor="hand2")
        b4.place(x=1100,y=100,width=220,height=220)

        b4_1=Button(bg_img,text="Help Desk",cursor="hand2", font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b4_1.place(x=1100,y=300,width=220,height=40)


        # Train Face Button
        img9=Image.open(r"./Images/trainData.png")
        img9=img9.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b5=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.train_data)
        b5.place(x=200,y=380,width=220,height=220)

        b5_1=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data, font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b5_1.place(x=200,y=580,width=220,height=40)


        # Photos face Button
        img10=Image.open(r"./Images/gallery.png")
        img10=img10.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b6=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.open_img)
        b6.place(x=500,y=380,width=220,height=220)

        b6_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img, font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b6_1.place(x=500,y=580,width=220,height=40)


        # Developer face button
        img11=Image.open(r"./Images/developer.jpeg")
        img11=img11.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b7=Button(bg_img,image=self.photoimg11,cursor="hand2")
        b7.place(x=800,y=380,width=220,height=220)

        b7_1=Button(bg_img,text="Developer",cursor="hand2", font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b7_1.place(x=800,y=580,width=220,height=40)


        # Exit face button
        img12=Image.open(r"./Images/exit.jpg")
        img12=img12.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg12=ImageTk.PhotoImage(img12)

        b8=Button(bg_img,image=self.photoimg12,cursor="hand2",command=self.iExit)
        b8.place(x=1100,y=380,width=220,height=220) 

        b8_1=Button(bg_img,text="Exit",cursor="hand2",command=self.iExit, font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b8_1.place(x=1100,y=580,width=220,height=40)


    def open_img(self):
        os.startfile("Data")

    
    def iExit(self):
        self.iExit=messagebox.askyesno("Face Recognition","Do you Really want to exit from this Project",parent=self.root)
        if self.iExit >0:
            self.root.destroy()
        else:
            return

    # ====================Funtion Buttons=====================

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)

    def attendace_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)


    




if __name__=="__main__":
    root=Tk()
    obj=Face_recognition_System(root)
    root.mainloop()