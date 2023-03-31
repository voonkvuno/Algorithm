from collections import deque
def solution(people, limit):
    answer = 0
    people = deque(sorted(people))
    while len(people) > 1:
        if people[0] + people[-1] <= limit:
            answer += 1
            people.popleft()
            people.pop()
        else:
            answer += 1
            people.pop()
    if people:
        answer += 1
    return answer