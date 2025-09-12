from datetime import datetime
import pytz
from werkzeug.routing import URLConverter

# Function to format time as perRFC1123 date format
def format_time(date):
    dt = date.astimezone(pytz.utc).strftime('%a, %d %b %Y %H:%M:%S %z')

    # Removing the : from the timezone offset (only for UTC)
    if date.tzinfo.utcoffset(None) == timedelta(0):
        dt = dt[:-3]

    return dt

# Current date and time
date = datetime.now(pytz.utc)

# Format the date as per the RFC1123 date format
formatted_time = format_time(date)

print(formatted_time)
