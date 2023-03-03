def solution(left, right):
    return sum(-i if int(i**0.5)==i**0.5 else +i for i in range(left, right+1))