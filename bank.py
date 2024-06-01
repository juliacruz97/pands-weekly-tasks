# bank.py is a program which should:
# Prompt the user and read in two money amounts (in cent)
# Add the two amounts
# Print out the answer in a human readable format with a euro 
# sign and decimal point between the euro and cent of the amount. 
# Author : Julia Cruz


n1= float(input('Enter amount1 : €'))
n2= int(input('Enter amount 2: €'))

total = float (n1/100 + n2/100)
print ('The total sum of these is €',(total))
