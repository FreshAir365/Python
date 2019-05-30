print("Abdikarim Ibrahim, Hw#5 ")
# This program is going to calculate the average of the random numbers and converts into a letter grade
import random
random.seed()
Count = 0
Sum =0
repeat=1
while repeat == 1:
    Score = random.randint(56,100)
    Sum = 0
    Count = 0
    while Score>=60:
        Count+=1
        Sum+=Score
        print("Your score is ",Score, "Your count is ",Count, "Your sum is ",Sum,)
        Score = random.randint(56,100)
    if Count !=0:
        Average = Sum/Count
        #print(Average)
        if Average>=90:
            print("Your average is:A ",Average)
        elif Average >=80 and Average<90:
            print("Your average is:B ",Average)
        elif Average >=70 and Average<80:
            print("Your average is:C ",Average)
        elif Average >=60 and Average<70:
            print("Your average is:D ",Average)
        else:
            print("Your average is:F n/",Average)
    else:
        print("No score for your result because zero can't be divided a number")
    ans=input("Would   you like to quit enter 'Y' for yes: ")
    if ans[0]=="Y" or ans[0]=="N":
        repeat=0
