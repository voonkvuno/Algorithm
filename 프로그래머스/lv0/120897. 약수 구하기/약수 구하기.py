def solution(n):
    answer = []
    for i in range(1,int(n**0.5)+1):
        if not divmod(n,i)[1]:
            answer.append(i)
            answer.append(divmod(n,i)[0])
    return sorted(set(answer))