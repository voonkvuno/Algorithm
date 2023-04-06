def check(s):
    while True:
        if "()" in s:
            s=s.replace("()","")
        elif "{}" in s:
            s=s.replace("{}","")
        elif "[]" in s:
            s=s.replace("[]","")
        else:
            return True if not s else False

def solution(s):
    answer = 0
    for i, _ in enumerate(s):
        if check(s[i:] + s[:i]):
            answer += 1
    return answer