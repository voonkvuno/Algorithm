import math

def solution(n):
    answer = 0
    for i in range(1, math.ceil(n**(1/2))):
        if n % i == 0:
            print(i)
            answer += 1
    return answer*2 + 1 if n % n**(1/2) == 0 else answer*2