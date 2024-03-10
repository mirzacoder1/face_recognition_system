from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from tkinter import filedialog
import csv
import os
# import cv2

mydata=[]

class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x800+0+0")
        self.root.title("Attendance System")

        # ==============Text Vatiables====================
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()

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
        title_lbl=Label(bg_img,text="Attendace Management System",font=("times new roman",35,"italic bold"),bg="green",fg="gold")
        title_lbl.place(x=0,y=0,width=1530,height=45)


        main_frame=Frame(bg_img,bd=2, bg="white")
        main_frame.place(x=15,y=55,width=1500,height=600)

        # left label frame
        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Details", font=("times new roman",12,"bold italic"))
        left_frame.place(x=10,y=10,width=730,height=580)


        # img_left=Image.open("__Image Path__")
        # img_left=img_left.resize((720,130),Image.Resampling.LANCZOS)
        # self.photoimg_left=ImageTk.PhotoImage(img_left)

        # f_lbl=Label(left_frame,image=self.photoimg_left)
        # f_lbl.place(x=5,y=0,width=720,height=130)

        left_inside_frame=Frame(left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=5,y=135,width=710,height=370)

        
        # Label and Entries

        # Attendance Id 
        AttendanceId_label=Label(left_inside_frame,text="AttendanceID:",font=("times new roman",12,"bold italic"))
        AttendanceId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        AttendanceId_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_id,font=("times new roman",12,"bold italic"))
        AttendanceId_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)


        # Roll 
        Roll_label=Label(left_inside_frame,text="Roll:",font=("times new roman",12,"bold italic"))
        Roll_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        Roll_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_roll,font=("times new roman",12,"bold italic"))
        Roll_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)


        # Name
        name_label=Label(left_inside_frame,text="Name:",font=("times new roman",12,"bold italic"))
        name_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)
        name_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_name,font=("times new roman",12,"bold italic"))
        name_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)


        # Department
        dep_label=Label(left_inside_frame,text="Department:",font=("times new roman",12,"bold italic"))
        dep_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)
        dep_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_dep,font=("times new roman",12,"bold italic"))
        dep_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)


        # Time
        time_label=Label(left_inside_frame,text="Time:",font=("times new roman",12,"bold italic"))
        time_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)
        time_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_time,font=("times new roman",12,"bold italic"))
        time_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)


        # Date
        time_label=Label(left_inside_frame,text="Time:",font=("times new roman",12,"bold italic"))
        time_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)
        Date_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_date,font=("times new roman",12,"bold italic"))
        Date_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)


        # Attendance
        Attendance_label=Label(left_inside_frame,text="Attendace Status:",font=("times new roman",12,"bold italic"))
        Attendance_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)
        _Attendance_Status_combo=ttk.Combobox(left_inside_frame,font=("times new roman",12,"bold italic"),width=20,textvariable=self.var_atten_attendance,state="readonly")
        _Attendance_Status_combo["values"]=("Status","Present","Absent")
        _Attendance_Status_combo.current(0)
        _Attendance_Status_combo.grid(row=3,column=1,padx=2,pady=8,sticky=W)



         # Button Frames
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=300,width=715,height=35)


        save_btn=Button(btn_frame,text="Import CSV",command=self.importCSV,font=("times new roman",12,"bold italic"),bg="blue",fg="white",width=19)
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Export CSV",command=self.exportCSV,font=("times new roman",12,"bold italic"),bg="blue",fg="white",width=19)
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Update",font=("times new roman",12,"bold italic"),bg="blue",fg="white",width=19)
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,font=("times new roman",12,"bold italic"),bg="blue",fg="white",width=19)
        reset_btn.grid(row=0,column=3)






        # right label frame
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Details", font=("times new roman",12,"bold italic"))
        right_frame.place(x=740,y=10,width=730,height=580)

        # img_right=Image.open("__Image Path__")
        # img_right=img_right.resize((720,130),Image.Resampling.LANCZOS)
        # self.photoimg_right=ImageTk.PhotoImage(img_right)

        # f_lbl=Label(right_frame,image=self.photoimg_right)
        # f_lbl.place(x=5,y=0,width=720,height=130)

        table_frame=Frame(right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=700,height=520)

        scroll_x = ttk.Scrollbar(right_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(right_frame,orient=VERTICAL)


        self.AttendanceReportTable=ttk.Treeview(table_frame,columns=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="AttendanceID")
        self.AttendanceReportTable.heading("roll",text="Roll")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")

        self.AttendanceReportTable["show"]="headings"
        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)



        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_Cursor)

    

    # =========================Fetch data====================
    
    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)

    # Import CSV
    def importCSV(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALL File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

    # Export CSV
    def exportCSV(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data Found to Export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALL File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your data have been exported Successfully to"+os.path.basename(fln))

        except Exception as es:
            messagebox.showerror("Dut To:File Not been Exported....")

    
    def get_Cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])





    # ====================Reset Function====================
    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("Status")






if __name__=="__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()