def solution(k, score):
    answer = []
    top_k = score[0:k]
    
    for i, v in enumerate(score):
        if i < k:
            answer.append(min(score[:i+1]))              
        else:
            if min(top_k) < v:
                top_k[top_k.index(min(top_k))] = v
            answer.append(min(top_k))
    
    return answer