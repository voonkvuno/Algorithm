def solution(n):
    answer = []
    cnt = 0
    for i in range(2,n+1):
        while n%i == 0:
            n = n//i
            cnt = 1
        if cnt == 1:
            answer.append(i)
        cnt = 0
    return answer