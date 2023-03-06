def solution(s, n):
    answer = ''
    a_to_z = list('abcdefghijklmnopqrstuvwxyz')
    
    for i in s:
        if i in a_to_z:
            if a_to_z.index(i)+n < 25:
                answer += a_to_z[a_to_z.index(i)+n]
            else:
                answer += a_to_z[a_to_z.index(i)+n-26]
        elif i.lower() in a_to_z :
            if a_to_z.index(i.lower())+n < 25:
                answer += (a_to_z[a_to_z.index(i.lower())+n]).upper()
            else:
                answer += (a_to_z[a_to_z.index(i.lower())+n-26]).upper()
        else:
            answer += i
    return answer