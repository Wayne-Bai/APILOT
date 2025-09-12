from werkzeug.http import http_date
import datetime

# Function to format the current time in RFC1123 format
def get_rfc1123_time():
    current_time = datetime.datetime.utcnow()
    return http_date(current_time)

# Example usage
if __name__ == "__main__":
    print(get_rfc1123_time())
