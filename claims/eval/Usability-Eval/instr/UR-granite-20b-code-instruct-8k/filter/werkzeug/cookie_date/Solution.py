from werkzeug.http import http_date
from datetime import datetime
date_time = datetime.now()
formatted_date = http_date(date_time)
print(formatted_date)
