def solution(my_string):
    answer = ""
    for mystring in my_string:
        if mystring.isupper():
            answer += mystring.lower()
        elif mystring.islower():
            answer += mystring.upper()
    return answer