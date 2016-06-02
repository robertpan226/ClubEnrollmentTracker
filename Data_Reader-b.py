#Gets info for all clubs :)
#-------------------------------------------------------------------------------
from glob import *
def get_clubs():
    data = []
    datae=[]
    data = glob("Data/clubs/*.txt")
    ##print data

    for i in range (len(data)):
        a=[]
        t=0.0
        b=0.0
        c=""
        path = data[i].replace('\\',"/")
        infile = open(path,'r')
        info = infile.read().replace(" ","")
        info = info.replace('\n',',').split(",")
        a.append(data[i].replace("Data/clubs\\","").replace(".txt",""))
        a.append(info[0])
        a.append(info[2]+" "+info[3])
        num = (len(info)-1)/4
        for i in range(num):
            c=info[(i*4)+4]
            c=c.split("/")
            t+=int(c[0])
            b+=int(c[1])
        a.append((round((t/b)*100.0,2)))
        a.append((info[4].split("/"))[1])


        datae.append(a)
        infile.close()
    #print datae
    return datae
#-------------------------------------------------------------------------------
def read_student(sFile):
    data = []
    temp = []
    # Opens the file sFile and stores the lines
    infile = open("Data/students/"+sFile+".txt","r")
    info = infile.read().replace(" ","")
    info = info.replace('\n',',').split(",")
    num = ((len(info))-3)/2
    data.append(sFile)
    data.append(info[0])
    data.append(info[1])
    data.append(info[2])
    print num
    for i in range(num):
        a= (i*2)+3
        b= (i*2)+4
        temp.append([info[a],info[b]])
    data.append(temp)
    print data
    return data


##    sText = fFile.readlines()
##    fFile.close()
##    # Removes \n from the end of each line
##    for iLine in range(len(sText)):
##        if "\n" in sText[iLine]:
##            sText[iLine] = sText[iLine][:-1]
##    # Reads first line for name, grade etc. and stores as variables
##    lInfo = sText[0].split(",")
##    sName = lInfo[1]+" "+lInfo[0]
##    sNumber = sFile[:-4]
##    lClubName=[]
##    lAttendance = []# list that stores lists with club name and attendance rate
##    for lLine in sText[1:]:# loop iterates through each club entry
##        lLine = lLine.split(",")
##        sClubName = lLine[0]
##        #Attendance
##        fAttrate = int((float(lLine[1])/float(lLine[2]))*100)# calculates the attendance rate
##        lAttendance.append(fAttrate)
##        lClubName.append(sClubName)
##    # Returns all values as a list
##    return sName, sNumber, lClubName, lAttendance
#DATA=["335202818","Ashkan","Zirakzadeh","12",[["Python","10/30"],["C++","20/23"]]]
#get_clubs()
#read_student("3342844456")