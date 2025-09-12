from datetime import datetime
from werkzeug import http

# Function to format time to RFC1123 date format
def rfc1123_format(date_time):
    format_string = "%a, %d %b %Y %H:%M:%S %z"
    return date_time.strftime(format_string)

# Example usage
current_time = datetime.utcnow()
formatted_time = rfc1123_format(current_time)
print(formatted_time)
