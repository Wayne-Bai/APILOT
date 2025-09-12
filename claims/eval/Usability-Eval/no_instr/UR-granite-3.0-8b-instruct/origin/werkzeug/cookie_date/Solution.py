from werkzeug.utils import secure_filename
from datetime import datetime

def format_time(time_str):
    # Convert the input time string to datetime object
    dt = datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S")

    # Format the datetime object to RFC1123 date format
    rfc1123_format = dt.strftime("%a, %d %b %Y %H:%M:%S %Z")

    return rfc1123_format
