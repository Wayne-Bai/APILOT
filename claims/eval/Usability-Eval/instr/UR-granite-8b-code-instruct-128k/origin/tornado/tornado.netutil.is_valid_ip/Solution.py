import tornado

def is_well_formed_ip(ip_str):
    try:
        parts = ip_str.split(".")
        if len(parts) != 4:
            return False
        for part in parts:
            if not part.isdecimal() or not 0 <= int(part) <= 255:
                return False
        return True
    except ValueError:
        return False
