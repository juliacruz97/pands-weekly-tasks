'''Write a program that takes a positive floating-point number as input and outputs an 
approximation of its square root.'''


n= int(input('Please enter a positive number: '))
n1= n+1
sqrt= n*n 
sqrt = n + (n1*n1)/(2*n1)
print(sqrt)