import datetime
import pytz



async def live() -> bool:
    chile_tz = pytz.timezone('Chile/Continental')
    now = datetime.datetime.now(tz=chile_tz)
    start_time = now.replace(hour=9, minute=0, second=0, microsecond=0)
    end_time = now.replace(hour=17, minute=0, second=0, microsecond=0)
    
    if start_time <= now <= end_time:
        return True
    else:
        return False
