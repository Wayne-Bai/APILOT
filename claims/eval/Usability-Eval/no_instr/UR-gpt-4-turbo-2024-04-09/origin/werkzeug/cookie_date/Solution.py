from werkzeug.http import http_date
from datetime import datetime

def format_rfc1123_date():
    now = datetime.now()
    formatted_date = http_date(now)
    return formatted_date

# Example usage
print(format_rfc1123_date())
