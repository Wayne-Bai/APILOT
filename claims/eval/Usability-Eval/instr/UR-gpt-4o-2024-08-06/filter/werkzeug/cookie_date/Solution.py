from werkzeug.http import http_date
from datetime import datetime

# Get the current time
current_time = datetime.utcnow()

# Format the time to match the RFC1123 date format
formatted_time = http_date(current_time.timestamp())

print(f"RFC1123 formatted date: {formatted_time}")
