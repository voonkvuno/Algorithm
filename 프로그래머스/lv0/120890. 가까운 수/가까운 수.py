def solution(array, n):
    answer = 0
    array.append(n)
    array.sort()
    idx = array.index(n)
    if idx == 0:
        answer = array[idx+1]
    elif 0 < idx < len(array)-1:
        if array[idx] - array[idx-1] > array[idx+1] - array[idx]:
            answer = array[idx+1]
        elif array[idx] - array[idx-1] < array[idx+1] - array[idx]:
            answer = array[idx-1]
        else:
            answer = array[idx-1]
    else:
        answer = array[idx-1]
    return answer