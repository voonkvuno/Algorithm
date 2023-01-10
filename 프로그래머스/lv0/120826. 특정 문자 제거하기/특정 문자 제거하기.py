def solution(my_string, letter):
    mystring = list(my_string)
    while letter in mystring:
        mystring.remove(letter)
    return ''.join(mystring)