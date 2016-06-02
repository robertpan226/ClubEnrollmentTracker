from Tkinter import *
import tkMessageBox
import Function_Module
#-------------------------------------------------------------------------------
Functions=Function_Module.functions()

class clubl():
    def main(self,currentID):
        self.cl=Tk()
        self.cl.lift()
        self.cl.title("Select Your Option")

        canvas = Canvas(self.cl, width=100, height=250, scrollregion=(0,0,100,5000))
        frame = Frame(canvas)
        vbar=Scrollbar(self.cl,orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand = vbar.set)

        vbar.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)
        canvas.create_window((4,4), window=frame, anchor="nw", tags="frame")


        sclublist = open("Data/idpw/"+currentID+".txt","r")
        slines = sclublist.read().replace('\n','-#').split('-#')
        itotalmembers = (len(slines))-1

        self.CreateClubButton=Button(frame,text="Create Club",fg="black",width=12,height=5,padx=5,pady=5,command = lambda:self.createClub(currentID)).pack()


        for i in range(0, itotalmembers):
            Button(frame,text=slines[i+1],fg="black",width=12,height=5,padx=5,pady=5,command = lambda i=i:Functions.Attend_Sheet(slines[i+1])).pack()


            #^coonnect button with club view page  need a way to find out which button is clicked

        self.cl.mainloop()
#-------------------------------------------------------------------------------


    def createClub(self,currentID):
        self.cc = Tk()
        self.cc.title("Create New Club")

        Label(self.cc, text="Club Name").grid(row=0)
        Label(self.cc, text="Club Leader(First & Last)").grid(row=1)
        Label(self.cc, text="Club Leader Student ID").grid(row=2)
        Label(self.cc, text="Staff Advisor").grid(row=3)
        Label(self.cc, text="Grade").grid(row=4)
        self.clubname = Entry(self.cc)
        self.clubleader = Entry(self.cc)
        self.clubleaderID=Entry(self.cc)
        self.clubstaff = Entry(self.cc)
        self.leadergrade=Entry(self.cc)

        self.clubname.grid(row=0, column=1)
        self.clubleader.grid(row=1, column=1)
        self.clubleaderID.grid(row=2, column=1)
        self.clubstaff.grid(row=3, column=1)
        self.leadergrade.grid(row=4,column=1)
        createButton=Button(self.cc, text = "Create", width = 10, command = lambda:writeclub(currentID,self.clubname,self.clubleader,self.clubleaderID,self.clubstaff))

        createButton.grid(row = 5, column = 1)
#-------------------------------------------------------------------------------

        def writeclub(currentID,name,leader,leaderid,staff):
            write=False
            self.sclubname=name.get()
            self.sclubleader=leader.get()
            self.sclubleaderID=leaderid.get()
            self.sclubstaff=staff.get()
            try:
                tempifileclub = open("Data/clubs/"+self.sclubname+".txt","r")
                tkMessageBox.showinfo("Error!","Same Name Club Exists")
                self.clubname.delete(0, END)
                self.clubleader.delete(0, END)
                self.clubleaderID.delete(0, END)
                self.clubstaff.delete(0, END)




            except IOError:
                tempifileclub = open("Data/clubs/"+self.sclubname+".txt","w")
                tempfileid = open("Data/idpw/"+currentID+".txt","a")  # load in appened so that the program does not rewrite


                tempfileid.write("\n") #new line
                tempfileid.write(self.sclubname) #add club



                tempifileclub.write(self.sclubstaff)
                tempifileclub.write("\n")
                tempname=self.sclubleader.split(" ")
                tempifileclub.write(self.sclubleaderID+","+tempname[0]+","+tempname[1]+","+"1/1")
                tempifileclub.close()
                tempfileid.close()




                try:
                    tempstudenttext=open("Data/students/"+self.clubleaderID.get()+".txt","r")
                    write=True

                except IOError:
                    print "hi"
                    tempstudenttext=open("Data/students/"+self.clubleaderID.get()+".txt","w")
                    tempstudenttext.write(self.clubleader.get().split(" ")[0]+","+self.clubleader.get().split(" ")[1]+","+self.leadergrade.get()+"\n")
                    tempstudenttext.write(self.clubname.get()+",1/1")
                    print "hi"

                if write==True:
                    tempstudenttext=open("Data/students/"+self.clubleaderID.get()+".txt","a")
                    tempstudenttext.write("\n"+self.clubname.get()+",1/1")



                tempstudenttext.close()
                self.cc.destroy()
                self.cl.destroy()
                self.main(currentID)
#refrsh after club is made    persons id gets deleted

        mainloop()




















