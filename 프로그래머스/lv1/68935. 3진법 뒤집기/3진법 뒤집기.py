def solution(n):
    three = ''
    
    while n!=0:
        three += str(n%3) 
        n = n//3
        
    return int(three,3)