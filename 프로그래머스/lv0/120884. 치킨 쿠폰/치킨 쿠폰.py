def solution(chicken):
    answer = 0
    
    while divmod(chicken,10)[0]:
        answer += divmod(chicken,10)[0]
        chicken = divmod(chicken,10)[0] + divmod(chicken,10)[1]
        
    return answer