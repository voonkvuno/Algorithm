def solution(array):
    return sum([1 for val in array for i in str(val) if i == '7'])