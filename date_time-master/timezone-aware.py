#Constructing timezone-aware datetimes
#Fixed Offset Time Zones
"""
For time zones that are a fixed offset from UTC, in Python 3.2+, the datetime module provides the timezone class, a
concrete implementation of tzinfo, which takes a timedelta and an (optional) name parameter:

"""
from datetime import datetime, timedelta, timezone
JST =timezone(timedelta(hours=+9))
dt=datetime(2015, 1, 1, 12, 0, 0, tzinfo=JST)
print(dt)
print(dt.tzname())
dt=datetime(2015, 1, 1, 12, 0, 0, tzinfo=timezone(timedelta(hours=9), 'JST'))
print(dt.tzname)