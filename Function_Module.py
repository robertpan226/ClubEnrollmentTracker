from Tkinter import *
import tkMessageBox
import View_By_Club
import Data_Reader
import Club_Attendance
import Student_Window
import Club_Window
import Warning_Window
#-------------------------------------------------------------------------------
class functions():
    def WarningListScreen(self):
        self.rootwl=Toplevel()
        self.rootwl.title("View Bad Attendance")
        Warning_Window.Red_Screen(self.rootwl).pack(side="top", fill="both", expand=True)
        self.rootwl.mainloop()
#-------------------------------------------------------------------------------
    def ViewClubScreen(self):
        self.rootvc=Toplevel()
        self.rootvc.title("View Club")
        View_By_Club.VBC(self.rootvc).pack(side="top", fill="both", expand=True)
        self.rootvc.mainloop()
#-------------------------------------------------------------------------------
    def student_window(self,data):
        root = Toplevel()
#-------------------------------------------------------------------------------
    def grabs(self):
        studentname = self.ssearchbox.get()
        try:
            Student_Window.run(studentname)

        except IOError:
            print "Student Error "
    def grabc(self):
        clubname = self.csearchbox.get()
        try:
            temp=Club_Window.Club_Screen()
            temp.club_screen(clubname)

        except IOError:
            print "Club Error"
#-------------------------------------------------------------------------------
    def SearchScreen (self):
        self.roots=Toplevel()
        self.roots.title("Search")
        self.ssb=Button(self.roots ,text=" Search",fg="black",width=4,height=1,command = self.grabs)
        self.scb=Button(self.roots ,text=" Search",fg="black",width=4,height=1,command = self.grabc)
        self.ssearchbox=Entry(self.roots)
        self.csearchbox=Entry(self.roots)
        Label(self.roots , text='Search Student Code:').grid(row=0,column=0)
        Label(self.roots , text='Search Club Name:').grid(row=1,column=0)
        self.csearchbox.grid(row=1,column=1)
        self.ssearchbox.grid(row=0,column=1)
        self.ssb.grid(row=0,column=2)
        self.scb.grid(row=1,column=2)
        self.roots.mainloop()
#-------------------------------------------------------------------------------
    def Attend_Sheet(self,currentClub):
        attendsheet=Club_Attendance.CAS()
        attendsheet.Club_Attendance(currentClub)
#-------------------------------------------------------------------------------





