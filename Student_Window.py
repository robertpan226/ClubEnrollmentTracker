from Tkinter import *
import Data_Reader
#DATA=["335202818","Ashkan","Zirakzadeh","12",[["Python","10/30"],["C++","20/23"]]]

class Student_Screen(object):
    def generate(self,x):
        data = Data_Reader.read_student(x)
        self.root = Tk()
        self.root.title("Student View Window")
        temp_label = Label(self.root,text=(data[1]+" "+data[2]+"    "+ data[0]))
        temp_label.pack()
        temp_label = Label(self.root,text=("Grade: "+data[3]))
        temp_label.pack()
        temp_label = Label(self.root,text=("Clubs: "+str(len(data[4]))))
        temp_label.pack()
        var1 = IntVar()
        num=0
        dec=0
        for i in range(len(data[4])):
            perc=data[4][i][1].split("/")
            num+=float(perc[0])
            dec+=float(perc[1])
            perc=round((float(perc[0])/float(perc[1]))*100,2)

            temp_label = Label(self.root,text=(str(data[4][i][0]+ " " + str(perc))+"%"))
            temp_label.pack()
        temp_label = Label(self.root,text=("Average Attendance: " + str(round((num/dec)*100.0,2))+"%"))
        temp_label.pack()

def run(x):
    #root = Tk()
    a = Student_Screen()
    a.generate(x)
#print var1