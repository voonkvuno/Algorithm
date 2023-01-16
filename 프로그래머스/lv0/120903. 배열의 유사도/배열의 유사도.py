def solution(s1, s2):
    answer = 0
    for arr1 in min(s1, s2):
        if arr1 in max(s1, s2):
            answer += 1
            
    return answer