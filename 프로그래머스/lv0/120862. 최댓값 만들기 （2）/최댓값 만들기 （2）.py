def solution(numbers):
    numbers.sort()
    return max(numbers[-2]*numbers[-1], numbers[0]*numbers[1])