from werkzeug.utils import secure_filename
from datetime import datetime

def format_time_for_rfc1123(time):
    # Get the current time
    current_time = datetime.utcnow()

    # Format the time to RFC1123 format
    rfc1123_time = current_time.strftime("%a, %d %b %Y %H:%M:%S %z")

    return rfc1123_time
