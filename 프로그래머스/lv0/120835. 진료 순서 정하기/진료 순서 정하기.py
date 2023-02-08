def solution(emergency):
    answer = []
    rank = sorted(emergency, reverse=True)
    for i in emergency:
        answer.append(rank.index(i)+1)
    return answer