#Author: Abdikarim Ibrahim
#Date: 11/13/2017
#Description: This program sort the Data array using Bubble Sort tech
#Then print the sorted array out on one line.

Data = list("ZABSDEFWGHICJKLPMNO")
print(Data)
#Then print the sorted array out on one line.
def Alpha(Data):
    for i in range(0,len(Data)-1):
        for j in range(0,len(Data)-1):
            if Data[j]>Data[j+1]:
                Temp=Data[j]
                Data[j]=Data[j+1]
                Data[j+1]=Temp
Alpha(Data)
for p in Data:
     print(p,"",end="")
######################################################################
Data = list("ZABSDEFWGHICJKLPMNO")
#Sort the Data array using bubble sort.
#Then print the sorted array out on one line.
N = len(Data)
UnSorted = 1
while UnSorted:
    UnSorted = 0 # Set flag indicating data is sorted.
    k = 0
    while k < N-1:  # Bubble Sort
        if Data[k] > Data[k+1]:
            Tmp = Data[k]       #Swapping element order
            Data[k] = Data[k+1]
            Data[k+1] = Tmp
            UnSorted = 1        #Set flag indicating data is unsorted.
        k += 1

print("Sorted data is: ",end="")
for c in Data:
    print(c,"",end="")
print()


                
                       
                       
    


