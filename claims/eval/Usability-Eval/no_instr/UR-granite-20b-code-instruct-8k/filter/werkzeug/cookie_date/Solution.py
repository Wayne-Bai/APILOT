from werkzeug.http import http_date

def format_time_rfc1123(time):
    return http_date(time)
