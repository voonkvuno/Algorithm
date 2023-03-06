def solution(s):
    answer = []
    word = {}
    for i, v in enumerate(s):
        if v not in word:
            answer.append(-1)
        else:
            answer.append(i - word[v])
        word[v] = i
    return answer