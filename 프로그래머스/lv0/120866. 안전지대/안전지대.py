def solution(board):
    bomb = []
    # bomb 좌표 저장
    for x, row in enumerate(board):
        for y, r in enumerate(row):
            if r == 1:
                bomb.append([x,y])
    # danger 좌표 저장
    for x, y in bomb:
        if x > 0 and y > 0:  board[x-1][y-1] = 1
        if y > 0:  board[x][y-1] = 1
        if x < len(board)-1 and y > 0:  board[x+1][y-1] = 1
        if x > 0:  board[x-1][y] = 1
        if x < len(board)-1:   board[x+1][y] = 1
        if x > 0 and y < len(row)-1:  board[x-1][y+1] = 1
        if y < len(board)-1:  board[x][y+1] = 1
        if x < len(board)-1 and y < len(board)-1:  board[x+1][y+1] = 1
    
    return len(board)**2 - sum(sum(board, []))