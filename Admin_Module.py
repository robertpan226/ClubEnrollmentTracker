from Tkinter import *
import tkMessageBox
import Function_Module
#-------------------------------------------------------------------------------
Functions=Function_Module.functions()

class admin():
    def main(self):



        self.root=Tk()
        self.root.title("ADMIN")

        WarningListButton=Button(self.root ,text="Warning List",fg="red",width=12,height=5,padx=5,pady=5,command = lambda:Functions.WarningListScreen())
        ViewClubButton=Button(self.root ,text="View By Club",fg="black",width=12,height=5,padx=5,pady=5,command = lambda:Functions.ViewClubScreen())
        SearchButton=Button(self.root ,text="Search",fg="black",width=12,height=5,padx=5,pady=5,command = lambda:Functions.SearchScreen())
        CreditButton=Button(self.root ,text="Credit Support",fg="blue",width=12,height=5,padx=5,pady=5,command = lambda:self.creditscreen())

        WarningListButton.grid(row=0,column=0)
        SearchButton.grid(row=0,column=1)
        CreditButton.grid(row=1,column=1)
        ViewClubButton.grid(row=1,column=0)


        self.root.mainloop()

        print "ADMIN"
    def creditscreen(self):
        tkMessageBox.showinfo("For Technical Support","Please Contact Python Group")

































