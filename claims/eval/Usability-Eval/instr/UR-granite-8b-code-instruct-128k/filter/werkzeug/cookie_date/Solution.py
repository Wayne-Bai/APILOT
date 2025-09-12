from werkzeug.http import http_date
import time
# Example usage
timestamp = time.time()
formatted_time = http_date(timestamp)
print(formatted_time)
