from datetime import datetime, timedelta
from dateutil import tz
JST = tz.tzoffset('JST', 9*3600) # 3600 seconds per hour
dt = datetime(2015, 1, 1, 12, 0, tzinfo=JST)
print(dt)
print(dt.tzname)