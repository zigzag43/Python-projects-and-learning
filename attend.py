from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import csv
from tkinter import filedialog
import os
mydata=[]
class attend:
    def __init__(self,root):


        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Student_Attendence")
        self.root.configure(bg="#FFFDE8")
        self.root.iconbitmap(r"E:\python\facerecon\image\student.ico")
        bg_label=Label(self.root)
        bg_label.place(x=0,y=0,width=1530,height=800)


        #=====text variable=====================
       
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()






        title_lb=Label(bg_label,text="Attendance",font=("times new roman",35,"bold"),bg="#FFFDE8",fg="dark green")
        title_lb.place(x=0,y=0,width=1530,height=90)
        main_frame=Frame(bg_label,bd=2,bg="#FFFDE8")
        main_frame.place(x=0,y=90,width=1539,height=700)

        def on_mousewheel(event):
             self.student_table.yview_scroll(int(-1*(event.delta/120)), "units")
             
             
        

        rightf=LabelFrame(main_frame,bd=1,relief=RIDGE,text="General Detials",font=("times new roman",30,"bold"),bg="#FFFDE8",fg="dark green")
        rightf.place(x=720,y=0,width=770,height=670)


         
         
        leftf=LabelFrame(main_frame,bd=1,relief=RIDGE,text="Edit",font=("times new roman",30,"bold"),bg="#FFFDE8",fg="dark green")
        leftf.place(x=10,y=150,width=700,height=500)

        img=Image.open(r"E:\python\facerecon\image\cover-image-facebook-stories.jpg")
        img = img.resize((645, 235), Image.ANTIALIAS if hasattr(Image, 'ANTIALIAS') else Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)
        _lb=Label(root,image=self.photoimg)
        _lb.place(x=5,y=0,width=645,height=235)

                 
        studentid_l=Label(leftf,text="StudentID:",font=("times new roman",12,"bold"))
        studentid_l.grid(row=0,column=0,padx=10,sticky=W)
        studentE=ttk.Entry(leftf,textvariable=self.var_atten_id,width=20,font=("times new roman",12,"bold"))
        studentE.grid(row=0,column=1,padx=10,pady=40,sticky=W)


        name=Label(leftf,text="Name:",font=("times new roman",12,"bold"))
        name.grid(row=0,column=2,padx=10,sticky=W)
        name=ttk.Entry(leftf,width=20,textvariable=self.var_atten_name,font=("times new roman",12,"bold"))
        name.grid(row=0,column=3,padx=10,pady=40,sticky=W)


               

        roll=Label(leftf,text="Roll No:",font=("times new roman",12,"bold"))
        roll.grid(row=1,column=0,padx=10,sticky=W)
        roll=ttk.Entry(leftf,textvariable=self.var_atten_roll,width=20,font=("times new roman",12,"bold"))
        roll.grid(row=1,column=1,padx=10,pady=40,sticky=W)
        
        
        dep=Label(leftf,text="Deparment:",font=("times new roman",12,"bold"))
        dep.grid(row=1,column=2,padx=10,sticky=W)
        depE=ttk.Entry(leftf,width=20,textvariable=self.var_atten_dep,font=("times new roman",12,"bold"))
        depE.grid(row=1,column=3,padx=10,pady=40,sticky=W)
        


            
        time=Label(leftf,text="Time:",font=("times new roman",12,"bold"))
        time.grid(row=2,column=0,padx=10,sticky=W)
        time=ttk.Entry(leftf,textvariable=self.var_atten_time,width=20,font=("times new roman",12,"bold"))
        time.grid(row=2,column=1,padx=10,pady=40,sticky=W)



                  
        date=Label(leftf,text="date:",font=("times new roman",12,"bold"))
        date.grid(row=2,column=2,padx=10,sticky=W)
        date=ttk.Entry(leftf,textvariable=self.var_atten_date,width=20,font=("times new roman",12,"bold"))
        date.grid(row=2,column=3,padx=10,pady=40,sticky=W)


        
        attan=Label(leftf,text="Attendance:",font=("times new roman",12,"bold"))
        attan.grid(row=3,column=0,padx=10,sticky=W)
        
        att=ttk.Combobox(leftf,textvariable=self.var_atten_attendance,font=("times new roman",12,"bold"),state="read only")
        att["values"]=("Status","Present","Absent")
        att.grid(row=3,column=1,padx=10,sticky=W)  


        bframe=Frame(leftf,bg="#FFFDE8",bd=2,relief=RIDGE)
        bframe.place(x=0,y=380,width=715,height=100)

        impo=Button(bframe,command=self.importcsv,text="Import",width=18,font=("times new roman",12,"bold"),bg="blue",fg="white")
        impo.grid(row=0,column=0,padx=5)

        update=Button(bframe,command=self.update_csv,text="Update",width=18,font=("times new roman",12,"bold"),bg="blue",fg="white")
        update.grid(row=0,column=1,padx=5)


        export=Button(bframe,text="Export",command=self.exportcsv,width=18,font=("times new roman",12,"bold"),bg="blue",fg="white")
        export.grid(row=0,column=2,padx=5)


        reset=Button(bframe,text="Reset",command=self.reset_dat,width=18,font=("times new roman",12,"bold"),bg="blue",fg="white")
        reset.grid(row=0,column=3,padx=5)  

        delete=Button(bframe,text="Delete",command=self.delete_row,width=18,font=("times new roman",12,"bold"),bg="blue",fg="white")
        delete.grid(row=1,column=0,padx=0,pady=5)       

        
        add=Button(bframe,text="Add",command=self.add,width=18,font=("times new roman",12,"bold"),bg="blue",fg="white")
        add.grid(row=1,column=1,padx=0,pady=5)    
  

        tabelf=Frame(rightf,bd=2,relief=RIDGE)
        tabelf.place(x=0,y=0,width=770,height=600)
    
        
 
        scroll_x=ttk.Scrollbar(tabelf,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(tabelf,orient=VERTICAL)
        self.student_table=ttk.Treeview(tabelf,column=("Id","Name","roll","Dep","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.bind("<MouseWheel>", on_mousewheel)



        self.student_table.heading("Id", text="StudentId", anchor="center")
        self.student_table.heading("Name", text="Roll no", anchor="center")
        self.student_table.heading("roll", text="Name", anchor="center")
        self.student_table.heading("Dep", text="Department", anchor="center")
        self.student_table.heading("time", text="Time", anchor="center")
        self.student_table.heading("date", text="Date", anchor="center")
        self.student_table.heading("attendance", text="Attendance", anchor="center")

        self.student_table["show"]="headings"
        self.student_table.pack (fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
    


    def fetchdata(self,rows):
        self.student_table.delete(*self.student_table.get_children())
        for i in rows:
            self.student_table.insert("",END,values=i)


    def importcsv(self):
        global mydata
        mydata.clear()
        fl = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File", "*.csv"), ("All Files", "*.*")), parent=self.root)
        with open(fl) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchdata(mydata)


    # def importauto(self):
    #     global mydata
    #     mydata.clear()
    #     path = r"c:\Users\reymn\Desktop\project\attendence.csv" 
    #     try:
    #         with open(path) as myfile:
    #             csvread = csv.reader(myfile, delimiter=",")
    #             for row in csvread:
    #                 mydata.append(row)
    #         self.fetchdata(mydata)
    #     except Exception as e:
    #         messagebox.showerror("Error", f"An error occurred while importing the CSV file: {e}")

   
    
    def exportcsv(self):
        try:
            if not mydata:  
                messagebox.showwarning("No Data", "No data found to export", parent=self.root)
                return False
    
            fl = filedialog.asksaveasfilename(
                initialdir=os.getcwd(),
                title="Save CSV",
                defaultextension=".csv",
                filetypes=(("CSV File", "*.csv"), ("All Files", "*.*")),
                parent=self.root
            )
    
            if fl:
                with open(fl, mode="w", newline='') as myfile:
                    exp_write = csv.writer(myfile, delimiter=",")
                    for row in mydata:
                        exp_write.writerow(row)
                messagebox.showinfo("Successful", f"Exported successfully to {os.path.basename(fl)}")
    
        except Exception as e:
            messagebox.showerror("Error", f"Due to: {str(e)}", parent=self.root)
    

    def get_cursor(self,event=""):
        try:

            cursor_row=self.student_table.focus()
            content=self.student_table.item(cursor_row)
            rows=content['values']
            self.var_atten_id.set(rows[0])
            self.var_atten_roll.set(rows[1])
            self.var_atten_name.set(rows[2])
            self.var_atten_dep.set(rows[3])
            self.var_atten_time.set(rows[4])
            self.var_atten_date.set(rows[5])
            self.var_atten_attendance.set(rows[6])

        except Exception as e:
            print("")

    def reset_dat(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")

    



    def update_csv(self):
        selected_item = self.student_table.focus()
        values = self.student_table.item(selected_item, "values")  
        if not values:
            return  
        
        # Retrieve the values from entry variables
        studentid = self.var_atten_id.get()
        name = self.var_atten_name.get()
        roll = self.var_atten_roll.get()
        time = self.var_atten_time.get()
        dep = self.var_atten_dep.get()
        date = self.var_atten_date.get()
        attendance = self.var_atten_attendance.get()
        
        self.student_table.item(selected_item, values=(studentid, roll, name, dep, time, date, attendance))
        
        with open(r"C:\Users\reymn\Desktop\project\attendance.csv", mode='r', newline='') as file:
            reader = csv.reader(file)
            data = list(reader)
        with open(r"C:\Users\reymn\Desktop\project\attendance.csv", mode='w', newline='') as file:
            writer = csv.writer(file)
            for row in data:
                if row[0] == values[0]:  # Check if the student id matches the selected item
                    writer.writerow([studentid, roll, name, dep, time, date, attendance])
                else:
                    writer.writerow(row)

    import csv

    def add(self):
        try:
            csv_file=r"C:\Users\reymn\Desktop\project\attendence.csv"
            studentid = self.var_atten_id.get()
            name = self.var_atten_name.get()
            roll = self.var_atten_roll.get()
            time = self.var_atten_time.get()
            dep = self.var_atten_dep.get()
            date = self.var_atten_date.get()
            attendance = self.var_atten_attendance.get()
            
    
            with open(csv_file, mode='r', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row and row[0] == studentid:  
                        messagebox.showinfo("Error","Cannot be same Id",parent=self.root)
        
      
            with open(csv_file, mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([studentid,  roll,name, dep,time,  date, attendance])   
                messagebox.showinfo("sucessfull","added sucessfully",parent=self.root)
            self.importauto()
           
            
        except Exception as e:
            print(f"Error appending record to CSV file: {e}")
            return False
           




    



    def delete_row(self):
            selected_item = self.student_table.focus()  # Get the selected item
            values = self.student_table.item(selected_item, "values")  # Get the values of the selected item
            if not values:
                return  # If no item is selected, return
    
            # Read the existing data from the CSV file
            with open(r"C:\Users\reymn\Desktop\project", mode='r', newline='') as file:
                reader = csv.reader(file)
                data = list(reader)
    
            # Remove the selected row from the data list
            data = [row for row in data if row[0] != values[0]]  # Exclude the row with the selected student id
    
            # Update the CSV file with the modified data
            with open(r"E:\python\facerecon\attendence.csv", mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(data)
    
            # Remove the selected row from the table
            self.student_table.delete(selected_item)
    



if __name__=="__main__":
    root=Tk()
    
    object=attend(root) 
    
    root.mainloop()