def solution(board, moves):
    answer = 0
    basket = []
    for kan in moves:
        for row in range(len(board[0])):
            if board[row][kan-1] !=0:
                basket.append(board[row][kan-1])
                board[row][kan-1] = 0
                if len(basket) > 1 and basket[-1] == basket[-2]:
                    basket.pop()
                    basket.pop()
                    answer += 2
                break
    print(basket)
    return answer