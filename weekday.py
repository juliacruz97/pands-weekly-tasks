#Weekday.py is a program that  that outputs
# whether or not today is a weekday
#Author: Julia Cruz
from datetime import date 
# Extract today date from library
today = date.today()

if today.weekday() == 0:
    print("Today is: Monday - Yes, unfortunately today is a weekday.")
elif today.weekday() == 1:
    print("Today is: Tuesday - Yes, unfortunately today is a weekday.")
elif today.weekday() == 2:
    print("Today is: Wednesday - Yes, unfortunately today is a weekday.")
elif today.weekday() == 3:
    print("Today is: Thursday - Yes, unfortunately today is a weekday.")
elif today.weekday() == 4:
    print("Today is: Friday - Yes, unfortunately today is a weekday.")
elif today.weekday() == 5:
    print("Today is: Saturday - weekend- Huhuhh !!!")
else:
    print("Today is: Sunday - weekend - Huhuhuh!!!")

