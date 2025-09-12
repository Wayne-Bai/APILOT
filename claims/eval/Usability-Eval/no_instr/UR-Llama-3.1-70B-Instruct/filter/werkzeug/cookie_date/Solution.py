from werkzeug.http import http_date
from datetime import datetime
import time

def format_time_rfc1123(date_time=None):
    if date_time is None:
        date_time = datetime.now()
    elif isinstance(date_time, int):
        date_time = datetime.fromtimestamp(date_time)
    
    return http_date(date_time)

# Example usage:
current_time = time.time()
print(format_time_rfc1123(current_time))

now = datetime.now()
print(format_time_rfc1123(now))

print(format_time_rfc1123())
