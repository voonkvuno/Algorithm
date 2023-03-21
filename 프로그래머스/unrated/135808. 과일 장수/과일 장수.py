def solution(k, m, score):
    cnt, box, answer = [0,0,0,0,0,0,0,0,0,0], 0, 0
    
    for i in score:
        cnt[i] += 1

    for i, v in reversed(list(enumerate(cnt))):
        box += v
        if box//m > 0:
            answer += i * m * (box//m)
            box = box%m
    
    return answer