from datetime import datetime
from email.utils import formatdate

# Get the current date and time
now = datetime.now()

# Format the time to match the RFC1123 date format
rfc1123_date = formatdate(now.timestamp())

print(rfc1123_date)
