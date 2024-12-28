from tkinter import*
from tkinter import ttk,messagebox
from PIL import Image,ImageTk   #pip install pillow
#import pymysql       #pip install pymysql
import sqlite3
import os
class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Registration Window") 
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")    
        #=======bg================
        self.bg=ImageTk.PhotoImage(file="image/bgg.jpg")
        bg=Label(self.root,image=self.bg).place(x=250,y=0,relwidth=1,relheight=1)

        #Register Frame=======
        frame1=Frame(self.root,bg="white")
        frame1.place(x=480,y=100,width=700,height=500)
        #=====Title======
        title=Label(frame1,text="REGISTER HERE",font=("times new roman",20,"bold"),bg="white",fg="green").place(x=50,y=30)
        #============row1===================
        
        f_name=Label(frame1,text="First Name",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=100)
        self.txt_fname=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_fname.place(x=50,y=130,width=250)

        l_name=Label(frame1,text="Last Name",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=100)
        self.txt_lname=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_lname.place(x=370,y=130,width=250)


        #===============================row 2==================
        contact=Label(frame1,text="Contact No.",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=170)
        self.txt_contact=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_contact.place(x=50,y=200,width=250)

        email=Label(frame1,text="Email",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=170)
        self.txt_email=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_email.place(x=370,y=200,width=250)


        #===============================row 3==================
        password=Label(frame1,text="Password",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=240)
        self.txt_password=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_password.place(x=50,y=270,width=250)

        cpassword=Label(frame1,text="Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=240)
        self.txt_cpassword=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_cpassword.place(x=370,y=270,width=250)
        

        #=========Term===============
        self.var_chk=IntVar()
        chk=Checkbutton(frame1,text="I Agree The Terms & Conditions",variable=self.var_chk,onvalue=1,offvalue=0,bg="white",font=("time new roman",12)).place(x=50,y=310)

        self.btn_img=ImageTk.PhotoImage(file="image/regis.jpg")
        btn_register=Button(frame1,image=self.btn_img,bd=0,cursor="hand2",command=self.register_data).place(x=50,y=350)

        btn_login=Button(self.root,text="Sign In",command=self.login_window,font=("times new roman",20),bd=0,cursor="hand2").place(x=880,y=480,width=180)
    
    def login_window(self):
        self.root.destroy()
        import login
        os.system("python login.py")







    def clear(self):
        self.txt_fname.delete(0,END)
        self.txt_lname.delete(0,END)
        self.txt_contact.delete(0,END)
        self.txt_email.delete(0,END)
        self.txt_password.delete(0,END)
        

    def register_data(self):
        if self.txt_fname.get()=="" or self.txt_contact.get()=="" or self.txt_email.get()=="" or self.txt_password.get()=="" or self.txt_cpassword.get()=="":
            messagebox.showerror("Error","All Fields Are ReQuired",parent=self.root)
        elif self.txt_password.get()!=self.txt_cpassword.get():
            messagebox.showerror("Error","Password & Confirm Password should be same",parent=self.root)
        elif self.var_chk.get()==0:
            messagebox.showerror("Error","Please Agree our terms & conditions",parent=self.root)
        else:
            try:
                con=sqlite3.connect(database="rns.db")
                cur=con.cursor()
                cur.execute("select * from resultt where email=?",(self.txt_email.get(),))
                row=cur.fetchone()
                
                #print(row)
                if row!=None:
                    messagebox.showerror("Error","User Already Exist,Please try with another email",parent=self.root)
                else:
                    cur.execute("insert into resultt (f_name,l_name,contact,email,password) values(?,?,?,?,?)",
                               (self.txt_fname.get(),
                                self.txt_lname.get(),
                                self.txt_contact.get(),
                                self.txt_email.get(),
                                self.txt_password.get()
                                ))
                con.commit()
                con.close()
                messagebox.showinfo("Success","Registered Successfully",parent=self.root)
                self.clear()
                self.login_window()
            except Exception as es: 
                messagebox.showerror("Error",f"Error due to:{str(es)}",parent=self.root)   
            


















root=Tk()
obj=Register(root)
root.mainloop()