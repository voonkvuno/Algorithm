def solution(num_list):
    even = [ 1 for num in num_list if divmod(num,2)[1] == 0 ]
    odd = [ 1 for num in num_list if divmod(num,2)[1] != 0 ]
    return [sum(even), sum(odd)]