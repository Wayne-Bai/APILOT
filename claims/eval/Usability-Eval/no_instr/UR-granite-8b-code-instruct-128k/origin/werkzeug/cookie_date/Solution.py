from werkzeug.http import http_date

def format_time_rfc1123(timestamp):
    return http_date(timestamp)
