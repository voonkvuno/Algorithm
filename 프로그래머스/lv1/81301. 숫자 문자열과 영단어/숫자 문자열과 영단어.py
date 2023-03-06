def solution(s):
    number = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
    for i in number:
        if i in s:
            s = s.replace(i,str(number.index(i)))
    return int(s)