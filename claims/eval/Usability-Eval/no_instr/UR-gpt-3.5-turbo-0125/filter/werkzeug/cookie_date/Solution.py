
from werkzeug.http import http_date

# Current time
current_time = time.time()

# Format the current time to RFC1123 date format
formatted_time = http_date(current_time)

print("Formatted time in RFC1123 format:", formatted_time)
