# Import the necessary module from werkzeug library
from werkzeug.http import http_date

# Function to format the time to match the RFC1123 date format
def format_time_to_rfc1123(dt):
    """
    Formats the given date and time to match the RFC1123 date format.

    Args:
        dt (datetime): The date and time to format.

    Returns:
        str: The formatted date and time string.
    """
    return http_date(dt)

# Example usage
from datetime import datetime
dt = datetime.now()
formatted_time = format_time_to_rfc1123(dt)
print(formatted_time)
