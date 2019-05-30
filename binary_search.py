# Author: Abdikarim Ibrahim

# Data for Binary Search
import random
random.seed()
# Build a list of random names in DataKeys.
dataKeys = []
for j in range(random.randint(40, 60)):  # the randint gives 40-60 inclusive
    # Create one random name.
    name = chr(random.randint(65, 90))  # give ASCII and convert in char
    for i in range(1, random.randint(3, 6)):
        name = name + chr(random.randint(97, 122))
    # print(name)
    dataKeys.append(name)
numDataKeys = len(dataKeys)

# Sort list
dataKeys.sort()
print("The following list contains", numDataKeys, "sorted names")
for j in range(numDataKeys):
    print(dataKeys[j], end="\t")  # end="/t" give tab each time
    if j % 8 == 7:
        print()
print()
key = dataKeys[random.randint(0, numDataKeys-1)]
print("Key to find is:", key)

# a binary serch to find Key in DataKeys.

num = (numDataKeys-1)
low = 0
high = num
index = int(num/2)
found = 0
while (found == 0) and low <= high:
    if key == dataKeys[index]:
        found = 1
    elif key > dataKeys[index]:
        low = index+1
        index = int((high+low)/2)
    elif key < dataKeys[index]:
        high = index-1
        index = int((high+low)/2)
print(key, index, dataKeys[index])
