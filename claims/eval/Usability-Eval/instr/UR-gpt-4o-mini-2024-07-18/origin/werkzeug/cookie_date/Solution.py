from werkzeug.http import http_date
from datetime import datetime

def format_time_to_rfc1123(dt):
    return http_date(dt.timestamp())

# Example usage:
current_time = datetime.utcnow()
formatted_time = format_time_to_rfc1123(current_time)
print(formatted_time)
