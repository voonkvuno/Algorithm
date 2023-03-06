def solution(a, b, n):
    answer = 0
    while n >= a:
        coke, reminder = divmod(n,a)
        answer += coke*b
        n = coke*b + reminder
    return answer