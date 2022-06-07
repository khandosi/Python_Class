import math

again = 'y'

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


def weekly_hours():
    hours = []
    num1 = input(float("Enter the hours for Monday: "))
    hours.append(num1)
    num2 = input(float("Enter the hours for Tuesday: "))
    hours.append(num2)
    num3 = input(float("Enter the hours for Wednesday: "))
    hours.append(num3)
    num4 = input(float("Enter the hours for Thursday: "))
    hours.append(num4)
    num5 = input(float("Enter the hours for Friday: "))
    hours.append(num5)
    print(sum(hours))


def sq_pi():
    power_str = input("Enter the power of pi: ")
    power_float = float(power_str)
    result = pow(3.1415926535897932384626433832795, power_float)
    print(result)

while(again == 'y'):

    print('\nWhich of the following would you like to calculate?')
    option = ['Area of a circle', 'MPG for a vehicle',
            'Total number of hours worked in a week', 'Hypotenuse of a triangle', 'Raise Pi to an exponent']
    for x in option:
        print(x)
    choice = input('\nChoose 1, 2, 3, 4, or 5: ')

    if int(choice) == 1:
        c_area()
    elif int(choice) == 2:
        mpg()
    elif int(choice) == 3:
        cone_volume()
    elif int(choice) == 4:
        weekly_hours()
    elif int(choice) == 5:
        sq_pi()
    else:
        print("Error.")

# Ask to play again
    again = input("Would you like to play again? (y/n) : ")
