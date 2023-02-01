def solution(n):
    answer = 0
    for num in range(4,n+1):
        count = []
        for i in range(1,int(num**0.5)+1):
            if num%i == 0 and i**2 == num:
                count.append(1)
            elif num%i == 0 and i**2 != num:
                count.append(2)
        if sum(count) >= 3:
            answer += 1    
    return answer