
import re

def is_ip_address(ip_address):
    pattern = r"^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])(\.(?!$)|$)){4}$"
    return bool(re.match(pattern, ip_address))
