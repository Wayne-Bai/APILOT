
import re
from tornado import gen

@gen.coroutine
def validate_ip(string):
    # Check if string is an IP address using regular expressions
    regex = r"^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$"
    if re.match(regex, string):
        return True
    else:
        return False
