# Author: Abdikarim Ibrahim
# Date: 11/01/17
# Description: translate general pseudocode of bubble sort into

data = list("ZABSDEFWHHICJKLPMNO")  # this is the initial code for the bubble sort
print(data)
g = 0
size = len(data)
while g < size - 1:
    k = 0
    while k < size - 1:
        if data[k] > data[k + 1]:
            tempt = data[k]
            data[k] = data[k + 1]
            data[k + 1] = tempt
            # print(k,Data)
        # else:
            #print("not swaping")
        k += 1
    g += 1
print(data)

