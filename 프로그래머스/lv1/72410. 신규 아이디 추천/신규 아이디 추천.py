def solution(new_id):
    able = 'abcdefghijklmnopqrstuvwxyz0123456789-_.'
    # step1, step2
    new_id  = ''.join([s for s in new_id.lower() if s in able])
    # step3
    while '..' in new_id:
        new_id = new_id.replace('..','.')
    # step4
    new_id = new_id.strip('.')
    # step5
    if not new_id:
        new_id += 'a'
    # step6
    if len(new_id) >= 16:
        new_id = (new_id[0:15]).rstrip('.')
    # step7
    while len(new_id) <= 2:
        new_id += new_id[-1]
    return new_id