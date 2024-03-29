from random import randint

print('Welcome to Guess the Number!')
print('In this game you have to guess a randomly chosen number between 1 and 100.')
print('To help you, there are indicators if the number is too high or too low.')
print('Good Luck!')

num = randint(1, 100)

guess = None

while num != guess:
    prompt = input('What is the number? ')
    guess = int(prompt)

    if guess > num:
        print('Too High.')
    if guess < num:
        print('Too Low. ')

print('You guessed the number. To play again press the play button.')