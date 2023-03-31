def solution(n,a,b):
    answer = 0
    round = [i for i in range(n+1)]
    flag = True
    while flag:
        answer += 1
        for i in range(1,n+1,pow(2,answer)):
            if a in round[i:i+pow(2,answer)] and b in round[i:i+pow(2,answer)]:
                flag = False
                break
    return answer