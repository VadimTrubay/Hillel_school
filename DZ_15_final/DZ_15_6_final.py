import random
import os


def board():
    print(' 1' + ' | ' + '2' + ' | ' + '3 ')
    print('---+---+---')
    print(' 4' + ' | ' + '5' + ' | ' + '6 ')
    print('---+---+---')
    print(' 7' + ' | ' + '8' + ' | ' + '9 ')


def draw_board(board):

    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('---+---+---')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('---+---+---')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])


def who_goes_first():
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'


def play_again():
    print('Do you want to play again?(y/n)')
    return input().lower().startswith('y')


def make_move(board, letter, move):
    board[move] = letter


def winner(bo, le):
    return ((bo[1] == le and bo[2] == le and bo[3] == le) or
            (bo[4] == le and bo[5] == le and bo[6] == le) or
            (bo[7] == le and bo[8] == le and bo[9] == le) or
            (bo[1] == le and bo[4] == le and bo[7] == le) or
            (bo[2] == le and bo[5] == le and bo[8] == le) or
            (bo[3] == le and bo[6] == le and bo[9] == le) or
            (bo[1] == le and bo[5] == le and bo[9] == le) or
            (bo[3] == le and bo[5] == le and bo[7] == le))


def get_board_copy(board):
    dupe_board = []

    for i in board:
        dupe_board.append(i)

    return dupe_board


def space_free(board, move):
    return board[move] == ' '


def get_player_move(board):
    move = ''
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not space_free(board, int(move)):
        print('your turn (1-9): ')
        move = input()
    return int(move)


def choose_random_move_from_list(board, moves_list):
    possible_moves = []
    for i in moves_list:
        if space_free(board, i):
            possible_moves.append(i)

    if len(possible_moves) != 0:
        return random.choice(possible_moves)
    else:
        return None


def get_computer_move(board, computer_letter):
    if computer_letter == 'x':
        player_letter = '0'
    else:
        player_letter = 'x'

    for i in range(1, 10):
        copy = get_board_copy(board)
        if space_free(copy, i):
            make_move(copy, computer_letter, i)
            if winner(copy, computer_letter):
                return i
    for i in range(1, 10):
        copy = get_board_copy(board)
        if space_free(copy, i):
            make_move(copy, player_letter, i)
            if winner(copy, player_letter):
                return i
    move = choose_random_move_from_list(board, [1, 3, 7, 9])
    if move != None:
        return move
    if space_free(board, 5):
        return 5
    return choose_random_move_from_list(board, [2, 4, 6, 8])


def board_full(board):
    for i in range(1, 9):
        if space_free(board, i):
            return False
    return True


while True:
    theBoard = [' '] * 10
    player_Letter = 'x'
    computer_letter = '0'
    turn = who_goes_first()
    print('Will be the first to walk ' + turn + '\n')
    gameIsPlaying = True
    while gameIsPlaying:
        os.system('cls')
        print("Let's play x or 0!")
        print("Player plays for x, computer plays for 0")
        if turn == 'player':
            draw_board(theBoard)
            move = get_player_move(theBoard)
            make_move(theBoard, player_Letter, move)
            if winner(theBoard, player_Letter):
                draw_board(theBoard)
                print('Congratulations!!! You have won the game!')
                gameIsPlaying = False
            else:
                if board_full(theBoard):
                    draw_board(theBoard)
                    print('Draw!')
                    break
                else:
                    turn = 'computer'
        else:
            move = get_computer_move(theBoard, computer_letter)
            make_move(theBoard, computer_letter, move)
            if winner(theBoard, computer_letter):
                draw_board(theBoard)
                print('The computer won!')
                gameIsPlaying = False
            else:
                if board_full(theBoard):
                    draw_board(theBoard)
                    print('Draw!')
                    break
                else:
                    turn = 'player'

    if not play_again():
        break

