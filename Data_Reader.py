#Gets info for all clubs :)
#-------------------------------------------------------------------------------
from glob import *
def get_clubs():
    data = []
    datae=[]
    data = glob("Data/clubs/*.txt")
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
def read_red():
    data = []
    datae=[]
    data = glob("Data/students/*.txt")
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
        a.append(data[i].replace("Data/students\\","").replace(".txt",""))
        a.append(info[0])
        a.append(info[1])
        a.append(info[2])
        num = ((len(info))-3)/2
        for i in range(num):
            c=info[(i*2)+4]
            c=c.split("/")
            t+=int(c[0])
            b+=int(c[1])
        perc = (round((t/b)*100))
        a.append(perc)
        if perc <= 70:
            datae.append(a)
        else:
            None
        infile.close()
    return datae



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
    print data,"datatest"
    return data

