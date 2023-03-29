def solution(keymap, targets):
    answer = []
    for target in targets:
        result = 0
        for i in list(target):
            number = []
            for k in keymap:
                if i in k:
                    number.append(k.find(i))
            if len(number) == 0:
                result = -1
                break
            result += min(number) + 1
        answer.append(result)
    return answer

def solution(keymap, targets):
    answer = []
    
    for word in targets:
        times = 0
        for char in word:
            flag = False
            time = 101
            for key in keymap:      
                if char in key:
                    time = min(key.index(char)+1, time)
                    flag = True
                    
            if not flag:           # 만약 keymap을 전부다 돌았는데도 문자를 찾지 못하면
                times = -1;break   # 목표 문자열을 작성할 수 없음 
            
            times += time          # 하나의 문자에 대해 누른 키를 총합(키)에 더해줌
            
        answer.append(times)        
        # targets에 있는 하나의 단어에 대해 수행이 끝났으면 answer에 누른 키 총합을 넣어줌
    
    return answer