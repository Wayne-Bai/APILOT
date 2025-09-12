from werkzeug.http import http_date
from datetime import datetime

def format_rfc1123_time(dt: datetime) -> str:
    return http_date(dt)

# Example usage:
current_time = datetime.utcnow()
formatted_time = format_rfc1123_time(current_time)
print(formatted_time)
