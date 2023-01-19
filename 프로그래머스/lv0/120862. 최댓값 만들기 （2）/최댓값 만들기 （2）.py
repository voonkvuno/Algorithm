def solution(numbers):
    numbers.sort()
    return numbers[-2]*numbers[-1] if numbers[-2]*numbers[-1] > numbers[0] * numbers[1] else numbers[0] * numbers[1]