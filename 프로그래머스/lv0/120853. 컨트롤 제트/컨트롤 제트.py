def solution(s):
    answer = 0
    for idx, val in enumerate(s.split()):
        if val == 'Z':
            answer -= int(s.split()[idx-1])
        else:
            answer += int(val)
    return answer