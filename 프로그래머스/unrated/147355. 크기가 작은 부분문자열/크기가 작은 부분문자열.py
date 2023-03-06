def solution(t, p):
    answer = 0
    for i in range(len(t)-len(p)+1):
        comp = t[i:i+len(p)]
        if len(comp) > 1 and comp[0] == '0':
            comp = comp[1:]
        if int(comp) <= int(p):
            answer += 1
    return answer