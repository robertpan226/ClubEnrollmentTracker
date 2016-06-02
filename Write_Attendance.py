import fileinput
import tkMessageBox
from glob import *
class Write_Attendance:
    def write_attendance(self,CurrentClub,attendeddata):
        currentClub=CurrentClub
        attended=attendeddata
        templist=[]
        writetextlist=[]
        studentdata=[]
        #intialize
        lclubfile=open("Data/clubs/"+currentClub+".txt","r")
        lclubfile2=lclubfile.readlines()
        lclubfile.close()
        #open and read from text file
        for i in range(0,len(attended)):
            for x in range(0,len(lclubfile2)):
                if attended[i]== lclubfile2[x].split(",")[0]:
                    templist.append(lclubfile2[x])
        #making templist
        for i in range(0,len(templist)):
            tempstring=templist[i].split(",")
            attendancerate=tempstring[3].split("/")
            if i==(len(templist)-1):
                tempstring2=tempstring[0]+","+tempstring[1]+","+tempstring[2]+","+str((int(attendancerate[0])+1))+"/"+str(int(attendancerate[1])+1)+"\n"
            else:
                tempstring2=tempstring[0]+","+tempstring[1]+","+tempstring[2]+","+str((int(attendancerate[0])+1))+"/"+str(int(attendancerate[1])+1)+"\n"
            writetextlist.append(tempstring2)
        #+1 to attendance rate
        for i in range(1,len(lclubfile2)):
            tempstring=lclubfile2[i].split(",")
            attendancerate=tempstring[3].split("/")
            if i==(len(lclubfile2)-1):
                tempstring2=tempstring[0]+","+tempstring[1]+","+tempstring[2]+","+str((int(attendancerate[0])))+"/"+str(int(attendancerate[1])+1)+"\n"
            else:
                tempstring2=tempstring[0]+","+tempstring[1]+","+tempstring[2]+","+str((int(attendancerate[0])))+"/"+str(int(attendancerate[1])+1)+"\n"
            lclubfile2[i]=tempstring2
        #+1 to total attendance rate
        for i in range (0,len(writetextlist)):
            for x in range(0,len(lclubfile2)):
                if writetextlist[i].split(",")[0]==lclubfile2[x].split(",")[0]:
                    lclubfile2[x]=writetextlist[i]
        lclubfile2[len(lclubfile2)-1]=lclubfile2[len(lclubfile2)-1].split("\n")[0]
        #changing clubfile2 value to new attendance rate  lastline get rid of space
        lclubfile=open("Data/clubs/"+currentClub+".txt","w")
        for i in range(0,len(lclubfile2)):
            lclubfile.write(lclubfile2[i])
        lclubfile.close()
        #writing new value to the club text file
#Club Write---------------------------------------------------------------------
        studentdata = glob("Data/students/*.txt")
        for i in range(0,len(studentdata)):
            temp=open(studentdata[i],"r")
            temp2=temp.readlines()
            for x in range(0,len(temp2)):
                if temp2[x].split(",")[0]==currentClub:
                    temp2[x]=temp2[x].split(",")[0]+","+str(int(temp2[x].split(",")[1].split("/")[0]))+"/"+str(int(temp2[x].split(",")[1].split("/")[1])+1)
            temp=open(studentdata[i],"w")
            for y in range(0,len(temp2)):
                temp.write(temp2[y])

            temp.close()

#add 1 to all text file total attendance

        for i in range(0,len(writetextlist)):
            studentfile=open("Data/students/"+writetextlist[i].split(",")[0]+".txt","r")
            studentfile2=studentfile.readlines()
            for x in range(0,len(studentfile2)):
                if studentfile2[x].split(",")[0]==currentClub:
                    studentfile2[x]=studentfile2[x].split(",")[0]+","+str(int(studentfile2[x].split(",")[1].split("/")[0])+1)+"/"+str(int(studentfile2[x].split(",")[1].split("/")[1]))
            studentfile=open("Data/students/"+writetextlist[i].split(",")[0]+".txt","w")
            for y in range(0,len(studentfile2)):
                studentfile.write(studentfile2[y])
            studentfile.close()
        tkMessageBox.showinfo("Attendance","Attendance Submitted")




#before process = templist
#replace text = writetextlise
#total list  = lclubfile2



















