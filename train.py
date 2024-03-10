from tkinter import *
# from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
# import mysql.connector
import numpy as np
import os
import cv2



class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x800+0+0")
        self.root.title("face Recognition System")

        img4=Image.open(r"./Images/background.jpg")
        img4=img4.resize((1530,800),Image.Resampling.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        bg_img=Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=0,width=1530,height=800)

        title_lbl=Label(bg_img,text="TRAIN DATASET",font=("times new roman",35,"italic bold"),bg="silver",fg="green")
        title_lbl.place(x=0,y=120,width=1530,height=45)


        img6=Image.open(r"./Images/trainData.png")
        img6=img6.resize((330,330),Image.Resampling.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b2=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.train_classifer)
        b2.place(x=589,y=190,width=330,height=330)

        b2_1=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_classifer, font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b2_1.place(x=589,y=520,width=330,height=40)


    def train_classifer(self):
        data_dir=("Data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L') # Grey Scale Images
            imgNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])
            faces.append(imgNp)
            ids.append(id)
            cv2.imshow("Training",imgNp)
            cv2.waitKey(1)==13
        
        ids=np.array(ids)

        # ===============Train the Classifier==============

        clf=cv2.face.LBPHFaceRecognizer.create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training DataSet Completed--")



if __name__=="__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()