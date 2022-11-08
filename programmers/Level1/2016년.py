import datetime

def solution(a, b):
    dict_day = "MON TUE WED THU FRI SAT SUN".split()
    date = dict_day[datetime.datetime(2016, a, b).weekday()]
    print(date)
    return date

