def solution(sides):
    large = max(sides)
    sides.remove(large)
    return 1 if large < sum(sides) else 2