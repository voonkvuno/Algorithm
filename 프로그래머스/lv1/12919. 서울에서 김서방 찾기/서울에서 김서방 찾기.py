def solution(seoul):
    answer = ''
    for idx, val in enumerate(seoul):
        if val == 'Kim':
            answer = '김서방은 ' + str(idx) + '에 있다'
    return answer