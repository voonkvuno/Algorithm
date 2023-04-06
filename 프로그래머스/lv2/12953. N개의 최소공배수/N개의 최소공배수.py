def solution(arr):
    n = 0   
    while True:
        n += 1
        result = True
        for num in arr:
            if (max(arr) * n) % num != 0:
                result = False
                break
        if result:
            break
    return max(arr) * n