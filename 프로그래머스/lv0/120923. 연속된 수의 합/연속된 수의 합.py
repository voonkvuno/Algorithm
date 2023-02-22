def solution(num, total):
    answer = [total//num]
    l,r = total//num, total//num
    # med 보다 작은 수
    for i in range(num//2 - 1 if num%2 == 0 else num//2):
        l -= 1
        answer.append(l)
    # med 보다 큰 수
    for i in range(num//2):
        r += 1
        answer.append(r)
    sorted(answer)
    return sorted(answer)