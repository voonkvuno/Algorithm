def solution(rsp):
    result = {2:0, 0:5, 5:2}
    return ''.join(str(result.get(int(i))) for i in rsp)
