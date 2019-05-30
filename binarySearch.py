#Data for Binary Search HW
import random
random.seed()
#Build a list of random names in DataKeys.
DataKeys = []
for j in range(random.randint(80,120)):
    #Create one random name.
    Name = chr(random.randint(65,90))
    for i in range(1,random.randint(3,6)):
        Name = Name + chr(random.randint(97,122))
    #print(Name)
    DataKeys.append(Name)
NumDataKeys = len(DataKeys)
#Build a list of keys to find.
KeyList = []
for j in range(random.randint(4,8)):
    KeyList.append(DataKeys[j])
#Modify the list so one key is not in the DataKeys.
j = random.randint(0,len(KeyList)-1)
KeyList[j]=KeyList[j] + "1"
#Sort list
DataKeys.sort()  #Do not use this function for sort HW assignments.
print("The following list contains",NumDataKeys,"sorted names")
for j in range(NumDataKeys):
    print(DataKeys[j],end="\t")
    if j % 8 == 7:
        print()
print()

print("Keylist contains",len(KeyList),"keys")
def BinarySearch(List,Keyword):
    N=(len(List))
    Low=0
    High=N
    Index=int(N/2)
    Found=0
    while (Found==0) and Low<=High:
        if Keyword==List[Index]:
            Found=1
        elif Keyword>List[Index]:
            Low=Index+1
            Index=int((High+Low)/2)
        elif Keyword<List[Index]:
            High=Index-1
            Index=int((High+Low)/2)
    if Found==1:
        print(Keyword,"\t",Index,"\t",List[Index])
    else:
        print("The keyword",Keyword,"not found")
        
for i in KeyList:
    BinarySearch(DataKeys,i)
    
