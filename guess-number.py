#This is a guess the Number game
import random

guessesTaken = 0

print('Hello! What is your name?')
myName = input()

number = random.randint(1,20)
print('well,' + myName + ',I am thinking of anumber between 1 and 20.')

for guessesTaken in range(6):
    print('Take a guess.')
    guess = input()
    guess = int(guess)

    if guess < number:
        print('Your guess is too low.')

    if guess > number:
        print('Your guess is too high.')

    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken + 1)
    print('Good job,' + myName + '! You guessed mynumber in' +guessesTaken + 'guesses!')

if guess !=number:
    number = str(number)
    print('Nope. The number I was thinking of was ' + number + '.')
