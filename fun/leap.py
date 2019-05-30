#Author: Abdikarim Ibrahim
#Date: 11/21/17
#Description: checks leap year.

def LeapYear(Year):
    if Year >=1752:
        if (Year%400==0) or ((Year%4==0) and not (Year%100==0)):
            return "Leap Year "
        else:
            return 'Not Leap Year'
    else:
        return "invalid "

def UserInput(Prompt): #Returns "None" if user aborts.
    while 1: # Exit loop by returning.
        #print("Enter q to "
              #"abort input.")
        ans = input(Prompt)
        if ans=="q":
            return "q"
        try:
            Numb=int(ans)
            if Numb>=0:
                return Numb
        except:
            pass
        print("** Invalid "
                  "input **")

#main program
def Main():
    Main=[1500,1900,2000,2001,2002,2003,2004]
    for i in Main:
        result=LeapYear(i)
        print(i,result)
    extraYear=1
    while extraYear !="q":
        extraYear=UserInput("Please Enter a year or 'q' to quit: ")
        if extraYear!="q":
            result=LeapYear(extraYear)
            print(extraYear,result)
        
Main()
    
        
