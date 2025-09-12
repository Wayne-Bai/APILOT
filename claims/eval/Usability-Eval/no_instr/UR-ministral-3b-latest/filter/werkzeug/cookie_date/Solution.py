from werkzeug import security
import datetime

def format_time_to_rfc1123(time_str):
    time_format = "%a, %d %b %Y %H:%M:%S GMT"
    formatted_time = datetime.datetime.strptime(time_str, time_format).astimezone(datetime.timezone.utc)
    return formatted_time.strftime("%a, %d %b %Y %H:%M:%S GMT")

# Example usage
formatted_time = format_time_to_rfc1123("Wed, 21 Oct 2020 07:28:15 GMT")
print(formatted_time)  # Output: Thu, 21 Oct 2020 07:28:15 GMT
