from werkzeug.http import http_date
import datetime

def dump_http_header():
    # Get the current date and time
    now = datetime.datetime.now()

    # Convert the datetime object to an HTTP date string
    http_date_string = http_date(now)

    # Create and print the HTTP header with the date
    print(f"HTTP/1.1 200 OK")
    print(f"Date: {http_date_string}")
    print(f"Content-Type: text/plain")
    print(f"Content-Length: 0")
    print(f"Connection: keep-alive")

# Call the function to test
dump_http_header()
