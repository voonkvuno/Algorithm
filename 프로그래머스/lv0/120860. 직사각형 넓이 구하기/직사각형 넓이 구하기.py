def solution(dots):
    x = [ i[0] for i in dots ]
    y = [ i[1] for i in dots ]
    
    if ( max(x) > 0 and min(x) > 0 ) or ( max(x) < 0 and min(x) < 0 ):
        width = abs(max(x) - min(x))
    else:
        width = abs(max(x)) + abs(min(x))
    
    if ( max(y) > 0 and min(y) > 0 ) or ( max(y) < 0 and min(y) < 0 ):
        height = abs(max(y) - min(y))
    else:
        height = abs(max(y)) + abs(min(y))
    
    return width * height