from cryptography.hazmat.backends import default_backend
from cryptography.x509.der import Time
from datetime import datetime

def naive_datetime_to_iso(date_time: Time) -> str:
    naive_datetime = datetime.fromtimestamp(date_time.year + 1900, date_time.month, date_time.day)
    iso_format_datetime = date_time.strftime('%Y-%m-%d %H:%M:%S')
    return iso_format_datetime

backend = default_backend()
date_time = Time(0, 231733520, 0, 0, default_backend())
naive_datetime_to_iso(date_time)
