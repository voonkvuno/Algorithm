from itertools import combinations
def solution(nums):
    answer = 0
    bp = False
    for i in combinations(nums,3):
        for j in range(2, (int(sum(i))//2)+1):
            if sum(i) % j == 0:
                answer -= 1
                break
        answer += 1
    return answer if answer > 0 else 0