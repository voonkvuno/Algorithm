def solution(s):
    answer = []
    word = {}
    for i, v in enumerate(s):
        if word.get(v,-1) == -1:
            answer.append(-1)
        else:
            answer.append(i - word[v])
        word[v] = i
    return answer