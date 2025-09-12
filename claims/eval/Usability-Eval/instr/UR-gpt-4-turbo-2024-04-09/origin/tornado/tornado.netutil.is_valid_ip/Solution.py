import ipaddress

def is_valid_ip(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False

# Example Usage
ip_test = "192.168.1.1"
print(is_valid_ip(ip_test))  # Output: True

ip_test = "192.168.1.300"
print(is_valid_ip(ip_test))  # Output: False
