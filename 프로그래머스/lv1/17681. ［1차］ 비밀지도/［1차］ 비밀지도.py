def solution(n, arr1, arr2):
    answer = []
    arr1 = [ '0'*(n - len(bin(i)[2:])) + bin(i)[2:] for i in arr1]
    arr2 = [ '0'*(n - len(bin(i)[2:])) + bin(i)[2:] for i in arr2]
    for a1, a2 in zip(arr1, arr2):
        row = ''
        for a, b in zip(a1, a2):
            if int(a+b,2) > 0:
                row += '#'
            else:
                row += ' '
        answer.append(row)
    return answer