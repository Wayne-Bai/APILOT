from werkzeug import times
from datetime import datetime

# Get the current time
current_time = datetime.utcnow()

# Format the current time to RFC1123 format
rfc1123_time = times.format(current_time)

print(rfc1123_time)
