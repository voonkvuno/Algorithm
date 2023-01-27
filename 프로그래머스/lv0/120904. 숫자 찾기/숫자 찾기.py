def solution(num, k):
    for i, v in enumerate(list(map(int,str(num))), 1):
        if k == v:
            return i
    return -1