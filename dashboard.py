from tkinter import*
from PIL import Image,ImageTk #pip install pillow
from course import CourseClass
from student import StudentClass
from result import resultClass
from report import reportClass
from tkinter import messagebox
import sqlite3
import os
class RNS:
    def __init__(self,root):
        self.root = root
        self.root.title("School Result Management System")
        self.root.geometry("1350x640+0+0")
        self.root.config(bg = "white")
        #===icons===
        self.logo_dash=ImageTk.PhotoImage(file="images/diu_logo.png")
        
        
        #===title===
        title=Label(self.root,text="School Result Management System",padx=10,compound=LEFT,image=self.logo_dash,font=("goudy old style",20,"bold"),bg="#033054",fg="white").place(x=0,y=0,relwidth=1,height=50)
        #===Menu===
        M_Frame=LabelFrame(self.root,text="Menu",font=("times new roman",15),bg="white")
        M_Frame.place(x=10,y=60,width=1340,height=80)
        

        btn_course=Button(M_Frame,text="Course",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_course).place(x=10,y=5,width=180,height=40)
        btn_student=Button(M_Frame,text="Student",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_student).place(x=220,y=5,width=180,height=40)
        btn_result=Button(M_Frame,text="Result",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_result).place(x=430,y=5,width=180,height=40)
        btn_view=Button(M_Frame,text="View Student Result",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_report).place(x=640,y=5,width=180,height=40)
        btn_logout=Button(M_Frame,text="Logout",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.logout).place(x=850,y=5,width=180,height=40)
        btn_exit=Button(M_Frame,text="Exit",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.exit_).place(x=1060,y=5,width=180,height=40)
        
        #====content_window====
        self.bg_img=Image.open("images/bg.png")
        self.bg_img=self.bg_img.resize((900,330),Image.Resampling.LANCZOS)
        self.bg_img=ImageTk.PhotoImage(self.bg_img)

        self.lbl_bg=Label(self.root,image=self.bg_img).place(x=400,y=150,width=920,height=350)

        #===update_details===
        self.lbl_student=Label(self.root,text="Total Students\n[ 0 ]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#e43b06",fg="white")
        self.lbl_student.place(x=400,y=510,width=240,height=70) 

        self.lbl_course=Label(self.root,text="Total Courses\n[ 0 ]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#0676ad",fg="white")
        self.lbl_course.place(x=700,y=510,width=240,height=70) 

        self.lbl_result=Label(self.root,text="Total Results\n[ 0 ]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#038074",fg="white")
        self.lbl_result.place(x=1010,y=510,width=240,height=70) 
            

          
        


        #===footer===
        footer=Label(self.root,text="SRMS-School Result Management System\nContact Us for any Technical Issue: 017xxxxxx08",font=("goudy old style",12),bg="#262626",fg="white").pack(side=BOTTOM,fill=X)
        self.update_details()
    #===================================================
    def update_details(self):
        con=sqlite3.connect(database="rns.db")
        cur=con.cursor() 
        try:
            cur.execute("select * from student")
            cr=cur.fetchall()
            self.lbl_student.config(text=f"Total Students\n[{str(len(cr))}]")
            


            cur.execute("select * from course")
            cr=cur.fetchall()
            self.lbl_course.config(text=f"Total Courses\n[{str(len(cr))}]")

            
            cur.execute("select * from result")
            cr=cur.fetchall()
            self.lbl_result.config(text=f"Total Results\n[{str(len(cr))}]")
            

            self.lbl_course.after(200,self.update_details)        
    
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}") 




    def add_course(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=CourseClass(self.new_win)


    def add_student(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=StudentClass(self.new_win)
    

    def add_result(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=resultClass(self.new_win)

   
    def add_report(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=reportClass(self.new_win)


    def logout(self):
        op=messagebox.askyesno("Confirm","Do you really want to logout?",parent=self.root)
        if op==True:
            self.root.destroy()
            os.system("python login.py")

    def exit_(self):
        op=messagebox.askyesno("Confirm","Do you really want to Exit?",parent=self.root)
        if op==True:
            self.root.destroy()
            
        


   
    def new_method(self):
      self.bg_img=ImageTk.PhotoImage(self.bg_img)

            
        

if __name__ == "__main__":
    root = Tk()
    obj  = RNS(root)
    root.mainloop()
 