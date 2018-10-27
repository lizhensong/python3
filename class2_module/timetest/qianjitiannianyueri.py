#!usr\bin\python3
#-*-coding:UTF-8-*-
#计算给定日期前几天的日期(30天的)
import calendar
def date(year,month,day,preday):
    if preday<day:
        day-=preday
    else:
        if month>1:
            month-=1
            thismonthdays=calendar.monthrange(year,month)[1]
            day=thismonthdays-(preday-day)
        else:
            year-=1
            month=12
            day=31-(preday-day)
    return year,month,day