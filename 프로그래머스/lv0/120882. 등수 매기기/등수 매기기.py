def solution(score):
    avg = [(e+m)/2 for e, m in score]
    rank = sorted(avg, reverse=True)

    return [rank.index(i)+1 for i in avg]