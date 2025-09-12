
import re

def is_valid_ip(ip):
    pattern = r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
    if re.match(pattern, ip):
        return True
    else:
        return False

# Example usage
ip_address = '192.168.1.1'
print(is_valid_ip(ip_address))
