def solution(quiz):
    answer = []
    x, y, z = 0, 0, 0
    for q in quiz:
        if ' + ' in q:
            x = int((q.split(' = ')[0]).split(' + ')[0])
            y = int((q.split(' = ')[0]).split(' + ')[1])
            z = int(q.split(' = ')[1])
        elif ' - ' in q:
            print('')
            x = int((q.split(' = ')[0]).split(' - ')[0])
            y = -int((q.split(' = ')[0]).split(' - ')[1])
            z = int(q.split(' = ')[1])
        if x + y == z:
            answer.append('O')
        else:
            answer.append('X')
    return answer