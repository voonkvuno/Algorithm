def solution(s):
    stack = []
    for i, v in enumerate(s):
        if not stack:
            stack.append(v)
        else:
            if v == stack[-1]:
                stack.pop()
            else:
                stack.append(v)
    return 1 if not stack else 0