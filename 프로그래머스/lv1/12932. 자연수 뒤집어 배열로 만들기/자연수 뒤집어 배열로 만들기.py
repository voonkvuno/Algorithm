def solution(n):
    answer = ''
    for i in str(n):
        answer = i + answer
    return [int(i) for i in answer]