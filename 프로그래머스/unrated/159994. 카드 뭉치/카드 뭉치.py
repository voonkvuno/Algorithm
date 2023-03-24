def solution(cards1, cards2, goal):
    cnt = 0
    for i in goal:
        if len(cards1) > 0 and i == cards1[0]:
            cards1.pop(0)
            cnt += 1
        elif len(cards2) > 0 and i == cards2[0]:
            cards2.pop(0)
            cnt += 1
    return "Yes" if len(goal) == cnt else "No"