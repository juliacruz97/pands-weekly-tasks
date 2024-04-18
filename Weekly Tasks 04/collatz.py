
collatz = num
number = int(input("Enter seed number : "))
while collatz(number) != 1:
    number = collatz(number)



print(number)