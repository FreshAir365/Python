# Author: Abdikarim Ibrahim
# print factorial a given number
N = 1
while N != 0:
    Numb = input(" Please enter a number between 1-20:, or 0 to quit ")
    try:
        N = int(Numb)
    except:
        print('Invalid input')
        N = -1
    if N > 20 or N < 0:
        print(" Your input is out not valid")
    else:
        Factorial = 1
        for I in range(1, N+1):  # Numb+1 gives me the last number of the range
            Factorial *= I
        print(N, Factorial)
        I = 1
        Factorial = 1
        while I <= N:
            Factorial *= I
            print(N, Factorial)
            I += 1
# else:
print(Factorial)
