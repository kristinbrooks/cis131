"""
    script: guess-the-number.py
    action: Write a script that plays “guess the number.” Choose the number to be guessed by selecting a random integer
     in the range 1 to 1000. Do not reveal this number to the user. Display the prompt "Guess my number between 1 and
     1000 with the fewest guesses:". The player inputs a first guess. If the guess is incorrect, display "Too high.
     Try again." or "Too low. Try again." as appropriate to help the player “zero in” on the correct answer, then
     prompt the user for the next guess. Count the number of guesses the player makes. If the number is 10 or fewer,
     display "Either you know the secret or you got lucky!" If the player makes more than 10 guesses, display "You
     should be able to do better!" When the user enters the correct answer, display "Congratulations. You guessed the
     number!” and allow the user to choose whether to play again.
    author: Kristin Brooks
    date:   06/04/26
"""
import random

# initialize variable to enter game loop
continue_play = 'y'

# start playing the game
while continue_play == 'y':
    # set the random number for guessing
    random_number = random.randint(1, 1000)

    # get first guess from the user and set guess counter
    guess = int(input('Guess my number between 1 and 1000 with the fewest guesses: '))
    num_guesses = 1

    # process wrong guesses
    while guess != random_number:

        # determine if guess is high or low and give user a hint
        if guess > random_number:
            print('Too high. Try again.')
        else:
            print('Too low. Try again.')

        # get next guess from the user
        guess = int(input('Guess again: '))

        # track number of guesses
        num_guesses += 1

    # tell user they have won
    print('Congratulations. You guessed the number!')

    # give user feedback based on number of guesses
    if num_guesses <= 10:
        print('Either you know the secret or you got lucky!')
    else:
        print('You should be able to do better!')

    # find out if user wants to play the game again or not
    continue_play = input('Do you want to play again? (y/n): ').lower()
