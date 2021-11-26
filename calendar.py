import calendar

cal = calendar.month(2021, 11)
print("Here is the November 2021 calendar: ")
print(cal)
#Gave an error AttributeError: partially initialized module 'calendar' has no attribute 'month' (most likely due to a circular import)
