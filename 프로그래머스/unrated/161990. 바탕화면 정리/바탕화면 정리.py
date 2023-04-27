def solution(wallpaper):
    x = []
    y = []
    for dy, row in enumerate(wallpaper):
        for dx, dot in enumerate(row):
            if dot == "#": 
                x.append(dx)
                y.append(dy)
    return [min(y),min(x),max(y)+1,max(x)+1]