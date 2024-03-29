theBoard = {'1': ' ', '2': ' ', '3': ' ',
             '4': ' ', '5': ' ', '6': ' ', 
             '7': ' ', '8': ' ', '9': ' '}
boardKeys = []

#print(boardKeys)

for key in theBoard:
    boardKeys.append(key)

#print(boardKeys)
    
def printBoard(board):
    print('|-+-+-|')
    print( '|' + board['1'] + '|' + board['2'] + '|' + board['3'] + '|')
    print('|-+-+-|')
    print( '|' + board['4'] + '|' + board['5'] + '|' + board['6'] + '|')
    print('|-+-+-|')
    print( '|' + board['7'] + '|' + board['8'] + '|' + board['9'] + '|')
    print('|-+-+-|')

def game():
    turn = 'X'
    count = 0
    for i in range(10): 
        printBoard(theBoard)
        print('It is ' + turn + 's turn. Choose the place to put the ' + turn + '. You can enter any integer between 1 and 9, inclusive.')
        print('1 through 9 signify a 3x3 grid which 1 is the first tile in the first row, 2 is the second and three is the third.')
        print('Same for the second and third rows except they begin with 4 and 7.')
        move = input()
        if theBoard[move] == ' ':
            theBoard[move] = turn
            count += 1
        else:
            print('This cell is filled.')
            continue
        if count >= 5:
            if theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ':
                printBoard(theBoard)
                print('\nGame Over\n')
                print('Player ' + turn + ' won the game.')
                break
            if theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ':
                printBoard(theBoard)
                print('\nGame Over\n')
                print('Player ' + turn + ' won the game.')
                break
            if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ':
                printBoard(theBoard)
                print('\nGame Over\n')
                print('Player ' + turn + ' won the game.')
                break
            if theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ':
                printBoard(theBoard)
                print('\nGame Over\n')
                print('Player ' + turn + ' won the game.')
                break
            if theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ':
                printBoard(theBoard)
                print('\nGame Over\n')
                print('Player ' + turn + ' won the game.')
                break
            if theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ':
                printBoard(theBoard)
                print('\nGame Over\n')
                print('Player ' + turn + ' won the game.')
                break
            if theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ':
                printBoard(theBoard)
                print('\nGame Over\n')
                print('Player ' + turn + ' won the game.')
                break
            if theBoard['3'] == theBoard['5'] == theBoard['7'] != ' ':
                printBoard(theBoard)
                print('\nGame Over\n')
                print('Player ' + turn + ' won the game.')
                break
        if count == 9:
            print('\nGame Over\n')
            print('The game is a tie.')
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
        restart = input('Do you want to restart? Say yes or no.')
        if restart == 'Yes' or restart == 'yes':
            for key in boardKeys:
                theBoard[key] = ' '
        elif restart == 'No' or restart == 'no':
            print('Thank you for playing!')
            game()
if __name__ == '__main__':
    game()