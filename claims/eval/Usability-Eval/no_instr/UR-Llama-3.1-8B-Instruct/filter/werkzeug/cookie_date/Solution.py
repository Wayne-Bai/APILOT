from datetime import datetime
from Werkzeug.utils import ticks_to_time
from Werkzeug.local import LocalProxy

# Create a timezone object
time_zone = LocalProxy(lambda: datetime.utcnow())

def format_rfc1123_time(time):
    """
    Formats the time to match the RFC1123 date format.
    
    :param time: The time to format (either datetime object, Unix timestamp or seconds since epoch)
    :return: The formatted time string in RFC1123 format
    """
    # Convert time to datetime object if it's a timestamp or epoch seconds
    if isinstance(time, (int, float)):
        time = ticks_to_time(time)
    
    return time.strftime('%a, %d %b %Y %H:%M:%S GMT')
