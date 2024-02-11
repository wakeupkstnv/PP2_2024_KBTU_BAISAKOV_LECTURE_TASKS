import datetime

time_now = datetime.datetime.now()
minus_for_year, minus_for_month, minus_for_day = 0, 0, 5

if time_now.day < 5:
    minus_for_month = 1
    minus_for_day = -26 
if time_now.month == 1 and minus_for_month == 1:
    minus_for_year = 1
    minus_for_month = 11 - time_now.month
 
print(datetime.datetime(
    time_now.year - minus_for_year, time_now.month - minus_for_month, time_now.day - minus_for_day, 
    time_now.hour, time_now.minute, time_now.second)
)
    
