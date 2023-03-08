# The simplest way to do this is to use the is None test.
if aDate is None:
    aDate =datetime.date.today()
    
if not aDate:
    aDate=datetime.date.today()