def solution(a, b):
    days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    week = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    return week[divmod(sum(days[:a]) + b, 7)[1] - 1]