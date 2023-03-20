from collections import Counter

def solution(X, Y):
    x, y, answer = Counter(X), Counter(Y), []
    
    for i in x if len(X) < len(Y) else y:
        answer += (str(i) * min(X.count(str(i)), Y.count(str(i))))
    
    if len(answer) == 0:
        return '-1'
    if answer.count('0') == len(answer):
        return '0'
    return ''.join(sorted(answer, reverse=True))