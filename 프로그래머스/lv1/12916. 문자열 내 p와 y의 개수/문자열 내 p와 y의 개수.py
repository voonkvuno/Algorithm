def solution(s):
    p, y = 0, 0
    for i in s:
        if i == 'p' or i.lower() == 'p':
            p += 1
        if i == 'y' or i.lower() == 'y':
            y += 1
    return True if p == y else False