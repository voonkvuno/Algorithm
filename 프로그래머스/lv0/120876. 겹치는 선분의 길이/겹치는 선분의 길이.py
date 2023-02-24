def solution(lines):
    dot, answer = {}, 0
    for a, b in lines:
        for i in range(a, b):
            dot[i] = dot.get(i, 0) + 1
    for k, v in dot.items():
        if v > 1:
            answer += 1
    return answer