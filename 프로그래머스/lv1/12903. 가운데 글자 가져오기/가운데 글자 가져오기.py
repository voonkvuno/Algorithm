def solution(s):
    idx = divmod(len(s),2)[0]
    return s[idx] if divmod(len(s),2)[1] else s[idx-1:idx+1]