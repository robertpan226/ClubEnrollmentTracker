import Login_Module
import Admin_Module
import ClubL_Module
#-------------------------------------------------------------------------------
LoginScreen=Login_Module.login()
AdminScreen=Admin_Module.admin()
ClubLScreen=ClubL_Module.clubl()
#-------------------------------------------------------------------------------
def load_login():
    Login=LoginScreen.login_screen()
    if Login[0]!="":

        if Login[0]=="admin":
            if (Login[1]==True):
                AdminScreen.main()
        else:
            if (Login[1]==True):
                ClubLScreen.main(Login[0])
#-------------------------------------------------------------------------------
selectscreen=LoginScreen.login_selection()
if selectscreen=="loginb":
    load_login()
if selectscreen=="signupb":
    Login=LoginScreen.sign_up()
    if Login==True:
        load_login()
#-------------------------------------------------------------------------------
#Todo---------------------------------------------------------------------------
#more Message Box
#fix top level issue
#image
#make it as a exe file
#icon
#
#
#
#


#Special thx to ahskan janet luyi Jackie







