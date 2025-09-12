from werkzeug.utils import secure_filename
import datetime

def format_time_to_rfc1123(time):
    dt = datetime.datetime.fromtimestamp(time)
    return dt.strftime("%a, %d %b %Y %H:%M:%S %z")

# Example usage:
time = 1633027200  # This is a Unix timestamp
formatted_time = format_time_to_rfc1123(time)
print(formatted_time)
