def solution(keyinput, board):
    answer = [0,0]
    
    for key in keyinput:
        if key == 'up':
            answer[0] += 0
            answer[1] += 1
        elif key == 'down':
            answer[0] += 0
            answer[1] += -1
        elif key == 'left':
            answer[0] += -1
            answer[1] += 0
        elif key == 'right':
            answer[0] += 1
            answer[1] += 0
            
        for i in range(2):
            if answer[i] <= (board[i]//2)*(-1):
                answer[i] = (board[i]//2)*(-1)
            elif answer[i] >= board[i]//2:
                answer[i] = board[i]//2
        
    return answer