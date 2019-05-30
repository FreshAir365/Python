###Author: Abdikarim Ibrahim
###Date: 12/06/17
###Description: read the file HW12-WriteStart and write a new file if one doesn't
###exist
print("Abdikarim Ibrahim, Hw#12-Write")
import random
random.seed()
def Name():
    N = chr(random.randint(65,90))
    for i in range(random.randint(2,3)):
        N += chr(random.randint(97,122))
    N += N[len(N)-1]
    return N
Rows = []
print("The data created for your program is:")
for i in range(random.randint(6,8)):
    Col = [Name()]
    for j in range(random.randint(3,5)):
        Col.append(random.randint(60,100)/10)
    Col.append(Col[len(Col)-1])
    Rows.append(Col)
    print(Col)
print("Number of Rows is",len(Rows),"\n\n*** Your Output is below ***")

# **** Put your code below this line.  Do not change anything above this line. ****

default_file="writefile.txt"#what file name to use
flag=0
myFile = default_file
while flag==0:
    try:
        #with open('writefile.txt','r') as f:
            #myFile=f.read()
        f=open(myFile,'r')
    except:
        #with open('writefile.txt','w') as f:
            #myFile=f.write()
        f=open(myFile,'w')
        print("file not found but creates new file")
        flag=1
    else:
        ans=input("Do you want to overwrite/erase:" + myFile +" " )
        if ans=='y' or ans=='Y':
            f.close()
            flag=1
            #with open('writefile.txt','w') as f:
                #myFile=f.write()
            f=open(myFile,'w')#create,or erase/overwrite
            print(myFile,"file opened")
        else:
            prompt=input("What file name you want to use")
            myFile = prompt
for j in Rows:
    print(j[0], end="")
    f.write(str(j[0]))
    for i in range (1,len(j)):
        print(", " + str(j[i]),end="")
        f.write(", ")
        f.write(str(j[i]))
    f.write('\n')
    print()
f.close()
    ##f.writelines('j')
            
