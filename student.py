from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2



class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")

        # ==================Variables==================

        self.var_course=StringVar()
        self.var_dep=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()


        #  First Image
        img1=Image.open("./Images/heading1.jpg")
        img1=img1.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=0,y=0,width=500,height=130)

        # Second Image
        img2=Image.open("./Images/heading2.jpg")
        img2=img2.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=500,y=0,width=500,height=130)

        # Third Image
        img3=Image.open("./Images/heading1.jpg")
        img3=img3.resize((560,130),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        f_lbl=Label(self.root,image=self.photoimg3)
        f_lbl.place(x=1000,y=0,width=560,height=130)

        # Background Image
        img4=Image.open("./Images/background.jpg")
        img4=img4.resize((1530,730),Image.Resampling.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        bg_img=Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=120,width=1530,height=730)


        # Title
        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",35,"italic bold"),bg="white",fg="darkblue")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        main_frame=Frame(bg_img,bd=2, bg="white")
        main_frame.place(x=15,y=55,width=1500,height=600)


        # left label frame

        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details", font=("times new roman",12,"bold italic"))
        left_frame.place(x=10,y=10,width=730,height=580)


        # img_left=Image.open("__Image Path__")
        # img_left=img_left.resize((720,130),Image.Resampling.LANCZOS)
        # self.photoimg_left=ImageTk.PhotoImage(img_left)

        # f_lbl=Label(left_frame,image=self.photoimg_left)
        # f_lbl.place(x=5,y=0,width=720,height=130)


        # current course information
        current_course_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Current course information", font=("times new roman",12,"bold italic"))
        current_course_frame.place(x=5,y=135,width=720,height=150)


        # Course
        course_label=Label(current_course_frame,text="Course",font=("times new roman",12,"bold italic"),bg="white")
        course_label.grid(row=0,column=0,padx=10,sticky=W)
        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",12,"bold italic"),width=17,state="readonly")
        course_combo["values"]=("Select Course","BE","BTech","MBA")
        course_combo.current(0)
        course_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        


        # Department
        dep_label=Label(current_course_frame,text="Department",font=("times new roman",12,"bold italic"),bg="white")
        dep_label.grid(row=0,column=2,padx=10,sticky=W)
        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",12,"bold italic"),width=17,state="readonly")
        dep_combo["values"]=("Select Department","CSE","CE","ECE","IT","ME")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)




        # Year
        year_label=Label(current_course_frame,text="Year",font=("times new roman",12,"bold italic"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)
        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",12,"bold italic"),width=17,state="readonly")
        year_combo["values"]=("Select Year","2020-21","2021-22","2022-23","2023-24","2024-25")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)



        # Semester
        semester_label=Label(current_course_frame,text="Semester",font=("times new roman",12,"bold italic"),bg="white")
        semester_label.grid(row=1,column=2,padx=10,sticky=W)
        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",12,"bold italic"),width=17,state="readonly")
        semester_combo["values"]=("Select Semester","Sem-1","Sem-2","Sem-3","Sem-4","Sem-5","Sem-6","Sem-7","Sem-8")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)




        # Class Student information
        class_student_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Current course information", font=("times new roman",12,"bold italic"))
        class_student_frame.place(x=5,y=250,width=720,height=300)


        # student Id 
        studentId_label=Label(class_student_frame,text="StudentID:",font=("times new roman",12,"bold italic"))
        studentId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        studentId_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_id,width=20,font=("times new roman",12,"bold italic"))
        studentId_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)


        # student Name 
        studentName_label=Label(class_student_frame,text="Student Name:",font=("times new roman",12,"bold italic"))
        studentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        studentName_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_name,width=20,font=("times new roman",12,"bold italic"))
        studentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)


        # student Division
        classDiv_label=Label(class_student_frame,text="Class Division:",font=("times new roman",12,"bold italic"))
        classDiv_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)
        
        div_combo=ttk.Combobox(class_student_frame,textvariable=self.var_div,font=("times new roman",12,"bold italic"),width=19,state="readonly")
        div_combo["values"]=("Select Division","A","B","C","D")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=2,pady=5,sticky=W)

        # ROll No
        rollNo_label=Label(class_student_frame,text="Roll No:",font=("times new roman",12,"bold italic"))
        rollNo_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)
        rollNo_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=20,font=("times new roman",12,"bold italic"))
        rollNo_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)


        # Gender
        gender_label=Label(class_student_frame,text="Gender:",font=("times new roman",12,"bold italic"))
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman",12,"bold italic"),width=19,state="readonly")
        gender_combo["values"]=("Select Gender","Male","Female","Others")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=2,pady=5,sticky=W)

        # gender_entry=ttk.Entry(class_student_frame,textvariable=self.var_gender,width=20,font=("times new roman",12,"bold italic"))
        # gender_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)


        # DOB
        DOB_label=Label(class_student_frame,text="DOB:",font=("times new roman",12,"bold italic"))
        DOB_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)
        DOB_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=20,font=("times new roman",12,"bold italic"))
        DOB_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)


         # email
        email_label=Label(class_student_frame,text="email:",font=("times new roman",12,"bold italic"))
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)
        email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=20,font=("times new roman",12,"bold italic"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)


        # Phone No 
        phone_label=Label(class_student_frame,text="Phone:",font=("times new roman",12,"bold italic"))
        phone_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)
        phone_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=20,font=("times new roman",12,"bold italic"))
        phone_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)


        # Address
        address_label=Label(class_student_frame,text="Address:",font=("times new roman",12,"bold italic"))
        address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)
        address_entry=ttk.Entry(class_student_frame,textvariable=self.var_address,width=20,font=("times new roman",12,"bold italic"))
        address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)


        # Teacher Name
        teacherName_label=Label(class_student_frame,text="Teacher Name:",font=("times new roman",12,"bold italic"))
        teacherName_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)
        teacherName_entry=ttk.Entry(class_student_frame,textvariable=self.var_teacher,width=20,font=("times new roman",12,"bold italic"))
        teacherName_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)


        # Radio Buttons
        self.var_radio1=StringVar()
        Radiobutton1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="take Photo Sample",value="Yes")
        Radiobutton1.grid(row=5,column=0)

        Radiobutton2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        Radiobutton2.grid(row=5,column=1)


        # Button Frames
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=200,width=715,height=35)


        save_btn=Button(btn_frame,text="Save",command=self.add_data,font=("times new roman",12,"bold italic"),bg="blue",fg="white",width=19)
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Update",command=self.update_data,font=("times new roman",12,"bold italic"),bg="blue",fg="white",width=19)
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,font=("times new roman",12,"bold italic"),bg="blue",fg="white",width=19)
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,font=("times new roman",12,"bold italic"),bg="blue",fg="white",width=19)
        reset_btn.grid(row=0,column=3)


        # PhotoUpdate Button Frame
        update_btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        update_btn_frame.place(x=0,y=236,width=715,height=35)
        
        take_photo_btn=Button(update_btn_frame,text="Take Photo Sample",command=self.generate_dataset,font=("times new roman",12,"bold italic"),bg="blue",fg="white",width=39)
        take_photo_btn.grid(row=0,column=0)

        update_photo_btn=Button(update_btn_frame,text="Update Photo Sample",font=("times new roman",12,"bold italic"),bg="blue",fg="white",width=39)
        update_photo_btn.grid(row=0,column=1)

        

        # right label frame
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details", font=("times new roman",12,"bold italic"))
        right_frame.place(x=740,y=10,width=730,height=580)

        # img_right=Image.open("__Image Path__")
        # img_right=img_right.resize((720,130),Image.Resampling.LANCZOS)
        # self.photoimg_right=ImageTk.PhotoImage(img_right)

        # f_lbl=Label(right_frame,image=self.photoimg_right)
        # f_lbl.place(x=5,y=0,width=720,height=130)



        # =========Search System==============
        search_frame=LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="Search System", font=("times new roman",12,"bold italic"))
        search_frame.place(x=5,y=135,width=710,height=70)


        search_label=Label(search_frame,text="Search By:",font=("times new roman",15,"bold italic"),bg="red",fg="white")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        
        search_combo=ttk.Combobox(search_frame,font=("times new roman",12,"bold italic"),width=15,state="readonly")
        search_combo["values"]=("Select","StudentID","Name","email","Address","Roll_No","Phone_No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_entry=ttk.Entry(search_frame,width=17,font=("times new roman",12,"bold italic"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        search_btn=Button(search_frame,text="Search",font=("times new roman",12,"bold italic"),bg="blue",fg="white",width=13)
        search_btn.grid(row=0,column=3,padx=4)

        showAll_btn=Button(search_frame,text="Show All",font=("times new roman",12,"bold italic"),bg="blue",fg="white",width=13)
        showAll_btn.grid(row=0,column=4,padx=4)


        # ============Table Frame==============
        table_frame=LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=210,width=710,height=350)

        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)


        self.student_table = ttk.Treeview(table_frame,columns=("course","dep","year","sem","id","name","roll","gender","div","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("course",text="Course")
        self.student_table.heading("dep",text="Department")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentId")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("roll",text="Roll")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"

        self.student_table.column("course",width=100)
        self.student_table.column("dep",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=100)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_Cursor)
        self.fetch_data()
    
    # ===========function Declaration====================
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_course.get()=="Select Course" or self.var_year.get()=="Select Year" or self.var_semester.get()=="Select Semester" or self.var_std_id=="":
        # or self.var_std_id.get()=="" or self.var_std_name=="" or self.var_roll.get()=="" or self.var_gender.get()=="" or self.var_dob.get()=="" or self.var_email.get()=="" or self.var_phone.get()=="" or self.var_address.get()=="" or self.var_teacher.get()==""
            messagebox.showerror("Error","All fields required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",port=3307,username="root",password="ILOVEammi@786",database="face_recognition")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into Student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                        self.var_course.get(),
                                                                                                        self.var_dep.get(),
                                                                                                        self.var_year.get(),
                                                                                                        self.var_semester.get(),
                                                                                                        self.var_std_id.get(),
                                                                                                        self.var_std_name.get(),
                                                                                                        self.var_div.get(),
                                                                                                        self.var_roll.get(),
                                                                                                        self.var_gender.get(),
                                                                                                        self.var_dob.get(),
                                                                                                        self.var_email.get(),
                                                                                                        self.var_phone.get(),
                                                                                                        self.var_address.get(),
                                                                                                        self.var_teacher.get(),
                                                                                                        self.var_radio1.get()
                                                                                                    ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("success","Student details has been added successfully...",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

    # ============Fetch Data=============
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",port=3307,username="root",password="ILOVEammi@786",database="face_recognition")
        my_cursor=conn.cursor()
        my_cursor.execute("Select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    
    # ===================Get Cursor===============
    def get_Cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_course.set(data[0])
        self.var_dep.set(data[1])
        self.var_year.set(data[2])
        self.var_semester.set(data[3])
        self.var_std_id.set(data[4])
        self.var_std_name.set(data[5])
        self.var_div.set(data[6])
        self.var_roll.set(data[7])
        self.var_gender.set(data[8])
        self.var_dob.set(data[9])
        self.var_email.set(data[10])
        self.var_phone.set(data[11])
        self.var_address.set(data[12])
        self.var_teacher.set(data[13])
        self.var_radio1.set(data[14])


    # ==============Update Function=================
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_course.get()=="Select Course" or self.var_year.get()=="Select Year" or self.var_semester.get()=="Select Semester":
            messagebox.showerror("Error","All Fields are Required..",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update {var_std_name} details",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",port=3307,username="root",password="ILOVEammi@786",database="face_recognition")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set course=%s,dep=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where student_id=%s",(
                                                                        self.var_course.get(),
                                                                        self.var_dep.get(),
                                                                        self.var_year.get(),
                                                                        self.var_semester.get(),
                                                                        self.var_std_name.get(),
                                                                        self.var_div.get(),
                                                                        self.var_roll.get(),
                                                                        self.var_gender.get(),
                                                                        self.var_dob.get(),
                                                                        self.var_email.get(),
                                                                        self.var_phone.get(),
                                                                        self.var_address.get(),
                                                                        self.var_teacher.get(),
                                                                        self.var_radio1.get(),
                                                                        self.var_std_id.get()
                                                                    ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Student Details Successfully Updated",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)


    # ===========Delete Function=================
    def delete_data(self,event=""):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do You want to delete this Student",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",port=3307,username="root",password="ILOVEammi@786",database="face_recognition")
                    my_cursor=conn.cursor()
                    sql="delete from student where student_id=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted student details",parent=self.root)

            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

# ===========Reset function=============
    def reset_data(self):
        self.var_course.set("Select Course")
        self.var_dep.set("Select Department")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Select Gender")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")


    # ==================Generate Data Set or Take Photo Samples=======================
        
    
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_course.get()=="Select Course" or self.var_year.get()=="Select Year" or self.var_semester.get()=="Select Semester":
            messagebox.showerror("Error","All Fields are Required..",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",port=3307,username="root",password="ILOVEammi@786",database="face_recognition")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myResult=my_cursor.fetchall()
                id=self.var_std_id.get()
                # for x in myResult:
                #     id+=1
                my_cursor.execute("update student set course=%s,dep=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where student_id=%s",(
                                                                self.var_course.get(),
                                                                self.var_dep.get(),
                                                                self.var_year.get(),
                                                                self.var_semester.get(),
                                                                self.var_std_name.get(),
                                                                self.var_div.get(),
                                                                self.var_roll.get(),
                                                                self.var_gender.get(),
                                                                self.var_dob.get(),
                                                                self.var_email.get(),
                                                                self.var_phone.get(),
                                                                self.var_address.get(),
                                                                self.var_teacher.get(),
                                                                self.var_radio1.get(),
                                                                self.var_std_id.get()
                                                            ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()


            # ============Load predefined data on face frontals from OpenCV========================
                
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    # Scaling factor=1.3
                    # Minimum Neighbour=5

                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(550,550))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="Data/user."+ id +"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data set Completed!!!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)





if __name__=="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()