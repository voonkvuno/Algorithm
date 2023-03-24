def solution(s):
    x, x_cnt, not_cnt, answer = 0, 0, 0, ''
    for i, v in enumerate(s):
        answer += v
        if i == 0:
            x = v
            x_cnt += 1
        else:
            if x == v:
                x_cnt += 1
            else:
                not_cnt += 1
        if i < len(s)-1 and x_cnt == not_cnt:
            answer += ' '
            x = s[i+1]
    return len(answer.split(' '))