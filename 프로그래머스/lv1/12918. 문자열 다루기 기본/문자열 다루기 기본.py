def solution(s):
    return True if (len(s) == 4 or len(s) == 6) and len(s) == sum(1 for i in s if i in '0123456789') else False