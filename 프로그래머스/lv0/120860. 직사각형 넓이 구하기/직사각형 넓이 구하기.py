def solution(dots):
    mx = max([ i[0] for i in dots ])
    nx = min([ i[0] for i in dots ])
    my = max([ i[1] for i in dots ])
    ny = min([ i[1] for i in dots ])
    
    return (mx-nx) * (my-ny)