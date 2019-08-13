import random

alive = True
board = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

for i in range(100):
    print()

for i in range(2):
    emptySpaces = []
    for i in range(4):
        for j in range(4):
            emptySpaces.append((i,j))
    
    space = random.randint(0,len(emptySpaces)-1)
    
    if random.random() > 0.9:
        board[emptySpaces[space][0]][emptySpaces[space][1]] = 4
    else:
        board[emptySpaces[space][0]][emptySpaces[space][1]] = 2

while (alive):
    for i in board:
        for j in i:
            print(j, end = '')
            if j < 10:
                print('    ', end = '')
            elif j < 100:
                print('   ', end = '')
            elif j < 1000:
                print('  ', end = '')
            else:
                print(' ', end = '')
        print()
    
    uin = input("")
    
    move = False
    if uin == "w":
        for i in range(4):
            for j in range(4):
                k = j
                if board[j][i] != 0:
                    while k > 0:
                        if board[k-1][i] == 0:
                            board[k-1][i] = board[k][i]
                            board[k][i] = 0
                            k-=1
                            move = True
                        else:
                            if board[k-1][i] == board[k][i]:
                                board[k-1][i] = 2*board[k][i]
                                board[k][i] = 0
                                move = True
                            break
    elif uin == "s":
        for i in range(4):
            for j in range(4):
                k = j
                if board[3-k][i] != 0:
                    while k > 0:
                        if board[3-k+1][i] == 0:
                            board[3-k+1][i] = board[3-k][i]
                            board[3-k][i] = 0
                            k-=1
                            move = True
                        else:
                            if board[3-k+1][i] == board[3-k][i]:
                                board[3-k+1][i] = 2*board[3-k][i]
                                board[3-k][i] = 0
                                move = True
                            break
    elif uin == "a":
        for i in range(4):
            for j in range(4):
                k = j
                if board[i][k] != 0:
                    while k > 0:
                        if board[i][k-1] == 0:
                            board[i][k-1] = board[i][k]
                            board[i][k] = 0
                            k-=1
                            move = True
                        else:
                            if board[i][k-1] == board[i][k]:
                                board[i][k-1] = 2*board[i][k]
                                board[i][k] = 0
                                move = True
                            break
    elif uin == "d":
        for i in range(4):
            for j in range(4):
                k = j
                if board[i][3-k] != 0:
                    while k > 0:
                        if board[i][3-k+1] == 0:
                            board[i][3-k+1] = board[i][3-k]
                            board[i][3-k] = 0
                            k-=1
                            move = True
                        else:
                            if board[i][3-k+1] == board[i][3-k]:
                                board[i][3-k+1] = 2*board[i][3-k]
                                board[i][3-k] = 0
                                move = True
                            break
    else:
        move = True
    
    emptySpaces = []
    if move:
        for i in range(4):
            for j in range(4):
                if board[i][j] == 0:
                    emptySpaces.append((i,j))
                    
    if len(emptySpaces) > 0:
        space = random.randint(0,len(emptySpaces)-1)

        if random.random() > 0.9:
            board[emptySpaces[space][0]][emptySpaces[space][1]] = 4
        else:
            board[emptySpaces[space][0]][emptySpaces[space][1]] = 2
    else:
        alive = False
    
