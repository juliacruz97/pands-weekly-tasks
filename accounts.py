# Accounts.py is a program  that reads in a 10 character account number 
# and outputs the account number with only the last 4 digits showing 
# (and the first 6 digits replaced with Xs).
# accounts.py program name
# Author = Julia Cruz

account_number = (input('Please enter an 10 digit account number: '))[0:10]
# Take the first 10 characters of the user's input, 
# ensuring it is a 10-digit number, 
# even if the user inputs more than that.

print('XXX-XXX-',account_number[-4:])  
# selects the last four characters of the string stored in account_number.
# showing only the last four digits and hiding the first six.