def solution(dartResult):
    dartResult = dartResult.replace('10','A')
    bonus = {'S':1, 'D':2, 'T':3}
    score = []
    for i, v in enumerate(dartResult):
        if v in bonus:
            score.append(int((dartResult[i-1]).replace('A','10')) ** bonus[v])
        elif v == '*':
            score[-1] *= 2
            if len(score) > 1:
                score[-2] *= 2
        elif v == '#':
            score[-1] *= -1
    return sum(score)