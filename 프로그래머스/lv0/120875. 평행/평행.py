def solution(dots):
    # dot
    ax, ay, bx, by, cx, cy, dx, dy = sum(dots, [])
    
    # line
    ab = (ax-bx)/(ay-by)
    cd = (cx-dx)/(cy-dy)
    
    ac = (ax-cx)/(ay-cy)
    bd = (bx-dx)/(by-dy)
    
    ad = (ax-dx)/(ay-dy)
    bc = (bx-cx)/(by-cy)
    
    return 1 if ab == cd or ac == bd or ad == bc else 0