
#option = ['Rock','Paper','Scissors','Lizard','Spock']
#finished = False
#print("\nThis is a game of Rock, Paper, Scissors, Lizard, Spock. Please choose an option below: \n")
#for x in option:
#        print(x)
#
#while finished == False:
#    answer = input("\nChoose an option: ")
#test update
# Import modules and initialize variables
import random


ties = 0
wins = 0
losses = 0


def testING(int):
    if int == 1:
        return 'rock'
    elif int == 2:
        return 'paper'
    elif int == 3:
        return 'scissors'
    elif int == 4:
        return 'lizard'
    elif int == 5:
        return 'spock'
    else:
        return 'Error'

# Start while loop
while True:

    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))


    # Get user guess and computer guess
    user_guess = input("Make a guess: ")
    
    r = random.randrange(1,6)
    com_guess = testING(r)
    print(com_guess)

    # Evaluate results guessed
    if user_guess == com_guess:
        print('You  ' + user_guess + ', and the computer guessed ' + com_guess + ', it is a tie.')
        ties += 1
    elif user_guess == 'rock' and com_guess == 'lizard' or com_guess == 'scissors':
        print('You guessed ' + user_guess + ', and the computer guessed ' + com_guess + ', you win!')
        wins += 1
    elif user_guess == 'paper' and com_guess == 'rock' or com_guess == 'spock':
        print('You guessed ' + user_guess + ', and the computer guessed ' + com_guess + ', you win!')
        wins += 1
    elif user_guess == 'scissors' and com_guess == 'paper' or com_guess == 'lizard':
        print('You guessed ' + user_guess + ', and the computer guessed ' + com_guess + ', you win!')
        wins += 1
    elif user_guess == 'lizard' and com_guess == 'paper' or com_guess == 'spock':
        print('You guessed ' + user_guess + ', and the computer guessed ' + com_guess + ', you win!')
        wins += 1
    elif user_guess == 'spock' and com_guess == 'rock' or com_guess == 'scissors':
        print('You guessed ' + user_guess + ', and the computer guessed ' + com_guess + ', you win!')
        wins += 1
    else:
        print('You guessed ' + user_guess + ', and the computer guessed ' + com_guess + ', you lose...')
        losses += 1

    while goAgain == False:
    # Ask to play again
    # while valid == False:
        playAgain = input("Would you like to play again? (y/n) : ")
        if playAgain == 'y':
            continue
        elif playAgain == 'n':
            break
        else:
            print("Please enter y or n.")
    break

 # Assign computer guess values
    if com_guess_int == 1:
        com_guess = 'rock'
    elif com_guess_int == 2:
        com_guess = 'paper'
    elif com_guess_int == 3:
        com_guess = 'scissors'
    elif com_guess_int == 4:
        com_guess = 'lizard'
    elif com_guess_int == 5:
        com_guess = 'spock'
    else:
        print("error")