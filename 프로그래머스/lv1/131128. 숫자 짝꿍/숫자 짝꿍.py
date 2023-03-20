def solution(X, Y):
    x, y, answer = {}, {}, []
    
    for i in X:
        x[i] = x.get(i, 0) + 1
    for i in Y:
        y[i] = y.get(i, 0) + 1
    
    for i in x if len(X) < len(Y) else y:
        if x.get(i,0) >= y.get(i,0):
            answer += i*y.get(i,0)
        else:
            answer += i*x.get(i,0)
    
    if len(answer) == 0:
        return '-1'
    if answer.count('0') == len(answer):
        return '0'
    return ''.join(sorted(answer, reverse=True))