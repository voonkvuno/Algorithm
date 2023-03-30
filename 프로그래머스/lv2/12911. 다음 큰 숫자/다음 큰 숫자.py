def solution(n):
    n_cnt = bin(n)[2:].count('1')
    next_cnt = 0
    while n_cnt != next_cnt:
        n += 1
        next_cnt = bin(n)[2:].count('1')
    return n