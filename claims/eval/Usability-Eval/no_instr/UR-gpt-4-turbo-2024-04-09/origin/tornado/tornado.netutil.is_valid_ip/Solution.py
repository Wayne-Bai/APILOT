import tornado

def is_well_formed_ip(address):
    """Return True if the given string is a well-formed IP address."""
    try:
        # Version from ipaddress package determines IP validity (both IPv4 and IPv6)
        import ipaddress
        ipaddress.ip_address(address)
        return True
    except ValueError:
        return False
