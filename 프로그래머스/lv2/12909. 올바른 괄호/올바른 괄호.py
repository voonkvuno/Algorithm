def solution(s):
    stack = []
    for i in s:
        if i == '(':  
            stack.append(i) 
        else: 
            if stack: 
                stack.pop()
            else:
                return False
    
    return True if not stack else False