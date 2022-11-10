import random

print("Welcome to the game!")

questions = ['What does HTML stand for?', 'What does CPU stand for?', 'What does RAM stand for?']
answers = ['hyper text markup language', 'central processing unit', 'random access memory']

playing = input("Do you want to play? ")

if playing.lower() != 'yes':
    quit()

print("Great! Lets play!")

randomquestion = random.choices(questions)
score = 0

for question in questions:
    print(question)
    answer = input("")
    if answer.lower() == 'hyper text markup language': # or 'random access memory' or 'central processing unit':
        print('Correct!\n')
        score += 1
    elif answer.lower() == 'central processing unit':
        print('Correct!\n')
        score += 1
    elif answer.lower() == 'random access memory':
        print('Correct!\n')
        score += 1
    else:
        print('Incorrect!\n')


print("Nice job!")
print(f'Final Score: {score}')