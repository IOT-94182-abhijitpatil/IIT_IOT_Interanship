import datetime

# get current date and time 
now = datetime.datetime.now()

#Display current date time and day
print("Current Date and Time: ",now)
print("Day of the week: ",now.strftime("%A"))

