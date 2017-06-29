"""This script is a guessing game. """

import random # Import random module to generate random numbers.

guesses_taken = 0 # Assign 0 to guesses_taken variable. This variable represents number of guesses taken by the user.

print('Hello! What is your name?') # Display text in console.
myName = input() # Request user input and assign it to myName variable.

number = random.randint(1, 20) # Generate random number between 1 and 20, then assign it to number variable.
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.') # Concatenate myName variable with text and display it in console.

while guesses_taken < 6: # Start while loop. Repeat until guesses_taken is not smaller than 6
    print('Take a guess.') # Display text in console.
    guess = input() # Request user input and assign it to guess variable.
    guess = int(guess) # Convert guess variable to int type

    guesses_taken += 1 # Increment guesses_taken by 1

    if guess < number: # Check if guess is smaller than number. If yes execute next line.
        print('Your guess is too low.') # Display text in console.

    if guess > number: # Check if guess is bigger than number. If yes execute next line.
        print('Your guess is too high.') # Display text in console.

    if guess == number: # Check if guess is equal to number. If yes execute next line.
        break # Exit while loop.

if guess == number: # Check if guess is equal to number. If yes execute next 2 lines.
    guesses_taken = str(guesses_taken) # Convert guesses_taken variable to string type
    print('Good job, ' + myName + '! You guessed my number in ' + guesses_taken + ' guesses!') # Concatenate myName and guesses_taken taken with text and display it in console.

if guess != number: # Check if guess is not equal to number. If yes execute next 2 lines.
    number = str(number) # Convert number variable to string type.
    print('Nope. The number I was thinking of was ' + number) # Concatenat number variable with text and display it in console.
