def solution(array, height):
    return sum([ 1 for arr in array if arr > height ])