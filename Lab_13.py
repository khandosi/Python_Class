from datetime import date
from datetime import datetime

# Custom function to calculate time differences
def time_dif(date,choice):
    diff = date - choice
    return diff

# Give instructions
print("This program will calculate the difference between today's date and certain historical events.")

# Initialize today's date and historical events
today = date.today()
napoleon = date(1769,8,15)
pearl = date(1941,12,7)
wright = date(1903,12,17)

# Print list of choices
choice = input("Would you like to calculate the time between today and: \n(1) Napoleon's brithday \n(2) The attack on Pearl Harbor \n(3) The flight of the Wright brothers\n(4) Custom date\n")

# Print results based on user's choice
if choice == "1":
    print("Napoleon\'s birthday was on " + napoleon.strftime("%B %d, %Y") + ". That was {} ago.".format(time_dif(today,napoleon)))
elif choice == "2":
    print("The attack on Pearl Harbor occurred on " + pearl.strftime("%B %d, %Y") + ". That was {} ago.".format(time_dif(today,pearl)))
elif choice == "3":
    print("The Wright brothers flew their first flight on " + wright.strftime("%B %d, %Y") + ". That was {} ago.".format(time_dif(today,wright)))
elif choice == "4":
    custom_input = input("Today's date is {}. Please enter the past date you would like to calculate from: \n(Use format mm/dd/yyyy)\n".format(today.strftime("%B %d, %Y")))
    custom_datetime = datetime.strptime(custom_input, '%m/%d/%Y')
    print("The time difference between today and " + custom_datetime.date().strftime("%B %d, %Y") + " is {}.".format(time_dif(today,custom_datetime.date())))
else:
    print("Invalid Selection")