def solution(n):
    answer = [1,1]
    for i in range(2,n+1):
        answer.append(answer[i-2] + answer[i-1])

    return answer[-1] % 1234567