import tornado

def is_valid_ip(ip):
    """
    Returns True if the given string is a well-formed IP address.
    """
    ip_parts = ip.split('.')
    if len(ip_parts) != 4:
        return False
    for part in ip_parts:
        try:
            if not 0 <= int(part) <= 255:
                return False
        except ValueError:
            return False
    return True
