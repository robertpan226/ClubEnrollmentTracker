from Tkinter import *
import tkMessageBox
class add_member:
    def AMScreen(self,currentClub):
        self.AMmaster = Tk()
        self.AMmaster.title("Add Member")
        self.AMmaster.lift ()
        Label(self.AMmaster, text="First & Last Name:").grid(row=0)
        Label(self.AMmaster, text="Student Number:").grid(row=1)
        Label(self.AMmaster,text="Grade:").grid(row=2)
        self.sname = Entry(self.AMmaster)
        self.snumber = Entry(self.AMmaster)
        self.sgrade= Entry(self.AMmaster)

        self.sname.grid(row=0, column=1)
        self.snumber.grid(row=1, column=1)
        self.sgrade.grid(row=2, column=1)
        Button(self.AMmaster, text = "Add", width = 10, command = lambda:calltwofunctions(self.sname,self.snumber,self.sgrade,currentClub)).grid(row = 4, column = 0)
        Button(self.AMmaster, text = "Done", width = 10, command = lambda:quitandmessage()).grid(row = 4, column = 1)



        def calltwofunctions(sname,snumber,sgrade,currentClub):
            self.write_member(sname,snumber,sgrade,currentClub)
            self.sname.delete(0, END)
            self.snumber.delete(0, END)
            self.sgrade.delete(0, END)
        def quitandmessage():
            self.AMmaster.destroy()
            tkMessageBox.showinfo("Friendly Message!","Click Refresh List Button to Refresh Members ")

        mainloop()

    def write_member(self,studentname,studentcode,studentgrade,clubname):
        write=False
        studentgrade=studentgrade.get()
        studentname=studentname.get().split(" ")[0]+","+studentname.get().split(" ")[1]
        studentcode=studentcode.get()

        tempclubidcheck=open("Data/clubs/"+clubname+".txt","r")
        tempclubidcheck2=tempclubidcheck.readlines()
        tempclubidcheck.close()
        joinedid=[]
        alreadyjoined=False
        for i in range(0,len(tempclubidcheck2)):
            if i>0:
                joinedid.append(tempclubidcheck2[i].split(",")[0])

        for k in range (0,len(joinedid)):
            if joinedid[k]==studentcode:
                tkMessageBox.showinfo("Error!","You Have Already Joined the Club "+clubname)
                alreadyjoined=True
        if alreadyjoined==False:
            tempclubtext=open("Data/clubs/"+clubname+".txt","a")



            try:
                tempstudenttext=open("Data/students/"+studentcode+".txt","r")
                write=True

            except IOError:
                tempstudenttext=open("Data/students/"+studentcode+".txt","w")
                tempstudenttext.write(studentname+","+studentgrade+"\n")
                tempstudenttext.write(clubname+",1/1")




            tempclubtext.write("\n"+studentcode+","+studentname+",1/1")
            if write==True:
                tempstudenttext=open("Data/students/"+studentcode+".txt","a")
                tempstudenttext.write("\n"+clubname+",1/1")



            tkMessageBox.showinfo("Congrats!","Member Added! "+clubname)
            tempclubtext.close()
            tempstudenttext.close()


#AMScreen("C++")






























