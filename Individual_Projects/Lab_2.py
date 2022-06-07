import random

ties = 0
wins = 0
losses = 0
again = 'y'


def com_choice(int):
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
while(again == 'y'):

    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))

    # Get user guess and computer guess
    user_guess = input("Make a guess: ")

    r = random.randrange(1, 6)
    com_guess = com_choice(r)
    print(com_guess)

    # Evaluate results guessed
    if user_guess == com_guess:
        print('You  ' + user_guess + ', and the computer guessed ' +
              com_guess + ', it is a tie.')
        ties += 1
    elif (user_guess == 'rock') and (com_guess == 'lizard' or com_guess == 'scissors'):
        print('You guessed ' + user_guess +
              ', and the computer guessed ' + com_guess + ', you win!')
        wins += 1
    elif (user_guess == 'paper') and (com_guess == 'rock' or com_guess == 'spock'):
        print('You guessed ' + user_guess +
              ', and the computer guessed ' + com_guess + ', you win!')
        wins += 1
    elif (user_guess == 'scissors') and (com_guess == 'paper' or com_guess == 'lizard'):
        print('You guessed ' + user_guess +
              ', and the computer guessed ' + com_guess + ', you win!')
        wins += 1
    elif (user_guess == 'lizard') and (com_guess == 'paper' or com_guess == 'spock'):
        print('You guessed ' + user_guess +
              ', and the computer guessed ' + com_guess + ', you win!')
        wins += 1
    elif (user_guess == 'spock') and (com_guess == 'rock' or com_guess == 'scissors'):
        print('You guessed ' + user_guess +
              ', and the computer guessed ' + com_guess + ', you win!')
        wins += 1
    else:
        print('You guessed ' + user_guess +
              ', and the computer guessed ' + com_guess + ', you lose...')
        losses += 1

    # Ask to play again
        again = input("Would you like to play again? (y/n) : ")
