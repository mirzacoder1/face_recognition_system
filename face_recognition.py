from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
# from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
# import numpy as np
# import os
import cv2



class Face_Recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x800+0+0")
        self.root.title("face Recognition System")

        img4=Image.open(r"./Images/background.jpg")
        img4=img4.resize((1530,800),Image.Resampling.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        bg_img=Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=0,width=1530,height=800)

        title_lbl=Label(bg_img,text="RECOGNISE THE FACE",font=("times new roman",35,"italic bold"),bg="darkblue",fg="gold")
        title_lbl.place(x=0,y=120,width=1530,height=45)


        img4=Image.open(r"./Images/faceDetector.jpeg")
        img4=img4.resize((330,330),Image.Resampling.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img4)

        b2=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.face_recog)
        b2.place(x=589,y=190,width=330,height=330)

        b2_1=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_recog, font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b2_1.place(x=589,y=520,width=330,height=40)

        # b2_2=Button(bg_img,text="Stop",cursor="hand2",command=self.Stop_Face, font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        # b2_2.place(x=589,y=560,width=330,height=40)




    # ==============Attendance===================
    def mark_attendance(self,i,r,n,dep):
        with open("attendance.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if((i not in name_list) and (r not in name_list) and (n not in name_list) and (dep not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"{i},{r},{n},{dep},{dtString},{d1},Present")



    # =============Face Recognition System=====================

    def face_recog(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbours,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbours)

            coord=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                conn=mysql.connector.connect(host="localhost",port=3307,username="root",password="ILOVEammi@786",database="face_recognition")
                my_cursor=conn.cursor()

                my_cursor.execute("select Name from student where Student_id="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)

                my_cursor.execute("select Roll from student where Student_id="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r)

                my_cursor.execute("select dep from student where Student_id="+str(id))
                dep=my_cursor.fetchone()
                dep="+".join(dep)

                my_cursor.execute("select student_id from student where Student_id="+str(id))
                i=my_cursor.fetchone()
                i="+".join(i)

                if confidence>77:
                    cv2.putText(img,f"ID:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{n}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Roll:{r}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department:{dep}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(i,r,n,dep)
                
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,f"Unknown Face.",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                coord=[x,y,w,y]
            return coord
        
        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img

        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer.create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome to Face Recognition",img)
            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()






if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()