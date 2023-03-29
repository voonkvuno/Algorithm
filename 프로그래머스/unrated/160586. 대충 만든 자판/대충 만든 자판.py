def solution(keymap, targets):
    answer = []
    for target in targets:
        result = 0
        for i in list(target):
            number = []
            for k in keymap:
                if i in k:
                    number.append(k.find(i))
            if len(number) == 0:
                result = -1
                break
            result += min(number) + 1
        answer.append(result)
    return answer