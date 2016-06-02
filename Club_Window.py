from Tkinter import *
class Club_Screen:
    def club_screen(self,currentClub):
        headings = ["Name", "Student #", "Attend. Rate"]
        club_data=self.Read_Club(currentClub)
        self.master = Tk()
        self.master.lift()
        self.master.title(club_data[0])

        canvas = Canvas(self.master, width=480, height=500, scrollregion=(0,0,500,500))
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
                r1 += 1
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

