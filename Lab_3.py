

import math

print('\nWhich of the following would you like to calculate?')
option = ['Area of a circle','MPG for a vehicle','Total number of hours worked in a week','Hypotenuse of a triangle','Placeholder']
for x in option:
        print(x)
choice = input('\nChoose 1, 2, 3, 4, or 5: ')


def c_area():
    str1 = input("Enter the diameter: ")
    int1 = int(str1)
    area = int1 * 3.14
    print(area)

def mpg():
    str1 = input("Enter the distance traveled: ")
    dist = int(str1)
    str2 = input("Enter the number of gallons used: ")
    gallons = int(str2)
    mpg = dist / gallons
    print(mpg)

def cone_volume():
    str1 = input("Enter the radius: ")
    radius = int(str1)
    str2 = input("Enter the height: ")
    height = int(str2)
    radius_sq = pow(radius, 2)
    volume = (1/3) * 3.14 * radius_sq * height
    print(volume)

cone_volume()

#done = False
#hours = []

#while done == False:
#    num_1 = input("Enter a number: ")
#    if num_1 == '':
#        done = True
#    else:
#        hours.append(num_1)


if choice == 1:
    c_area()
elif choice == 2:
    mpg()

c_area()

mpg()



