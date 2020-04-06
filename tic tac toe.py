import random

board = [['-','-', '-'],
         ['-','-', '-'],
         ['-','-', '-']]

def printBoard(board):

    for row in board:
        print(row[0], row[1], row[2])
    print()
    return


def evaluate(board, isMax):

    mark = '-'
    isMax = not isMax
    
    for row in board:
        if(row[0]==row[1] and row[1]==row[2] and row[0]!='-'):
            mark = row[0]
    for i in range(3):
        if(board[0][i]==board[1][i] and board[1][i]==board[2][i] and board[0][i]!='-'):
            mark = board[0][i]
    if(board[0][0]==board[1][1] and board[1][1]==board[2][2] and board[0][0]!='-'):
        mark = board[0][0]
    if(board[0][2]==board[1][1] and board[1][1]==board[2][0] and board[0][2]!='-'):
        mark = board[0][2]
        
    if(mark=='x' and isMax):
        return 100
    elif(mark=='x' and not isMax):
        return -100
    if(mark=='o' and isMax):
        return 100
    elif(mark=='o' and not isMax):
        return -100

    return 0


def isBoardFull(board):
    for row in board:
        if '-' in row:
            return False
    return True

def minmax(board, depth, isMax):

    score = evaluate(board, isMax)
    if(score==100):
        return score - depth

    if(score==-100):
        return score + depth

    
    if (isBoardFull(board)):
        return 0

    if(isMax):
        bestVal = -1000
        for r in range(3):
            for c in range(3):
                if(board[r][c]=="-"):
                    board[r][c] = "x"
                    bestVal = max(bestVal, minmax(board, depth+1, not isMax))
                    board[r][c] = "-"
        return bestVal

    else:
        bestVal = 1000
        for r in range(3):
            for c in range(3):
                if(board[r][c]=="-"):
                    board[r][c] = "o"
                    bestVal = min(bestVal, minmax(board, depth+1, not isMax))
                    board[r][c] = "-"
        return bestVal


def findPos(move):
    c = (move%3)-1
    r = move//3
    if(c==-1):
        r = r-1
        c = 2
    return r,c 


firstGo = random.choice([0,1])
print("Initial Board")
printBoard(board)

if(firstGo):
    isMaxPlayer = True
    roboMark = 'x'
    humanMark = 'o'
    
else:
    isMaxPlayer = False
    roboMark = 'o'
    humanMark = 'x'

    pos = int(input("Human Turn: "))
    r,c = findPos(pos)
    while(board[r][c]!='-'):
        pos = int(input("Error! Human Turn: "))
        r,c = findPos(pos)
    board[r][c]=humanMark
    printBoard(board)

move = (2,0)
while(True):
    print("AI Turn :")
    if(isMaxPlayer):
        score = -1000
    else:
        score = 1000
        
    for r in range(3):
        for c in range(3):
            if(board[r][c]=='-'):
                board[r][c]=roboMark
                val = minmax(board, 0, not isMaxPlayer)
                board[r][c] = '-'
                if(isMaxPlayer):
                    if(val>score):
                        score = val
                        move = (r,c)
                else:
                    if(val<score):
                        score = val
                        move = (r,c)
                

    
    board[move[0]][move[1]]=roboMark
    printBoard(board)

    if(evaluate(board, isMaxPlayer)==100 or evaluate(board, isMaxPlayer)==-100):
        print("Robo Wins! Game Over!")
        break

    if(isBoardFull(board)):
        print("Game Over!")
        break
    
    pos = int(input("Human Turn: "))
    r,c = findPos(pos)
    while(board[r][c]!='-'):
        pos = int(input("Error! Human Turn: "))
        r,c = findPos(pos)
    board[r][c]=humanMark
    printBoard(board)

    if(evaluate(board, isMaxPlayer)==100 or evaluate(board, isMaxPlayer)==-100):
        print("Human Wins! Game Over!")
        break            
    
    if(isBoardFull(board)):
        print("Game Over!")
        break
