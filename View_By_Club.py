from Tkinter import *
from Data_Reader import *
import Club_Window
class comp_button():

    def __init__(self,name,master,row):
        self.name = name
        self.master = master
        self.row = row
    def make_button(self):
        self.info = Button(self.master,text=self.name,command=self.new_window)
        self.info.grid(row=self.row+1,column=0)
    def new_window(self):
        cw=Club_Window.Club_Screen()
        cw.club_screen(self.name)

class VBC(Frame):
    DATA = get_clubs()
    def __init__(self, root):

        Frame.__init__(self, root)
        self.canvas = Canvas(root, borderwidth=0,width=650, height=300)
        self.frame = Frame(self.canvas, )
        self.vsb = Scrollbar(root, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.vsb.set)

        self.vsb.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas.create_window((4,4), window=self.frame, anchor="nw",
                                  tags="self.frame")

        self.frame.bind("<Configure>", self.OnFrameConfigure)

        self.populate()
    def populate(self):
        headings = ["Name","Staff Advisor", "President","Attendance Rate (%)","# Of Meets"]
        data = VBC.DATA
        l = len(data)
        for i in range(5):
            temp_label = Label(self.frame,text=headings[i],width=15)
            temp_label.grid(row =0,column=i)

        for i in range(l):
            temp_button = comp_button(data[i][0],self.frame,i)
            temp_button.make_button()
            for i2 in range(4):
                temp_label = Label(self.frame,text=data[i][i2+1],width=15)
                temp_label.grid(row =i+1, column=i2+1)


    def OnFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))


