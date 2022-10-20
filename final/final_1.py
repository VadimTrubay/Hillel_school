import random

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
    print()
    print(f'Player: {player}')
    computer = random.choice(A)
    print(f'Computer: {computer}')
    if player == computer:
        print('Draw')
        print()
        continue
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
    question = input('Repeat (Y/N)?')
    print()
    if question != 'Y':
        exit()