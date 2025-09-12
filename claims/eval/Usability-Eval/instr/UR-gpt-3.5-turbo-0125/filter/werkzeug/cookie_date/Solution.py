
from datetime import datetime

def format_time_to_RFC1123(date_time):
    date_string = date_time.strftime('%a, %d %b %Y %H:%M:%S GMT')
    return date_string

# Usage example
current_time = datetime.utcnow()
formatted_time = format_time_to_RFC1123(current_time)
print(formatted_time)
