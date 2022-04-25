

print('Which of the following would you like to calculate?')
option = ['Area of a circle','MPG for a vehicle','Total number of hours worked in a week','Hypotenuse of a triangle','Placeholder']
for x in option:
        print(x)


#import random
#
#def goAgain():
#    str = input("Would you like to play again? (y/n):")
#    if str == 'y':
#        return 'yes'
#    elif str == 'n':
#        return 'no'
#    else:
#        return None
#
#goAgain()
import math

#def c_area(int1):
#    sum1 = int1 * 3.14
#    return sum1

#def mpg(int1,int2):
#    sum1 = int1 / int2
#    return sum1

done = False
hours = []

while done == False:
    num_1 = input("Enter a number: ")
    if num_1 == '':
        done = True
    else:
        hours.append(num_1)

print(sum(hours))




