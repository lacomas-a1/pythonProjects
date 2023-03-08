from datetime import datetime
from deteutil import tz
local = tz.gettz()
PT= tz.gettz('US/Pacific')

dt_l = datetime(2015, 1, 1, 12, tzinfo=local)
dt_pst=datetime(2015, 1, 1,12, tzinfo=PT)
dt_pdt=datetime(2015, 7, 1, 12, tzinfo=PT)
print(dt_l)
print(dt_pst)
print(dt_pdt)


