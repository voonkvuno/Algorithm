def solution(s):
    bin_cnt, zero_cnt = 0, 0
    while s != '1':
        bin_cnt += 1
        zero_cnt += len(s) - len(s.replace('0',''))
        s = bin(len(s.replace('0','')))[2:]
    return [bin_cnt, zero_cnt]