def solution(numbers, k):
    answer = 0
    order = numbers * (((k*2-1)//len(numbers))+1)
    return order[k*2-2]