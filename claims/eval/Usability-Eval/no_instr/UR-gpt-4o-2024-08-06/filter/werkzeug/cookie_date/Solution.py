from werkzeug.http import http_date
import datetime

# Get the current time
current_time = datetime.datetime.now()

# Format the time using Werkzeug's utility to match RFC 1123 format
rfc1123_time = http_date(current_time.timestamp())

# Output the formatted time
print(rfc1123_time)
