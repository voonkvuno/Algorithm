def solution(numbers, hand):
    answer = ''
    L = ['*']
    R = ['#']
    keypad = {'1':[0,0],'2':[0,1],'3':[0,2],
              '4':[1,0],'5':[1,1],'6':[1,2],
              '7':[2,0],'8':[2,1],'9':[2,2],
              '*':[3,0],'0':[3,1],'#':[3,2]}
    for number in numbers:
        if number in [1,4,7]:
            answer += 'L'
            L.append(str(number))
        elif number in [3,6,9]:
            answer += 'R'
            R.append(str(number))
        else:
            l, r = 0, 0
            for x, y, z in zip(keypad[str(number)], keypad[L[-1]], keypad[R[-1]]):
                l += abs(x-y)
                r += abs(x-z)
            if l == r:
                if hand == 'left':
                    answer += 'L'
                    L.append(str(number))
                elif hand == 'right':
                    answer += 'R'
                    R.append(str(number))
            elif l < r:
                answer += 'L'
                L.append(str(number))
            elif l > r:
                answer += 'R'
                R.append(str(number))
    return answer