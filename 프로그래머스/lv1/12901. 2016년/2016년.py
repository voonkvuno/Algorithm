def solution(a, b):
    days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    week = ['SUN','MON','TUE','WED','THU','FRI','SAT']
    january1 = 5 # FRI
    return week[divmod(january1 + sum(days[:a]) + b, 7)[1] - 1]