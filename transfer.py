import random as r
import string

#def make_file(file):
#    f = open(file,'w')

def addLetters():
    random = r.choice(string.ascii_letters)
    return random 

def addIntegers():
    random = r.sample(range(0, 9999))
    return random

def addFloat():
    random = round(r.uniform(0, 100000), 2)
    return random

def main():
    input_file = input('Enter a file: ')
    #make_file(input_file)
    f = open(input_file, "a")
    
 

    letter = addLetters()
    integer = addIntegers()
    floater = addFloat()

    #i = 1
    #while i < 20:
    #    f.write('{}\n').format(letter)
    #    i += 1

main()
