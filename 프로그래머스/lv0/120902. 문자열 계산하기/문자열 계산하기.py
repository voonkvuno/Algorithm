def solution(my_string):
    answer = int(my_string.split()[0])
    for idx, val in enumerate(my_string.split()):
        if val == '+':
            answer += int(my_string.split()[idx+1])
        elif val =='-':
            answer -= int(my_string.split()[idx+1])
    return answer