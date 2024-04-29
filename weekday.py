from datetime import date 
# Extract today date from library
today = date.today()

if today.weekday() == 0:
    print("Today is: Monday - weekday")
elif today.weekday() == 1:
    print("Today is: Tuesday - weekday")
elif today.weekday() == 2:
    print("Today is: Wednesday - weekday")
elif today.weekday() == 3:
    print("Today is: Thursday - weekday")
elif today.weekday() == 4:
    print("Today is: Friday - weekday")
elif today.weekday() == 5:
    print("Today is: Saturday - weekend- Huhuhh ")
else:
    print("Today is: Sunday - weekend - Huhuhuh")

