import socket

def is_valid_ip(ip_str):
    try:
        # Try to convert the string to a valid IP address
        socket.inet_aton(ip_str)
        # Conversion was successful, return True
        return True
    except socket.error:
        # Conversion failed, it's not a valid IP address
        return False

# Example usage
if __name__ == "__main__":
    ip_address = "192.168.1.1"
    print(f"{ip_address} is valid: {is_valid_ip(ip_address)}")

    invalid_ip = "999.999.999.999"
    print(f"{invalid_ip} is valid: {is_valid_ip(invalid_ip)}")
