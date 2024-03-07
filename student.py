from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox,simpledialog
import mysql.connector
from datetime import datetime
import qrcode
import csv
import os
import cv2

class student:
    def __init__(self,root):


        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Student_Managment_system")
        self.root.iconbitmap(r"E:\python\facerecon\image\learn.ico")
        bg_label=Label(self.root)
        bg_label.place(x=0,y=0,width=1530,height=800)


        #==========================variables====================
        
        
        self.var_dep=StringVar()
        self.var_course=StringVar() 
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
        self.var_search=StringVar()





        title_lb=Label(bg_label,text="Student Managment System",font=("times new roman",35,"bold"),bg="#EDEDED",fg="dark green")
        title_lb.place(x=0,y=0,width=1530,height=80)
        main_frame=Frame(bg_label,bd=2)
        main_frame.place(x=0,y=80,width=1500,height=700)



        rightf=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Detials",font=("times new roman",30,"bold"))
        rightf.place(x=750,y=0,width=749,height=670)


         
         
        leftf=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Edit",font=("times new roman",30,"bold"))
        leftf.place(x=10,y=0,width=730,height=670)
        
        img=Image.open(r"E:\python\facerecon\image\OIP (3).jpg")
        img = img.resize((720, 155), Image.ANTIALIAS if hasattr(Image, 'ANTIALIAS') else Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)
        _lb=Label(leftf,image=self.photoimg)
        _lb.place(x=5,y=0,width=720,height=155)

        #======================current course===============================================
        current_c=LabelFrame(leftf,bd=2,relief=RIDGE,text="Current Course Information",font=("times new roman",20,"bold"))
        current_c.place(x=5,y=155,width=720,height=200)

        dep_label=Label(current_c,text="Department",font=("times new roman",13,"bold"))
        dep_label.grid(row=0,column=0,padx=10)

        dep_combo=ttk.Combobox(current_c,textvariable=self.var_dep,font=("times new roman",12,"bold"),state="read olny")
        dep_combo["values"]=("Select Department","IT","Civil","Mechanical","Management")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10)
        
        course_l=Label(current_c,text="course",font=("times new roman",12,"bold"),)
        course_l.grid(row=0,column=2,padx=10,sticky=W)

        course_combo=ttk.Combobox(current_c,textvariable=self.var_course,font=("times new roman",12,"bold"),state="read only")
        course_combo["values"]=("Select Course","Electric Engineer","BHM","Select Course","Bachelor of Computer Application (BCA)","Bachelor of Information Technology (BIT)","Bachelor of Pharmacy (BPharm)","Bachelor of Nursing (BN)","Bachelor of Education (BEd)","Bachelor of Engineering (BE)","Bachelor of Business Administration (BBA)","Bachelor of Commerce (BCom)","Bachelor of Arts (BA)")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=10,sticky=W)

        year_l=Label(current_c,text="Year",font=("times new roman",12,"bold"),)
        year_l.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_c,textvariable=self.var_year,font=("times new roman",12,"bold"),state="read only")
        year_combo["values"]=("select year","2020-21","2021-22","2022-23","2023-24","2024-25")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,sticky=W)           
                       
        

        semester_l=Label(current_c,text="Semester",font=("times new roman",12,"bold"),)
        semester_l.grid(row=1,column=2,padx=10,sticky=W)

        semester_combo=ttk.Combobox(current_c,textvariable=self.var_semester,font=("times new roman",12,"bold"),state="read only")
        semester_combo["values"]=("Select Semester","Semester-1","Semester-2","Semester-3","Semester-4","Semester-5","Semester-6","Semester-7","Semester-8")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=10,sticky=W)           

        #==========class  info=============================================
        class_c=LabelFrame(leftf,bd=2,relief=RIDGE,text="Class Student Information",font=("times new roman",20,"bold"))
        class_c.place(x=5,y=280,width=720,height=335)


        clsd_l=Label(class_c,text="Class Division:",font=("times new roman",12,"bold"))
        clsd_l.grid(row=1,column=0,padx=10,sticky=W)

               
        studentid_l=Label(class_c,text="StudentID:",font=("times new roman",12,"bold"))
        studentid_l.grid(row=0,column=0,padx=10,sticky=W)
        studentE=ttk.Entry(class_c,textvariable=self.var_std_id,width=20,font=("times new roman",12,"bold"))
        studentE.grid(row=0,column=1,padx=10,sticky=W)

        studentN_l=Label(class_c,text="Student Name:",font=("times new roman",12,"bold"))
        studentN_l.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        studentNE=ttk.Entry(class_c,textvariable=self.var_std_name,width=20,font=("times new roman",12,"bold"))
        studentNE.grid(row=0,column=3,padx=10,sticky=W)

        roll_l=Label(class_c,text="Roll No:",font=("times new roman",12,"bold"))
        roll_l.grid(row=1,column=2,padx=10,pady=5,sticky=W)
        roll=ttk.Entry(class_c,textvariable=self.var_roll,width=20,font=("times new roman",12,"bold"))
        roll.grid(row=1,column=3,padx=10,sticky=W)



        gender_l=Label(class_c,text="Gender:",font=("times new roman",12,"bold"))
        gender_l.grid(row=2,column=0,padx=10,pady=5,sticky=W)
      
        
        div_combo=ttk.Combobox(class_c,textvariable=self.var_div,font=("times new roman",12,"bold"),state="read only",width=18)
        div_combo["values"]=("A","B","C")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=10,pady=10,sticky=W)  
        
        gender_combo=ttk.Combobox(class_c,textvariable=self.var_gender,font=("times new roman",12,"bold"),state="read only",width=18)
        gender_combo["values"]=("Select","Male","Female","Others")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=10,sticky=W) 


        dob_l=Label(class_c,text="Date Of Birth:",font=("times new roman",12,"bold"))
        dob_l.grid(row=2,column=2,padx=10,pady=5,sticky=W)
        dolE=ttk.Entry(class_c,textvariable=self.var_dob,width=20,font=("times new roman",12,"bold"))
        dolE.grid(row=2,column=3,padx=10,sticky=W)


        email_l=Label(class_c,text="Email:",font=("times new roman",12,"bold"))
        email_l.grid(row=3,column=0,padx=10,pady=5,sticky=W)
        emailE=ttk.Entry(class_c,textvariable=self.var_email,width=20,font=("times new roman",12,"bold"))
        emailE.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        
        
        phone_l=Label(class_c,text="Phone No:",font=("times new roman",12,"bold"))
        phone_l.grid(row=3,column=2,padx=10,pady=5,sticky=W)
        phoneE=ttk.Entry(class_c,textvariable=self.var_phone,width=20,font=("times new roman",12,"bold"))
        phoneE.grid(row=3,column=3,padx=10,pady=5,sticky=W)



        
        address_l=Label(class_c,text="Address:",font=("times new roman",12,"bold"))
        address_l.grid(row=4,column=0,padx=10,pady=5,sticky=W)
        addresE=ttk.Entry(class_c,textvariable=self.var_address,width=20,font=("times new roman",12,"bold"))
        addresE.grid(row=4,column=1,padx=10,pady=5,sticky=W)



        teacher_l=Label(class_c,text="Teacher:",font=("times new roman",12,"bold"))
        teacher_l.grid(row=4,column=2,padx=10,pady=5,sticky=W)
        teacherE=ttk.Entry(class_c,textvariable=self.var_teacher,width=20,font=("times new roman",12,"bold"))
        teacherE.grid(row=4,column=3,padx=10,pady=5,sticky=W)

        self.var_radio1=StringVar()
        Radiobutn=ttk.Radiobutton(class_c,variable=self.var_radio1,text="Take sample photo",value="yes")
        Radiobutn.grid(row=5,column=0,pady=6)

        Radiobutn=ttk.Radiobutton(class_c,variable=self.var_radio1,text="No sample photo",value="no")
        Radiobutn.grid(row=5,column=1,pady=6)

        bframe=Frame(class_c,bd=2,relief=RIDGE)
        bframe.place(x=0,y=230,width=715,height=40)

        save=Button(bframe,text="Save",command=self.data,width=18,font=("times new roman",12,"bold"),bg="blue",fg="white")
        save.grid(row=0,column=0,padx=5)

        update=Button(bframe,text="Update",command=self.update,width=18,font=("times new roman",12,"bold"),bg="blue",fg="white")
        update.grid(row=0,column=1,padx=5)


        delete=Button(bframe,text="Delete",command=self.delete,width=18,font=("times new roman",12,"bold"),bg="blue",fg="white")
        delete.grid(row=0,column=2,padx=5)


        reset=Button(bframe,text="Reset",command=self.reset,width=18,font=("times new roman",12,"bold"),bg="blue",fg="white")
        reset.grid(row=0,column=3,padx=5)


        b2frame=Frame(class_c,bd=2,relief=RIDGE)
        b2frame.place(x=0,y=270,width=715,height=45)


        take=Button(b2frame,command=self.register,text="QR generator",width=40,font=("times new roman",12,"bold"),bg="blue",fg="white")
        take.grid(row=1,column=0,padx=5)

        
        take1=Button(b2frame,command=self.open_camera_app,text="Take sample photo",width=40,font=("times new roman",12,"bold"),bg="blue",fg="white")
        take1.grid(row=1,column=1,padx=5)
        
        #====================left frame============================================
        search=LabelFrame(rightf,bd=2,relief=RIDGE,text="filtering",font=("times new roman",18,"bold"))
        search.place(x=0,y=0,width=746,height=70)

        search_l=Label(search,text="Search By:",font=("times new roman",12,"bold"),fg="white",bg="dark green")
        search_l.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        
        search_combo=ttk.Combobox(search,font=("times new roman",12,"bold"),state="read only")
        search_combo["values"]=("Select","Roll No","Phone Number")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,sticky=W)  

        searchE=ttk.Entry(search,textvariable=self.var_search,width=20,font=("times new roman",12,"bold"))
        searchE.grid(row=0,column=2,padx=10,pady=5,sticky=W)


        
        search_but=Button(search,text="Search",command=self.search,width=12,font=("times new roman",12,"bold"),bg="blue",fg="white")
        search_but.grid(row=0,column=3,padx=5)


        showall=Button(search,text="Show All",command=self.fetch,width=12,font=("times new roman",12,"bold"),bg="blue",fg="white")
        showall.grid(row=0,column=4,padx=5)


        tabelf=Frame(rightf,bd=2,relief=RIDGE)
        tabelf.place(x=0,y=75,width=746,height=550)
    


        scroll_x=ttk.Scrollbar(tabelf,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(tabelf,orient=VERTICAL)
        self.student_table=ttk.Treeview(tabelf,column=("dep","course","year","sem","id","name","roll","gender","div","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)


        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year",text="Year") 
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id", text="StudentId") 
        self.student_table.heading("name", text="Name")
        self.student_table.heading("roll", text="Division") 
        self.student_table.heading("gender", text="rollno") 
        self.student_table.heading("div", text="Gender") 
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("email", text="Email") 
        self.student_table.heading("phone", text="Phone")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("teacher", text="Teacher")
        self.student_table.heading("photo", text="PhotoSampleStatus") 
        self.student_table["show"]="headings"
        self.student_table.pack (fill=BOTH, expand=1)

        
        self.student_table.column("dep",width=80)
        self.student_table.column("course", width=180) 
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("roll", width=100)
        self.student_table.column("gender", width=100) 
        self.student_table.column("div",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=150)
        self.student_table.column("phone", width=100)
        self.student_table.column("address", width=100)
        self.student_table.column("teacher", width=100)
        self.student_table.column("photo", width=100)
        self.student_table.bind("<ButtonRelease>", self.cursor)
        self.fetch()
#=====================function==============================

    def data(self):
        if self.var_dep.get()=='select Department' or self.var_std_name.get()=="" or self.var_std_id.get=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Nabin(123)",database="facerecon")
                my_cursor=conn.cursor()
                my_cursor.execute("INSERT INTO studentS VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (
    self.var_dep.get(),
    self.var_course.get(),
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
                self.fetch()
                conn.close()
                messagebox.showinfo("Sucessfull","Sucessfully added")
            except Exception as e:
                messagebox.showinfo("Error",f"Due to: {e}",parent=self.root)

#=================================fetching==================================
    def fetch(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Nabin(123)",database="facerecon")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from students")
        data=my_cursor.fetchall()
        if len(data)!=0:
            self.student_table.delete(* self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
            conn.close()
#=================================get cursor===============================
    def cursor(self,event=""):
        cursor_focus = self.student_table.focus() 
        content = self.student_table.item(cursor_focus)
        data=content["values"]


        self.var_dep.set(data[0])
        self.var_course.set(data[1]), 
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]), 
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data [11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data [13]),
        self.var_radio1.set(data[14])

    def update(self):
        if self.var_dep.get() == 'select Department' or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                update = messagebox.askyesno("update", "do you want to update the student details", parent=self.root)
                if update > 0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="Nabin(123)", database="facerecon")
                    my_cursor = conn.cursor()
                    my_cursor.execute("UPDATE students SET Dep=%s, course=%s, Year=%s, Semester=%s, Name=%s, Division=%s, Roll_No=%s, Gender=%s, Dob=%s, Email=%s, Phone_No=%s, Address=%s, Teacher=%s, photosampel=%s WHERE student_id=%s", (self.var_dep.get(), self.var_course.get(), self.var_year.get(), self.var_semester.get(), self.var_std_name.get(), self.var_div.get(), self.var_roll.get(), self.var_gender.get(), self.var_dob.get(), self.var_email.get(), self.var_phone.get(), self.var_address.get(), self.var_teacher.get(), self.var_radio1.get(), self.var_std_id.get()))
                else:
                    if not update:
                        return
                messagebox.showinfo("Successful", "student detail successfully updated")
                conn.commit()
                conn.close()
            except Exception as e:
                print(e)

                messagebox.shwerror("Error", f"Due to: {e}", parent=self.root)



    def search(self):
        search_text = self.var_search.get()

        try:
            conn = mysql.connector.connect(host="localhost", username="root", password="Nabin(123)", database="facerecon")
            my_cursor = conn.cursor()

            # Execute a query to search across multiple fields
            my_cursor.execute("SELECT * FROM students WHERE student_id = %s OR Name = %s OR Dep = %s OR course = %s OR Year = %s OR Semester = %s OR Division = %s OR Roll_No = %s OR Gender = %s OR Dob = %s OR Email = %s OR Phone_No = %s OR Address = %s OR Teacher = %s OR photosampel = %s",
                              (search_text, search_text, search_text, search_text, search_text, search_text, search_text, search_text, search_text, search_text, search_text, search_text, search_text, search_text, search_text))

            search_results = my_cursor.fetchall()

            conn.close()

            if search_results:
                # Call the fetch function to populate the tree view with search results
                self.populate_tree_view(search_results)
            else:
                messagebox.showinfo("Information", "No matching records found")

        except Exception as e:
            print(e)
            messagebox.showerror("Error", f"Due to: {e}", parent=self.root)

    def populate_tree_view(self, data):
        # Clear existing tree view data
        for item in self.student_table.get_children():
            self.student_table.delete(item)

        # Populate tree view with new data
        for row in data:
            self.student_table.insert('', 'end', values=row)

    #=====================delete===================================
    def delete(self):
       if self.var_std_id.get() == "":
           messagebox.showerror("Error", "Student id must be required", parent=self.root)
       else:
           try:
               delete = messagebox.askyesno("Student Delete", "Do you want to remove the student details", parent=self.root)
               if delete:
                   conn = mysql.connector.connect(host="localhost", username="root", password="Nabin(123)", database="facerecon")
                   my_cursor = conn.cursor()
                   sql = "DELETE FROM students WHERE student_id=%s"
                   val = (self.var_std_id.get(),)
                   my_cursor.execute(sql, val)
               else:
                   return
               conn.commit()
               self.fetch()
               conn.close()
               messagebox.showinfo("Delete", "Successfully deleted", parent=self.root)
           except Exception as e:
               print(e)
               messagebox.showerror("Error", f"Due to: {e}", parent=self.root)

#=================rest======================
    def reset(self):
        self.var_dep.set("Select Department") 
        self.var_course.set("Select Course") 
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Male")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")

#===================== photo sampel===================
    
    def open_camera_app(self):
 
        save_directory = r"C:\Users\reymn\Desktop\project\data"
      
        filename = simpledialog.askstring("Input", "Enter student name (without extension):")
        if filename is None:
            messagebox.showerror("Error", "No file name provided.",parent=self.root)
            return
        filename = os.path.join(save_directory, filename + ".jpg")
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            messagebox.showerror("Error:","Could not open camera.",parent=self.root)
            return
        ret, frame = cap.read()
        if not ret:
            messagebox.showerror("Error", " Could not capture photo.",parent=self.root)
            cap.release()
            return
        cv2.imshow("Captured Image", frame)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        cv2.imwrite(filename, frame)
        print(f"Image captured and saved as {filename}")
        cap.release()
        
        

    
    def register(self):
       if self.var_std_id.get() == "":
           messagebox.showerror("Error", "Student id must be required", parent=self.root)
       else:
           try:
               id = self.var_std_id.get()
               roll_no = self.var_roll.get()
               name = self.var_std_name.get()
               course = self.var_dep.get()
               time = datetime.now().strftime("%H:%M:%S")
               date = datetime.now().strftime("%d/%m/%Y")
               status = "Present"
               
               csv_folder = r"C:\Users\reymn\Desktop\project\csv"
               os.makedirs(csv_folder, exist_ok=True)
               
               csv_filename = os.path.join(csv_folder, "registration_data.csv")

               # Append data to CSV file
               with open(csv_filename, 'a', newline='') as csvfile:
                   writer = csv.writer(csvfile)
                   writer.writerow([id, roll_no, name, course, time, date, status]) 
                   
               qr_folder = "qrcodes"
               os.makedirs(qr_folder, exist_ok=True)
               
               # Generate QR Code
               qr = qrcode.QRCode(
                   version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_L,
                   box_size=10,
                   border=4,
               )
               qr.add_data(f"{id},{roll_no},{name},{course},{time},{date},{status}") 
               qr.make(fit=True)
               timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
               qr_img = qr.make_image(fill_color="black", back_color="white")
               qr_img.save(f"{qr_folder}/registration_qr_{id}_{timestamp}.png")
       
               messagebox.showinfo("Generated successfully", f"QR code generated in {qr_folder}/registration_qr_{id}_{timestamp}.png", parent=self.root)
           except Exception as e:
               messagebox.showerror("Error", f"Due to {e}", parent=self.root)
    
    
                            
        
        
                


    




       
        





if __name__=="__main__":
    root=Tk()
    object=student(root)
    root.mainloop()