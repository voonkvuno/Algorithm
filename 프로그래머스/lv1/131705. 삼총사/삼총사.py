from itertools import combinations
def solution(number):
    return sum([1 for i in combinations(number,3) if sum(i) == 0])