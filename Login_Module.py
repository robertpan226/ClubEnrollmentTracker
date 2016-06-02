from Tkinter import *
import tkMessageBox
import sys
import linecache
import os
#-------------------------------------------------------------------------------
class login():

    def login_screen(self):
        self.root = Tk()
        self.root.title("LOGIN")
        self.img=PhotoImage(file='Data/images/logo.gif')
        Label(self.root,image=self.img).grid(row=0, column=0, columnspan=2)
        self.root.lift()
        self.tempid=("")
        self.returnvalue=[self.tempid,False]
        self.IDe=Entry(self.root )
        self.PWe=Entry(self.root ,show="*")

        loginbutton=Button(self.root ,text="Login",fg="black",width=4,height=1,command = lambda:self.attempt_login(None))
        self.root.bind('<Return>', self.attempt_login)

        Label(self.root , text='ID:').grid(row=1,column=0)
        Label(self.root , text='PW:').grid(row=2,column=0)
        self.IDe.grid(row=1,column=1,ipadx=3,ipady=3)
        self.PWe.grid(row=2,column=1,ipadx=3,ipady=3)
        loginbutton.grid(columnspan=3,ipadx=3,ipady=3)

        self.root .mainloop()

        self.returnvalue[0]=self.tempid


        return self.returnvalue
#-------------------------------------------------------------------------------
    def attempt_login(self,event):
        self.tempid = self.IDe.get()
        self.IDe.delete(0,END)

        self.temppw = self.PWe.get()
        self.PWe.delete(0,END)
        icounter=0
        try:
            infile = open("Data/idpw/"+self.tempid+".txt","r")
            pw = infile.readline().strip()
            infile.close()
            if pw==self.temppw:
                print "login successful!"
                self.root.destroy()
                self.returnvalue[1]=True

            else:
                tkMessageBox.showinfo("Error!","Incorrect Password")


        except IOError:
            tkMessageBox.showinfo("Error!", "No Such Account")

#-------------------------------------------------------------------------------
    def login_selection(self):
        self.selectionreturnvalue=""
        self.ls = Tk()
        self.ls.title("Clubs Program - Start Window")
        self.img=PhotoImage(file='Data/images/logo.gif')
        Label(self.ls,image=self.img).pack()
        Label(self.ls, text = "Clubs Managing Program", width = 20).pack()
        def loginb():
            self.selectionreturnvalue="loginb"
            self.ls.destroy()
        def signupb():
            self.selectionreturnvalue="signupb"
            self.ls.destroy()


        self.loginsb=Button(self.ls, text = "Log In", width = 15, command = lambda:loginb())
        self.singinsb=Button(self.ls, text = "Sign Up", width = 15, command = lambda:signupb())
        self.loginsb.pack()
        self.singinsb.pack()
        self.ls.mainloop()
        return self.selectionreturnvalue
#-------------------------------------------------------------------------------
    def sign_up(self):
        def create_account(tid,tpw1,tpw2):
            sid=tid.get()
            spw1=tpw1.get()
            spw2=tpw2.get()
            if (sid=="" or spw1=="" or spw2==""):
                tkMessageBox.showinfo("Missing Info", "Please fill up all the blanc")
            else:
                try:
                    idcheck=open("Data/idpw/"+sid+".txt","r")
                    tkMessageBox.showinfo("Error!"," Same ID exists")
                except IOError:
                    if spw1!=spw2:
                        tkMessageBox.showinfo("Password Does Not Match", "Please Type Your Password Again !")
                    else:
                        file = open("Data/idpw/"+sid+'.txt','w')
                        file.write(spw1)
                        file.close()
                        self.returnvalue2=True
                        tkMessageBox.showinfo("Congrats!","You Have Made Your Account")
                        self.su.destroy()


#-------------------------------------------------------------------------------
        self.su = Tk()
        self.su.title("Sign Up")
        self.returnvalue2=False

        self.lid=Label(self.su, text="Student ID").grid(row=0)
        self.lPW1=Label(self.su, text="Password").grid(row=1)
        self.lPW2=Label(self.su, text="Confirm Password").grid(row=2)

        self.eID = Entry(self.su)
        self.ePW1 = Entry(self.su,show="*")
        self.ePW2 = Entry(self.su,show="*")
        self.signupbutton=Button(self.su, text = "Sign Up", width = 10, command = lambda:create_account(self.eID,self.ePW1,self.ePW2))


        self.eID.grid(row=0, column=1)
        self.ePW1.grid(row=1, column=1)
        self.ePW2.grid(row=2, column=1)
        self.signupbutton.grid(row = 4, column = 1)

        self.su.mainloop()
        return self.returnvalue2
#-------------------------------------------------------------------------------




























