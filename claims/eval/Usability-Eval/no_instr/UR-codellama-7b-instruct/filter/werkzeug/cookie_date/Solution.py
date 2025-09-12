
from datetime import datetime
from werkzeug.http import generate_timestamp

# Create a new timestamp object
now = datetime.utcnow()

# Format the timestamp as an RFC1123 string
rfc1123_str = now.strftime('%a, %d %b %Y %H:%M:%S GMT')

print(rfc1123_str)
