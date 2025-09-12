from werkzeug.http import http_date
import time

# Define a function to format the time in RFC1123 format
def format_time(input_time):
    # Convert the input time to seconds since epoch
    seconds = time.mktime(input_time.timetuple())

    # Format the time in RFC1123 format
    formatted_time = http_date(seconds)

    return formatted_time

# Test the function
test_time = time.strptime('2022-01-01 00:00:00', '%Y-%m-%d %H:%M:%S')
print(format_time(test_time))

