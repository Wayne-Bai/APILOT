
import hmac
import hashlib
from tornado.escape import utf8, native_str, _unicode
from tornado.util import unicode_type

def decode_signed_value(secret, name, value, max_age_days=31):
    if not value:
        return None
    parts = value.split("|")
    if len(parts) != 3:
        return None
    timestamp = utf8(parts[0])
    if timestamp.startswith(b't'):
        timestamp = timestamp[1:]
    try:
        timestamp = float(timestamp)
    except (TypeError, ValueError):
        return None
    if timestamp < time.time() - max_age_days * 86400:
        return None
    new_signature = create_signed_value(secret, name, parts[1], timestamp)
    if new_signature == utf8(parts[2]):
        return native_str(parts[1])
    return None
