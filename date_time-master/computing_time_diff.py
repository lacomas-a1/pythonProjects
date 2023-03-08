from datetime import datetime, timedelta
now = datetime.now()
then = datetime(2016, 5, 23)
delta=now-then
print(delta.days)
print(delta.seconds)

# To get n day's after and n day's before date we could use:
# n day's after date:

def get_n_days_after_date(date_format="%d %B %Y", add_days=120):
    date_n_days_after =datetime.datetime.now() + timedelta(days=add_days)
    return date_n_days_after.strftime(date_format)

# n day's before date:
def get_n_days_before_date(self, date_format="%d %B %Y", days_before=120):
    date_n_days_ago = datetime.datetime.now() - timedelta(days=days_before)
    return date_n_days_ago.strftime(date_format)