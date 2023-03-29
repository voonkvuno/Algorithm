def solution(s):     
    return ' '.join([i[:1].upper() + i[1:].lower() for i in s.split(' ')])