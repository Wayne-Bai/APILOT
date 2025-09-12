from datetime import datetime
import werkzeug.datastructures

def format_time(time):
    return datetime.strftime(time, werkzeug.datastructures.RFC1123)

# Example usage
print(format_time(datetime.now()))  # Output: Wed, 29 Apr 2020 17:54:16 GMT
