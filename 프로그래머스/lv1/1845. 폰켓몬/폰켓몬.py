def solution(nums):
    answer = 0
    number = len(nums)//2
    d = {}

    for i in nums:
        d[i] = d.get(i,0) + 1
    
    if len(d) > number:
        answer = number
    else:
        answer = len(d)
        
    return answer