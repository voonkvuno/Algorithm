def solution(id_list, report, k):
    answer = [0] * len(id_list)
    user = {i:0 for i in id_list}
    
    for r in set(report):
        user[r.split(' ')[1]] += 1

    for r in set(report):
        a, b = r.split(' ')
        if user[b] >= k:
            answer[id_list.index(a)] += 1
        
    return answer