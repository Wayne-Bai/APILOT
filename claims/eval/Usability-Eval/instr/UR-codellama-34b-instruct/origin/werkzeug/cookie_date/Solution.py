import werkzeug.contrib.routing
from datetime import datetime

def format_time(timestamp):
    # Convert timestamp to datetime object
    dt = datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%SZ')
    
    # Use werkzeug.contrib.routing.HTTPDate to convert datetime object to RFC1123 format
    rfc_date = werkzeug.contrib.routing.HTTPDate(dt)
    
    return rfc_date
