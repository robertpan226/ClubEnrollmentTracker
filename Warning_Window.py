from Tkinter import *
import Data_Reader

class Red_Screen(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)
        self.canvas = Canvas(root, borderwidth=0,width=650, height=3000000, scrollregion=(0,0,3000000,3000000))
        self.frame = Frame(self.canvas, )
        self.vsb = Scrollbar(root, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.vsb.set)

        self.vsb.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas.create_window((4,4), window=self.frame, anchor="nw",
                                  tags="self.frame")



        self.generate()




    def generate(self):
        data = Data_Reader.read_red()
        data.insert(0,["Number","F.Name","L.Name","Grade","Attendance %"])
        for i in range (len(data)):
            for i2 in range(5):
                label=Label(self.frame,text=data[i][i2],width=10).grid(row=i,column=i2)
