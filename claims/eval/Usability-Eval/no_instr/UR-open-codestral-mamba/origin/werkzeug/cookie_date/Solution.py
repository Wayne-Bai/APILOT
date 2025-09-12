from werkzeug.http import http_date
from datetime import datetime

# Get the current time
now = datetime.now()

# Format the time to match the RFC1123 date format
formatted_time = http_date(now.timestamp())

print(formatted_time)
