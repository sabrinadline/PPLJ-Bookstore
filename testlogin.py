from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk

import mysql.connector

class login_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login Page")
        self.root.geometry("1550x800+0+0")

        #self.bg = PhotoImage(file="background-login-page.jpg")

        #lbl_bg = Label(self.root,image=self.bg)
        #lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame = Frame(self.root, bg="#D1D1D1")
        frame.place(x=610,y=170,width=340,height=450)

        get_str=Label(frame,text="Welcome, Admin", font=("Calibri",20,"bold"),fg="black",bg="#D1D1D1")
        get_str.place(x=60,y=60)

        #label
        label_username=lbl=Label(frame,text="Username:", font=("Calibri",15),fg="black",bg="#D1D1D1")
        label_username.place(x=40,y=140)

        self.txtuser=ttk.Entry(frame,font=("Calibri",13))
        self.txtuser.place(x=40,y=170,width=260)

        label_password=lbl=Label(frame,text="Password:", font=("Calibri",15),fg="black",bg="#D1D1D1")
        label_password.place(x=40,y=200)

        self.txtpass=ttk.Entry(frame,font=("Calibri",13), show = '*')
        self.txtpass.place(x=40,y=230,width=260)

        #login button
        loginbtn=Button(frame,command=self.login,text="Login", font=("Calibri",15),bd=3,relief=RAISED,fg="white",bg="#008A31")
        loginbtn.place(x=110,y=350,width=120,height=35)
    
    def login(self):

        IDAdmin = self.txtuser.get()
        Password_Admin = self.txtpass.get()

        if IDAdmin=="" or Password_Admin=="":
            messagebox.showerror("Error","all field required")
        elif IDAdmin=="sabrina" and Password_Admin=="Admin123":
            messagebox.showinfo("Success","Welcome to Admin Page")
            #self.new_window=Toplevel(self.root)
            #self.app=adminpage_window(self.new_window)
        else:
            messagebox.showerror("Invalid","Invalid username or password")
            """conn=mysql.connector.connect(host="localhost",user="root",password="Admin123_",database="databaseadm")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from data admin where nama_admin=%s and password_admin=%s",(
                                                                                            self.txtuser.get(),
                                                                                            self.txtpass.get()
                                                                                            ))
            
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username or Password")
            else:
                self.new_window=Toplevel(self.new_window)
                self.app=adminpage_window(self.new_window)
            
            conn.commit()
            conn.close()"""

if __name__ == "__main__":
    root=Tk()
    app = login_window(root)
    root.mainloop()