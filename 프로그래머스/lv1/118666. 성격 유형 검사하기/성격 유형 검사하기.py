def solution(survey, choices):
    idx, ans = '', ''
    score = [0,3,2,1,0,1,2,3]

    for s, c in zip(survey, choices):
        if c < 4:
            idx += (s[0] * score[c])
        elif c > 4:
            idx += (s[1] * score[c])

    if idx.count('R') >= idx.count('T'): ans += 'R'
    else:   ans += 'T'
    if idx.count('C') >= idx.count('F'): ans += 'C'
    else:   ans += 'F'
    if idx.count('J') >= idx.count('M'): ans += 'J'
    else:   ans += 'M'
    if idx.count('A') >= idx.count('N'): ans += 'A'
    else:   ans += 'N'

    return ans