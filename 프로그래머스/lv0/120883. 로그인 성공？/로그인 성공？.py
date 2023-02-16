def solution(id_pw, db):
    answer = []
    for id, pw in db:
        if id_pw[0] == id and id_pw[1] == pw:
            answer.append('login')
        elif id_pw[0] == id and id_pw[1] != pw:
            answer.append('wrong pw')
        elif id_pw[0] != id:
            answer.append('fail')
            
    if 'login' in answer:
        return 'login'
    else:
        if 'wrong pw' in answer:
            return 'wrong pw'
        else:
            return 'fail'