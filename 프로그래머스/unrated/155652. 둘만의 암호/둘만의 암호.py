def solution(s, skip, index):
    answer = ''
    alphabet = [i for i in list('abcdefghijklmnopqrstuvwxyz') if i not in skip ]
    
    for i in s:
        idx = alphabet.index(i) + index
        answer += alphabet[idx % len(alphabet)]
        
    return answer