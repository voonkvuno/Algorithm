def solution(n):
    answer = 0
    ch = [0]*(n+1)
    for i in range(2, n+1):
        if ch[i] == 0:
            answer += 1
            for j in range(i, n+1, i):
                ch[j] = 1
                
    return answer