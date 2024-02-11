import datetime

newton_birthtime = datetime.datetime(1643, 1, 4, 15, 55, 4, 15432)
time_now = datetime.datetime.now()

time_difference = time_now - newton_birthtime
dif_seconds = time_difference.total_seconds()

print(dif_seconds)
