def solution(my_string, num1, num2):
    mystring = list(my_string)
    mystring[num1], mystring[num2] = mystring[num2], mystring[num1]
    return ''.join(mystring)