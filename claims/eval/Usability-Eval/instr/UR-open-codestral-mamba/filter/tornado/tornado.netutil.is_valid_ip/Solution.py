import tornado

def is_valid_ip(ip_address):
    try:
        tornado.netutil.is_valid_ip(ip_address)
        return True
    except ValueError:
        return False
