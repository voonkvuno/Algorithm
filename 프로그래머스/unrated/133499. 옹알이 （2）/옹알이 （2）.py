def solution(babbling):
    count = 0
    babble = [ "aya", "ye", "woo", "ma" ]
    for utter in babbling:
        for text in babble:
            if text * 2 not in utter:
                utter = utter.replace(text, ' ')
        if utter.strip() == '':
            count += 1
    return count