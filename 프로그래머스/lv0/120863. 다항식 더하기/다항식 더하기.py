def solution(polynomial):
    x, n = [], []
    
    for i in polynomial.split(' + '):
        if 'x' in i:
            x.append(int(i.split('x')[0]) if not i.split('x')[0] == '' else 1)
        else:
            n.append(int(i) if not i == '' else 1)
            
    if sum(x) > 0 and sum(n) > 0:
        if sum(x) == 1:
            return 'x + ' + str(sum(n))
        return str(sum(x)) + 'x + ' + str(sum(n))
    elif sum(x) > 0 and not sum(n) > 0:
        if sum(x) == 1:
            return 'x'
        return str(sum(x)) + 'x'
    elif not sum(x) > 0 and sum(n) > 0:
        return str(sum(n))
    else:
        return '0'