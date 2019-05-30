##Author: Abdikarim Ibrahim
##Date: 11/29/17
##Description: the program read an existing file

def Average_Score(total):
    Sum=0
    for i in range (1,len(total)):
        Sum+=float(total[i])
    Average=(Sum/(len(total)-1))
    return round(Average,2)
    
default_file='writefile.txt'
flag=0
myFile = default_file
while flag==0:
    try:
        f=open(myFile,'r')
    except:
        print("file not found ")
        prompt=input("press one to abort or zero to create new file ")
        if prompt==1:
            flag=1
        else:
            userInput=input("What file name you want to use? ")
            myFile = userInput
    else:
        flag=1
        line=f.readline()
        print
        count=0
        Sum_Avg=0
        while line!= "":
            splitLine=line.split(",")
            print(line[0:-1],"avg=",Average_Score(splitLine))
            line=f.readline()
            count+=1
            Sum_Avg+=Average_Score(splitLine)
            #print(round(Sum_Avg,2))
        Avg_AvgScore=Sum_Avg/count
        print()
        print("Students processed = ",count,\
              "Average Student Grade = ",round(Avg_AvgScore,2))
