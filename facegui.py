from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import Image,ImageTk
from student import student
from attend import attend
import numpy as np
import mysql.connector
import os
import cv2
import webbrowser
from time import strftime
from datetime import datetime
class Face_recon:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face_recognition_system")
        self.root.iconbitmap(r"E:\python\facerecon\image\home.ico")
        

        #=========background img============================
        img4=Image.open(r"E:\python\facerecon\image\4334353_2239760.jpg")
        img4 = img4.resize((1530, 800), Image.ANTIALIAS if hasattr(Image, 'ANTIALIAS') else Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        bg_label=Label(self.root,image=self.photoimg4)
        bg_label.place(x=0,y=0,width=1530,height=800)

        title_lb=Label(bg_label,text=" ATTENDENCE SYSTEM SOFTWARE",font=("times new roman",35,"bold"),bg="#EDEDED",fg="blue")
        title_lb.place(x=0,y=0,width=1530,height=80)
         
        img5=Image.open(r"E:\python\facerecon\image\OIP (1).jpg")
        img5 = img5.resize((220, 220), Image.ANTIALIAS if hasattr(Image, 'ANTIALIAS') else Image.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        b1=Button(bg_label,command=self.student_detials,image=self.photoimg5,cursor="hand2")
        b1.place(x=150,y=100,width=220,height=220)
        b11=Button(bg_label,command=self.student_detials,text="Admit Students",font=("times new roman",18,"bold"),bg="#EDEDED",fg="blue",cursor="hand2")
        b11.place(x=150,y=300,width=220,height=35)

        


              
        img6=Image.open(r"E:\python\facerecon\image\Untitled.jpeg")
        img6 = img6.resize((220, 220), Image.ANTIALIAS if hasattr(Image, 'ANTIALIAS') else Image.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)
        b2=Button(bg_label,image=self.photoimg6,cursor="hand2")
        b2.place(x=1150,y=100,width=220,height=220)
        b22=Button(bg_label,text="Attandance",font=("times new roman",18,"bold"),bg="#EDEDED",fg="blue",cursor="hand2")
        b22.place(x=1150,y=300,width=220,height=35)
        

        img7=Image.open(r"E:\python\facerecon\image\R.png")
        img7 = img7.resize((220, 220), Image.ANTIALIAS if hasattr(Image, 'ANTIALIAS') else Image.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)
        b3=Button(bg_label,command=self.attend_data,image=self.photoimg7,cursor="hand2")
        b3.place(x=1150,y=100,width=220,height=220)
        b33=Button(bg_label,command=self.attend_data,text="Attendance report",font=("times new roman",18,"bold"),bg="#EDEDED",fg="blue",cursor="hand2")
        b33.place(x=1150,y=300,width=220,height=35)
       
        

        img8=Image.open(r"E:\python\facerecon\image\255_Photo-1024.webp")
        img8 = img8.resize((220, 220), Image.ANTIALIAS if hasattr(Image, 'ANTIALIAS') else Image.LANCZOS)
        self.photoimg8=ImageTk.PhotoImage(img8)
        b3=Button(bg_label,command=self.open_folder,image=self.photoimg8,cursor="hand2")
        b3.place(x=150,y=430,width=220,height=220)
        b33=Button(bg_label,command=self.open_folder,text="Photos",font=("times new roman",18,"bold"),bg="#EDEDED",fg="blue",cursor="hand2")
        b33.place(x=150,y=630,width=220,height=35) 


        
     


        img10=Image.open(r"E:\python\facerecon\image\VoiceLogIcons-06.png")
        img10= img10.resize((220, 220), Image.ANTIALIAS if hasattr(Image, 'ANTIALIAS') else Image.LANCZOS)
        self.photoimg10=ImageTk.PhotoImage(img10)
        b3=Button(bg_label,command=self.help,image=self.photoimg10,cursor="hand2")
        b3.place(x=1150,y=430,width=220,height=220)
        b33=Button(bg_label,command=self.help,text="Help & support",font=("times new roman",18,"bold"),bg="#EDEDED",fg="blue",cursor="hand2")
        b33.place(x=1150,y=630,width=220,height=35) 



#========================function buttons========================   
    def student_detials(self):
        self.new_window=Toplevel(self.root)
        self.app=student(self.new_window)

    
    def open_folder(self):
        os.startfile(r"C:\Users\reymn\Desktop\project\data")


    def attendence(self,g,r,n,d):
        with open(r"E:\python\facerecon\attendence.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if((g not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtstring=now.strftime("%H:%M:%S")
                f.writelines(f"\n{g},{r},{n},{d},{dtstring},{d1},Present")
    

       
        


#========================function buttons========================
    def attend_data(self):
        self.new_window=Toplevel(self.root)
        self.app=attend(self.new_window)
        self.app.importauto()

    def help(self):
        top = Toplevel()
        top.title("Help & Support")
      
        

        message =""" Need Help or Support? We're Here for You! 🌟

If you're feeling overwhelmed, struggling with mental health challenges, or need someone to talk to, we're here to support you. 

Please don't hesitate to reach out to us. We understand that everyone goes through tough times, and it's okay to ask for help when you need it. You're not alone in this journey.

Together, we can work through your difficulties and find ways to improve your well-being. Whether it's through a heartfelt conversation, providing resources, or connecting you with professional help, we're committed to assisting you every step of the way.

Your mental health matters to us, and we're dedicated to creating a safe and supportive environment for you to express yourself and seek the assistance you deserve.

Remember, reaching out for help is a sign of strength, and we admire your courage in taking this step. You're important to us, and we're here to help you navigate life's challenges with compassion and understanding.
"""

        label = Label(top, text=message, font=("Helvetica", 13), wraplength=1000, justify="left")
        label.pack(padx=10, pady=10)

        # Function to open WhatsApp number
        def open_whatsapp():
            webbrowser.open("https://wa.me/9779807574687")

        # Function to open email
        def open_email():
            webbrowser.open("mailto:nabintharu773@gmail.com")

        # Create clickable labels for WhatsApp number and email
        whatsapp_label = Label(top, text="📱 WhatsApp Number: +977 9807574687", font=("Helvetica", 14), fg="blue", cursor="hand2")
        whatsapp_label.pack(pady=(0, 5))
        whatsapp_label.bind("<Button-1>", lambda event: open_whatsapp())

        email_label = Label(top, text="📧 Email: nabintharu773@gmail.com", font=("Helvetica", 14), fg="blue", cursor="hand2")
        email_label.pack()
        email_label.bind("<Button-1>", lambda event: open_email())


        



if __name__=="__main__":
    root=Tk()
    object=Face_recon(root)
    root.mainloop()
    