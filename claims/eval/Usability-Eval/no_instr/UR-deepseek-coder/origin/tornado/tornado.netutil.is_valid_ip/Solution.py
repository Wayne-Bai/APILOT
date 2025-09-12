import re
from tornado import gen

def is_valid_ip(ip):
    # Regular expression pattern for validating an IP address
    pattern = re.compile(r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$')
    return bool(pattern.match(ip))

@gen.coroutine
def check_ip(ip):
    result = is_valid_ip(ip)
    return result
