def solution(hp):
    five, three, one = 0, 0, 0
    five, remainder = divmod(hp,5)
    if remainder:
        three, remainder = divmod(remainder,3)
    if remainder:
        one, remainder = divmod(remainder, 1)
    print(five, three, one)
    return five + three + one