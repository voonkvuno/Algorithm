def solution(food):
    answer = ''
    for i, v in enumerate(food):
        if i > 0 and v//2 > 0:
            answer += str(i)*(v//2)
    return answer + '0' + ''.join(reversed(answer))