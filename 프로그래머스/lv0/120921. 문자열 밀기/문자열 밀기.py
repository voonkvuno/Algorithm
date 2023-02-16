def solution(A, B):
    for idx, _ in enumerate(A):
        if A == B:
            return idx
        A = A[-1] + A[:-1]
    return -1