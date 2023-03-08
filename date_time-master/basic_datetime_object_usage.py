import datetime

# Date object
today = datetime.date.today()
new_year = datetime.date(2017, 1, 1)

# Time object
noon = datetime.time(12, 0, 0)

# Current datetime
now= datetime.datetime.now()

# Datetime object
millenium_turn = datetime.datetime(2000, 1, 1, 0, 0, 0)

# subtraction of noon from today
print('time since the millenium at midnight: ',
      datetime.datetime(today.year, today.month, today.day)- millenium_turn)
#or
print('Time since the millenium at noon: ', 
      datetime.datetime.combine(today, noon) - millenium_turn)