import random


def board():
    print(' 1' + ' | ' + '2' + ' | ' + '3')
    print('---+---+---')
    print(' 4' + ' | ' + '5' + ' | ' + '6')
    print('---+---+---')
    print(' 7' + ' | ' + '8' + ' | ' + '9')


def drawBoard(board):
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('---+---+---')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('---+---+---')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])


def whoGoesFirst():
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'


def playAgain():
    print('Do you want to play again?(y/n)')
    return input().lower().startswith('y')


def makeMove(board, letter, move):
    board[move] = letter


def isWinner(bo, le):
    return ((bo[1] == le and bo[2] == le and bo[3] == le) or
            (bo[4] == le and bo[5] == le and bo[6] == le) or
            (bo[7] == le and bo[8] == le and bo[9] == le) or
            (bo[1] == le and bo[4] == le and bo[7] == le) or
            (bo[2] == le and bo[5] == le and bo[8] == le) or
            (bo[3] == le and bo[6] == le and bo[9] == le) or
            (bo[1] == le and bo[5] == le and bo[9] == le) or
            (bo[4] == le and bo[5] == le and bo[7] == le))


def getBoardCopy(board):
    dupe_board = []
    for i in board:
        dupe_board.append(i)
    return dupe_board


def isSpaceFree(board, move):
    return board[move] == ' '


def getPlayerMove(board):
    move = ''
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('your turn (1-9): ')
        move = input()
    return int(move)


def chooseRandomMoveFromList(board, moves_list):
    possible_moves = []
    for i in moves_list:
        if isSpaceFree(board, i):
            possible_moves.append(i)
    if len(possible_moves) != 0:
        return random.choice(possible_moves)
    else:
        return None


def getComputerMove(board, computer_letter):
    if computer_letter == 'x':
        player_letter = '0'
    else:
        player_letter = 'x'
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, computer_letter, i)
            if isWinner(copy, computer_letter):
                return i
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, player_letter, i)
            if isWinner(copy, player_letter):
                return i
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move
    if isSpaceFree(board, 5):
        return 5
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])


def isBoardFull(board):
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True


print("Let's play x or 0!")
print("Player plays for x, computer plays for 0")
board()
print()
while True:
    theBoard = [' '] * 9
    playerLetter = 'x'
    computer_letter = '0'
    turn = whoGoesFirst()
    print('Will be the first to walk ' + turn + '\n')
    gameIsPlaying = True
    while gameIsPlaying:
        if turn == 'player':
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)
            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print('Congratulations!!! You have won the game!')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('Draw!')
                    break
                else:
                    turn = 'computer'
        else:
            move = getComputerMove(theBoard, computer_letter)
            makeMove(theBoard, computer_letter, move)
            if isWinner(theBoard, computer_letter):
                drawBoard(theBoard)
                print('The computer won!')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('Draw!')
                    break
                else:
                    turn = 'player'

    if not playAgain():
        break
