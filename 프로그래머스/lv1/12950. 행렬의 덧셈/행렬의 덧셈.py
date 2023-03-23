def solution(arr1, arr2):
    answer = []
    for a, b in zip(arr1, arr2):
        answer.append([a[i] + b[i] for i in range(len(a))])
    return answer