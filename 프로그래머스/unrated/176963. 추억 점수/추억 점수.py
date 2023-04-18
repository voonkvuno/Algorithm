def solution(name, yearning, photo):
    answer = []
    dic = {a:b for a, b in zip(name, yearning)}
    for p in photo:
        answer.append(sum([dic[i] for i in p if i in dic.keys()]))
    return answer