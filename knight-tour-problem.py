board = [[0 for x in range(8)] for y in range(8)]
result = [[0 for x in range(8)] for y in range(8)]
counter = 0
res_counter = 0
def makeMove(board,currX,currY):
    global counter
    global res_counter

    if counter == 64:
        return True

    if currX>7 or currX<0 or currY>7 or currY<0 or board[currX][currY] == 1:
        return False
    else:
        counter += 1
        res_counter += 1

    board[currX][currY] = 1

    if makeMove(board,currX+1,currY+2):
        result[currX][currY] = res_counter
        res_counter -= 1
        return True
    elif makeMove(board,currX+2,currY+1):
        result[currX][currY] = res_counter
        res_counter -= 1
        return True
    elif makeMove(board,currX+2,currY-1):
        result[currX][currY] = res_counter
        res_counter -= 1
        return True
    elif makeMove(board,currX+1,currY-2):
        result[currX][currY] = res_counter
        res_counter -= 1
        return True
    elif makeMove(board,currX-1,currY-2):
        result[currX][currY] = res_counter
        res_counter -= 1
        return True
    elif makeMove(board,currX-2,currY-1):
        result[currX][currY] = res_counter
        res_counter -= 1
        return True
    elif makeMove(board,currX-2,currY+1):
        result[currX][currY] = res_counter
        res_counter -= 1
        return True
    elif makeMove(board,currX-1,currY+2):
        result[currX][currY] = res_counter
        res_counter -= 1
        return True
    else:
        if currX>7 or currX<0 or currY>7 or currY<0 or board[currX][currY] == 1:
            counter -= 1
            res_counter -= 1
            board[currX][currY]=0
        return False

makeMove(board,0,0)
print(result)
