def solution(n,a,b):
    answer = 0
    flag = True
    while flag:
        answer += 1
        for i in range(1,n+1,pow(2,answer)):
            if i <= a < i+pow(2,answer) and i <= b < i+pow(2,answer):
                flag = False
                break
    return answer