from datetime import datetime
datetime_string = 'Oct 1 2016, 00:00:00'
datetime_string_format = '%b %d %Y, %H: %M: %S'
datetime.strptime(datetime_string, datetime_string_format)
print(datetime_string)