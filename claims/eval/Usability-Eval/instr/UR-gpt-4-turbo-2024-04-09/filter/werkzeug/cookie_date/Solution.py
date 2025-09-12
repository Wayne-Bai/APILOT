from werkzeug.http import http_date
from datetime import datetime

def format_time_rfc1123(current_time):
    formatted_time = http_date(current_time)
    return formatted_time

# Example usage
current_time = datetime.now()
formatted_time = format_time_rfc1123(current_time)
print("Formatted Time (RFC1123):", formatted_time)
