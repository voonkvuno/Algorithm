def solution(price):
    answer = price
    
    if 100000 <= price < 300000:
        answer = price * 0.95
    elif 300000 <= price < 500000:
        answer = price * 0.9
    elif price >= 500000:
        answer = price * 0.8
        
    return int(answer)