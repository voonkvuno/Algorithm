def solution(answers):
    count1, count2, count3 = 0, 0, 0
    submit1 = [1,2,3,4,5] * 2000
    submit2 = [2,1,2,3,2,4,2,5] * 1250
    submit3 = [3,3,1,1,2,2,4,4,5,5] * 1000
    
    for sub1, sub2, sub3, ans in zip(submit1, submit2, submit3, answers):
        if sub1 == ans:
            count1 += 1
        if sub2 == ans:
            count2 += 1
        if sub3 == ans:
            count3 += 1
            
    count_list = [count1, count2, count3]        
    max_count = max([count1, count2, count3])   

    return [i+1 for i, v in enumerate(count_list) if v == max_count]