import random
import time

A = ['rock', 'scissors', 'paper', 'lizard', 'spock']
a = [
    {
        'scissors': 'paper',
        'paper': 'rock',
        'rock': 'lizard',
        'lizard': 'spock',
        'spock': 'scissors'
    },
    {
        'scissors': 'lizard',
        'lizard': 'paper',
        'paper': 'spock',
        'spock': 'rock',
        'rock': 'scissors'
    }
]

while True:
    player = input('Your choice (rock paper scissors lizard spock)?>: ')
    print(f'Player: {player}')
    time.sleep(1.5)
    computer = random.choice(A)
    print(f'Computer: {computer}')
    time.sleep(1.5)
    if computer == player:
        print('Draw')
        print()
    for x in range(len(a)):
        for i in a[x].items():
            if player == i[0] and computer == i[1]:
                print("Player WIN!")
                print()
                break
            elif computer == i[0] and player == i[1]:
                print("Computer WIN!")
                print()
                break
    time.sleep(1.5)
    question = input('Repeat (y/n)?>: ')
    print()
    if question != 'y':
        exit()