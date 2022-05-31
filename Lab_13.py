from datetime import date

def time_dif(date,choice):
    diff = date - choice
    return diff

today = date.today()
napoleon = date(1769,8,15)
pearl = date(1941,12,7)
wright = date(1903,12,17)

choice = input("Would you like to calculate the time between today and: \n(1) Napoleon's brithday \n(2) The attack on Pearl Harbor \n(3) The flight of the Wright brothers\n:")

if choice == "1":
    print("Napoleon\'s birthday was on " + napoleon.strftime("%B %d, %Y") + ". That was {} ago.".format(time_dif(today,napoleon)))
elif choice == "2":
    print("The attack on Pearl Harbor occurred on " + pearl.strftime("%B %d, %Y") + ". That was {} ago.".format(time_dif(today,pearl)))
elif choice == "3":
    print("The Wright brothers flew their first flight on " + wright.strftime("%B %d, %Y") + ". That was {} ago.".format(time_dif(today,wright)))
else:
    print("Invalid Selection")