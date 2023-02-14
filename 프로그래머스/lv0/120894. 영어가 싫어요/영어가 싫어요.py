def solution(numbers):
    zero_to_nine = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for k,v in enumerate(zero_to_nine):
        numbers = numbers.replace(v,str(k))
    return int(numbers)