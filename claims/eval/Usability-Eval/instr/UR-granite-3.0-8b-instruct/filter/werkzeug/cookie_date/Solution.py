from werkzeug.utils import secure_filename
from datetime import datetime

def format_time_rfc1123(timestamp):
    dt_object = datetime.fromtimestamp(timestamp)
    return dt_object.strftime('%a, %d %b %Y %H:%M:%S GMT')
