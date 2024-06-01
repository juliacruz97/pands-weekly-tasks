# Collatz.py, is a program that asks the user to input any positive integer and 
# outputs the successive values of the following calculation.
# At each step calculate the next value by taking the current value and, 
# if it is even, divide it by two, but if it is odd, multiply it by three and add one.
# Have the program end if the current value is one.
# Author: Julia Cruz

import sys  # The line of code "import sys" in Python means that the sys module is being imported.

def collatz (num): # def: It's the keyword used in Python to define a function. collatz: It's the name of the function being defined.
    if num == 1:
       return 1
    if num % 2 == 0:
       print(num//2)
       return collatz (num//2)
    else:
       print(3 * num + 1)
       return collatz (3 * num + 1)
    
run = True
while run:
    try:
       ans = int(input('Input any positive number:  '))
    except:
       print("You must input an integer. ")
       continue
    if ans == 0:
       sys.exit()
    else:
       while collatz (ans) !=1:
          collatz(ans)
       if collatz(ans) ==1:
          continue