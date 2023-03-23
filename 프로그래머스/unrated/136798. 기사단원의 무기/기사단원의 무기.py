def solution(number, limit, power):
    answer = 0
    for n in range(1,number+1):
        # 약수 계산
        cnt = 0
        for i in range(1,int(n**0.5)+1):
            if n%i == 0:
                cnt += 1
                if i**2 != n:
                    cnt += 1
        # 공격력 계산
        if limit >= cnt:
            answer += cnt
        else:
            answer += power
                
    return answer