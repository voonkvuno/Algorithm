def solution(d, budget):
    d.sort()
    i = 0
    price = d[i]
    while price <= budget:
        if i < len(d) - 1:
            i += 1
            price += d[i]
        else:
            i += 1
            break
    return i