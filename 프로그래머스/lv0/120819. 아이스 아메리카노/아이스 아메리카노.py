def solution(money):
    coffee, cash = divmod(money,5500)
    return [coffee, cash]