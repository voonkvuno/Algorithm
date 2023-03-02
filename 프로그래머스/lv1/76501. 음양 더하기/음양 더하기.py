def solution(absolutes, signs):
    return sum([absolutes[i] if v else -absolutes[i] for i, v in enumerate(signs)])