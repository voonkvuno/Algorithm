def solution(numbers, k):
    return numbers[((k*2-1)%len(numbers))-1]