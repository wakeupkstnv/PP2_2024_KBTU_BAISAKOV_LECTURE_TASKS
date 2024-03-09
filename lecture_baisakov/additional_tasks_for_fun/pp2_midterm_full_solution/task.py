import datetime
import re

date_now = datetime.datetime.now()

def isBlackList(date: str) -> str:
    global date_now
    
    collect_data_from_user = list(date.split('.'))
    
    if len(collect_data_from_user) > 3: return 'not correct data from user'
    if len(collect_data_from_user[0]) != 4 or len(collect_data_from_user[1]) > 2 or len(collect_data_from_user[2]) > 2: return 'not correct data from user' 
    
    upd_data_from_user = datetime.datetime(year=int(collect_data_from_user[0].strip()), month=int(collect_data_from_user[1].strip()), day=int(collect_data_from_user[2].strip()))
    
    delta_in_time = upd_data_from_user - date_now
    need_time = datetime.datetime(year=date_now.year, month=date_now.month, day=date_now.day + 3)
    
    if delta_in_time.days <= 3 and delta_in_time.days >= 0: return date
    if delta_in_time.days > 3 or delta_in_time.days < 0: return 'Black List' 
    
    
with open('some.txt') as file:
    text = file.read()
    pattern = r'(?P<name>.+) (?P<date>[2-9][0-9][0-9][0-9].[0-9][0-9]*.[0-9][0-9]*\S)'
    
    with open('answer.txt', 'w') as file:    
        for i in re.finditer(pattern, text):
              file.write(f'{i.group('name')}: {isBlackList(i.group('date'))}\n')
            