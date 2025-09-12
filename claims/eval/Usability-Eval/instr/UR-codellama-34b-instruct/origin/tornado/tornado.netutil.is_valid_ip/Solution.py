import ipaddress
from tornado import gen

@gen.coroutine
def is_ip_address(addr):
    try:
        ip = ipaddress.IPv4Address(addr)
        return True
    except ValueError:
        return False
