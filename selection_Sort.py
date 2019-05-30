#Author: Abdikarim Ibrahim
#Date: 11/07/17
#Description: sort the ramdom int by using selection sort

import random
Data = [int(i) for i in range(20)]
k = len(Data)
while k > 0:
    k -= 1
    Data[k] = random.randint(1,20)


N=len(Data)
M=0
Temp=0
K=0
print("Ages unsorted: ",end=" ")
while M<N:
    print(Data[M],end=" ")
    M+=1
print()
while K<N:
    Youngest=Data[K]
    Index=K
    J=K+1
    while J<N:
        if Data[J]<Youngest:
            Youngest=Data[J]
            Index=J
        J+=1
    if K!=Index:
        Temp=Data[K]
        Data[K]=Data[Index]
        Data[Index]=Temp
    K+=1
print("Ages sorted: ",end=" ")
M=0
while M<N:
    print(Data[M],end=" ")
    M+=1
print()
    
        


    
