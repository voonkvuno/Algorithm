def factorial(n):
    if(n > 1):
        return n * factorial(n - 1)
    else:
        return 1

def solution(n):
    answer = 0
    for i in range(1,11):
        if factorial(i) <= n < factorial(i+1):
            answer = i
    return answer