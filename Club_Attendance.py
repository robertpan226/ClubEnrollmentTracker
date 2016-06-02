from Tkinter import *
import Add_Member
import Kick_Member
import Write_Attendance
import tkMessageBox
class CAS:

    def Club_Attendance(self,currentClub):
        headings = ["Name", "Student #", "Attend. Rate"]
        self.avlist=[] #attendace checker variable list
        self.attended=[]

        club_data=self.Read_Club(currentClub)
        ams=Add_Member.add_member()
        km=Kick_Member.kick_member()
        wa=Write_Attendance.Write_Attendance()
        self.master = Tk()
        self.master.lift()
        self.master.title(club_data[0])

        canvas = Canvas(self.master, width=480, height=50000, scrollregion=(0,0,50000,50000))
        frame = Frame(canvas)
        vbar=Scrollbar(self.master,orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand = vbar.set)

        vbar.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)
        canvas.create_window((4,4), window=frame, anchor="nw", tags="frame")


        Label(frame, text = "President: " + club_data[1] + " (" + club_data[2] + ")").grid(row = 0, column = 0, sticky = W)
        Label(frame, text = "Staff Advisor: " + club_data[3]).grid(row = 1, column = 0, sticky = W)
        Label(frame, text = "Avg Attend. Rate: " + str(club_data[4])+ "%").grid(row = 2, column = 0, sticky = W)
        Label(frame, text = "Members:").grid(row = 3, column = 0, sticky = W)

        for hc1 in range(0, len(headings)):
            Label(frame, text = headings[hc1], width = 10).grid(row = 4, column = hc1)

        r1 = 5

        if club_data[5] != []:
            for c1 in range(0, len(club_data[5])):
                student = club_data[5][c1].split(",")
                Label(frame, text = student[1] + " "+student[2], width = 15).grid(row = r1, column = 0)     #name
                Label(frame, text = student[0], width = 15).grid(row = r1, column = 1)                  #student number
                Label(frame, text = student[3], width = 15).grid(row = r1, column = 2)



                self.avlist.append(student[0])
                Checkbutton(frame, text="Attended",onvalue=1,offvalue=0,
                command=lambda c1=c1:make_attendance(c1,self.avlist)).grid(row = r1, column = 3)
                r1 += 1
        def refresh(CurrentClub):
            self.master.destroy()
            self.Club_Attendance(CurrentClub)
#-------------------------------------------------------------------------------
        def make_attendance(indexno,studentcode):
            if studentcode[indexno] in self.attended:
                self.attended.remove(studentcode[indexno])
            else:
                self.attended.append(studentcode[indexno])
            #print self.attended
#-------------------------------------------------------------------------------
            #self.attended have a person who has attended
            #write in both student and club file
#-------------------------------------------------------------------------------

        Button(frame, text = "Submit", width = 10, command = lambda:wa.write_attendance(currentClub,self.attended)).grid (row = 0, column = 3)
        Button(frame, text = "Add Member", width = 10, command = lambda:ams.AMScreen(currentClub)).grid (row = 1, column = 3)
        Button(frame, text = "Refresh List", width = 10, command = lambda:refresh(currentClub)).grid (row = 2, column = 3)
        Button(frame, text = "Kick Member", width = 10, command = lambda:km.deleteGUI(self.Read_Club(currentClub),currentClub,"334284452")).grid (row = 3, column = 3)
        mainloop()

    #-------------------------------------------------------------------------------
    def Read_Club(self,CurrentClub):
        tempfile=open("Data/clubs/"+CurrentClub+".txt","r")
        readtext = tempfile.readlines()
        tempfile.close()

        returnclubdata=[]
        personlist=[]
        memberlist=[]
        templist=[]
        totalmeeting=0
        totalattend=0
        #-------------------------------------------------------------------------------
        for iLine in range(len(readtext)):
                if "\n" in readtext[iLine]:
                    readtext[iLine] = readtext[iLine][:-1]
        for i in range (0,len(readtext)):
            if i>0:
                personlist.append(readtext[i])


        for x in range(0,len(personlist)):
            totalmeeting+=int(personlist[x].split(",")[3].split("/")[1])*1.0
            totalattend+=int(personlist[x].split(",")[3].split("/")[0])*1.0
        totalavg=round(totalattend/totalmeeting,2)*100



      #calculate total attence -------------------------------------------------------
        staffadvisor=readtext[0]
        leaderdata=personlist[0].split(",")
        leaderid=leaderdata[0]
        leadername=leaderdata[1]+" "+leaderdata[2]
        returnclubdata.append(CurrentClub)
        returnclubdata.append(leadername)
        returnclubdata.append(leaderid)
        returnclubdata.append(staffadvisor)
        returnclubdata.append(totalavg)
        returnclubdata.append(personlist)
        return returnclubdata


































