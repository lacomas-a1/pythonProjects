#parsing a string into a timezone aware datetime object
#UTC offset in the form +HHMM or -HHMM (empty string if the object is naive).
import datetime
dt=datetime.datetime.strptime ("2016-04-15T08:27:18-0500", "%Y-%m-%dT%H:%M:%S%z")
print(dt)
"""
import dateutil.parser
dt = dateutil.parser.parse("2016-04-15T08:27:18-0500")
"""
