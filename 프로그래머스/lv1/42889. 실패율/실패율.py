def solution(N, stages):
    fail = dict()
     # 실패율 = 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수
    for n in range(1,N+1):
        success = 0
        for stage in stages:
            if stage >= n:
                success += 1
        if success == 0:
            fail[n] = 0
        else:
            fail[n] = stages.count(n) / success
            
    return [i for i, _ in sorted(fail.items(), key=lambda x: x[1], reverse=True)]