from datetime import datetime, timedelta
import pytz
PT= pytz.timezone('US/Pacific')
dt_pst =PT.localize(datetime(2015, 1, 1, 12))
dt_pdt = PT.localize(datetime(2015, 11, 1, 0, 30))
print(dt_pst)
print(dt_pdt)

dt_new =dt_pdt + timedelta(hours=3)
print(dt_new)

dt_corrected =PT.normalize(dt_new)
print(dt_corrected)