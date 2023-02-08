def solution(num_list, n):
    answer, n_list, cnt = [], [], 0
    
    for i in num_list:
        n_list.append(i)
        cnt += 1
        if cnt == n:
            answer.append(n_list)
            n_list, cnt = [], 0
    
    return answer