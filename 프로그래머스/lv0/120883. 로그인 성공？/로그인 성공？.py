def solution(id_pw, db):
    for id, pw in db:
        if id_pw[0] == id and id_pw[1] == pw:
            return 'login'
        elif id_pw[0] == id and id_pw[1] != pw:
            return 'wrong pw'
    return 'fail'