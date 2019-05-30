# Author: Abdikarim Ibrahim

FirstName=(input("Please enter your first name: or space to quit: "))
LastName=(input("Please enter your last name: or space to quit: "))
Length1= len(FirstName)
Length2=len(LastName)
Cont="Y"
while FirstName!=(" ") or LastName!=(" "):
    for i in range(Length2):
        print(FirstName," ", end=LastName+"\n")
        print(Length1,  "          ",end=" ")
        print(Length2)
        ans=(input("Do you like to process another name (Y/N) 'Y': or enter space to quit "))
        FirstName=(input("Please enter your first name: or space to quit: "))
        LastName=(input("Please enter your last name: or space to quit: "))
        Length1= len(FirstName)
        Length2=len(LastName)
    for j in rang(Length2):
        print(FirstName," ", end=LastName+"\n")
        print(Length1,  "          ",end=" ")
        print(Length2)
else:
        print("See you again")
