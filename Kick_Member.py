import re
import fileinput
from Tkinter import *
class kick_member:
    def importclubfile(self,CurrentClub):
        tfile1=open("Data/clubs/"+CurrentClub+".txt","r")
        lfile=tfile1.read().replace('\n',',').split(',')
        tfile1.close()
        return lfile
#-------------------------------------------------------------------------------
    def delete_member(self,sstudentnum,lclub,CurrentClub):
        f = open("Data/clubs/"+CurrentClub+".txt",'w')
        f.write(lclub[0])
        for i in range (len(lclub)/4):
            if lclub[4*i+1] != sstudentnum:
                f.write('\n'+','.join(lclub[i*4+1:i*4+5]))
        f.close()
#-------------------------------------------------------------------------------
    def deletefromstudent(self,studentcode,CurrentClub):
        f = open("Data/students/"+studentcode+".txt",'r')
        f2=f.readlines()
        for i in range (1,len(f2)):
            print f2[i].split(",")[0]
            if f2[i].split(",")[0]==CurrentClub:
                f2.remove(f2[i])
        f.close()
        f = open("Data/students/"+studentcode+".txt",'w')
        for i in range(0,len(f2)):
            f.write(f2[i])
        f.close()
#-------------------------------------------------------------------------------
    def runkick (self,CurrentClub,StudentID):
        lclub= self.importclubfile(CurrentClub)
        self.delete_member(StudentID,lclub,CurrentClub)
        self.deletefromstudent(StudentID,CurrentClub)
        print "ran"
#-------------------------------------------------------------------------------
    def deleteGUI(self,clubdata,CurrentClub,StudentID):
        headings = ["Name", "Student #", "Rate", "Kick?"]
        club_data=clubdata
        self.deletevar=[]
        self.studentlist=[]
        self.deletescreen = Tk()
        self.deletescreen.lift()
        self.deletescreen.title(club_data[0])
        canvas = Canvas(self.deletescreen, width=480, height=50000, scrollregion=(0,0,50000,50000))
        frame = Frame(canvas)
        vbar=Scrollbar(self.deletescreen,orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand = vbar.set)
        vbar.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)
        canvas.create_window((4,4), window=frame, anchor="nw", tags="frame")
        Label(frame, text = "Members:").grid(row = 3, column = 0, sticky = W)
        for hc1 in range(0, len(headings)):
            Label(frame, text = headings[hc1], width = 10).grid(row = 4, column = hc1)
        r1 = 5
        if club_data[5] != []:
            for c1 in range(0, len(club_data[5])):
                if c1 != 0:
                    student = club_data[5][c1].split(",")
                    self.studentlist.append(student[0])
                    Label(frame, text = student[1] + " "+student[2], width = 15).grid(row = r1, column = 0)     #name
                    Label(frame, text = student[0], width = 15).grid(row = r1, column = 1)                  #student number
                    Label(frame, text = student[3], width = 15).grid(row = r1, column = 2)
                    Checkbutton(frame,onvalue=1,offvalue=0,command=lambda c1=c1:makedeletelist(c1,self.studentlist)).grid(row = r1, column = 3)
                r1 += 1
        Button(frame, text = "Submit", width = 10,command=lambda:InitDelete()).grid(row=0,column=3)

        def makedeletelist(indexno,studentcode):
            if studentcode[indexno-1] in self.deletevar:
                self.deletevar.remove(studentcode[indexno-1])
            else:
                self.deletevar.append(studentcode[indexno-1])
            print self.deletevar


        def InitDelete():
            print "init delete"
            for i in range(0,len(self.deletevar)):
                self.runkick(CurrentClub,self.deletevar[i])











#self.deletevar is the one who should be kicked out





















#Message jackie on how to remove empty space at the end and sutdent delete file
#delete from both student & Club remove empty space after deleting
#when check box is chekced and submit buutton is pressed load function delete_member and refresh
#the window














