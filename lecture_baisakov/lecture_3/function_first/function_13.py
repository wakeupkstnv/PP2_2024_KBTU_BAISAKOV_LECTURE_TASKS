from random import randint

def guess_the_number():
    name = input('Hello! What is your name?\n')
    user_answer = None
    guesses_count = 0

    last_range = randint(20, 100)
    print(f'Well, {name}, I am thinking of a number between 1 and {last_range}.')

    random_number = randint(1, last_range)
    while user_answer != random_number:
        user_answer = int(input('Take a guess.\n'))
        guesses_count += 1

        if user_answer < random_number: print('Your guess is too low.')
        if user_answer > random_number: print('Your guess is too high')
        if user_answer == random_number: print(f'Good job, {name}! You guessed my number in {guesses_count} guesses!\n')

guess_the_number()