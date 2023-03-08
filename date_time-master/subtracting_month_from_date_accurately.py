#using calendar module
import calendar
from datetime import date

def monthdelta(date, delta):
    m, y =(date.month+delta) % 12, date.year + ((date.month) +delta-1)//12
    if not m: m=12
    d=min(date.day, calendar.monthrange(y, m)[1])
    return date.replace(day=d, month=m, year=y)
next_month = monthdelta(date.today(), 1)
print(next_month)

#or
import datetime
import dateutil.relativedelta

d=datetime.datetime.strptime("2013-03-31", "%Y-%m-%d")
d2= d - dateutil.relativedelta.relativedelta(months=1)