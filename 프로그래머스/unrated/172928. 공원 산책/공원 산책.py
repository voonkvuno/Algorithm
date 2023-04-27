def solution(park, routes):
    s = []
    for i, p in enumerate(park):
        if p.find('S') > -1:
            s.append(i)
            s.append(p.find('S'))
            
    for route in routes:
        move = int(route[-1])
        if route[0] == 'N' and 0 <= s[0]-move < len(park):
            if not 'X' in [park[s[0]-i][s[1]] for i in range(1, move+1)]:
                s[0] -= move
        elif route[0] == 'S' and 0 <= s[0]+move < len(park):
            if not 'X' in [park[s[0]+i][s[1]] for i in range(1, move+1)]:
                s[0] += move
        elif route[0] == 'W' and 0 <= s[1]-move < len(park[0]):
            if not 'X' in [park[s[0]][s[1]-i] for i in range(1, move+1)]:
                s[1] -= move
        elif route[0] == 'E' and 0 <= s[1]+move < len(park[0]):
            if not 'X' in [park[s[0]][s[1]+i] for i in range(1, move+1)]:
                s[1] += move
    return s