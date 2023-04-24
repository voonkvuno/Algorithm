from datetime import datetime
from dateutil.relativedelta import relativedelta
def solution(today, terms, privacies):
    answer = []
    now = datetime.strptime(today,'%Y.%m.%d')
    terms_dict = {t.split(' ')[0]:t.split(' ')[1] for t in terms}
    for i,p in enumerate(privacies):
        start_date = datetime.strptime(p.split(' ')[0], '%Y.%m.%d')
        end_date = start_date + relativedelta(months=int(terms_dict[p.split(' ')[1]]))
        if end_date <= now:
            answer.append(i+1)
        
    return answer