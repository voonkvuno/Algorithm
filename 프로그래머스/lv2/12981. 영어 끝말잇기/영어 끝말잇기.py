def solution(n, words):
    for i, v in enumerate(words):
        if i == 0:
            continue
        if  v[0] != words[i-1][-1] or words[i] in words[:i]:
            return [(i%n)+1, (i//n)+1]
    return [0,0]