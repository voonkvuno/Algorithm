def solution(array):
    count = {}
    for i in set(array):
        count.setdefault(i, array.count(i))
    answer = [k for k, v in count.items() if max(count.values()) == v]
    return answer[0] if len(answer) == 1 else -1