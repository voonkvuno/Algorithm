def solution(brown, yellow):
    yellow_list = [ [yellow//i, i] 
                   for i in range(1, int(yellow**0.5)+1) if yellow % i == 0 ]

    for w, h in yellow_list:
        if brown == (w+2) * (h+2) - yellow:
            return [w+2, h+2]