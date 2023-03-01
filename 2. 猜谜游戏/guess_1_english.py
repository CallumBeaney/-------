import random
numberToGuess = random.randint(1, 10)

user_name = input("What's your name?\n") # \n == insert a newline
numberOfGuesses = 0
print('I\'m glad to meet you, {} \nLet\'s play a game -- I will think of a number between 1 and 10 then you will guess! \nDon\'t forget: you have only 3 chances! So, guess a number:'.format(user_name))

while numberOfGuesses < 3:
    guess = int(input())
    numberOfGuesses += 1
    if guess < numberToGuess:
        print('Your estimate is too low, go up a little!')
    if guess > numberToGuess:
        print('Your estimate is too high, go down a bit!')
    if guess == numberToGuess:
        break
if guess == numberToGuess:
    print( 'Congratulations {}, you guessed the number in {} tries!'.format(user_name, numberOfGuesses))
else:
    print('Close but no cigar, you couldn\'t guess the number. \nWell, the number was {}.'.format(numberToGuess))