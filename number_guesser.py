import random

top_range = input("Type a number: ")

if top_range.isdigit():
    top_range = int(top_range)
    if top_range <= 0:
        print("Please type a number larger than 0!")
        quit()
else:
    print('Please type a number next time')
    quit()
    

rando = random.randint(0, top_range)
guesses = 0

while True:
    guesses += 1
    guess = input("Guess the number: ")
    if guess.isdigit():
        guess = int(guess)
    else:
        print('Please type a number next time')
        continue

    if guess == rando:
        print('You guessed it!\n')
        break
    elif guess > rando:
        print("Too High! Try again\n")
    else:
        print('Too Low, try again\n')

print(f'You guessed the number in {guesses} tries! Good job!')

