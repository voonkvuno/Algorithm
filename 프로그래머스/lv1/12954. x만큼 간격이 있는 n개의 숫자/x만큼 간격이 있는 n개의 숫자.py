def solution(x, n):
    answer = []
    i = 0
    for _ in range(n):
        i += x
        answer.append(i)
    return answer