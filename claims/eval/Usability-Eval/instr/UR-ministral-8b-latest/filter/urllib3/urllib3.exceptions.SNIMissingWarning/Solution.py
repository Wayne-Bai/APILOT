import urllib3

def check_sni_availability(hostname):
    http = urllib3.PoolManager()
    try:
        # Attempt to create a secure connection using SNI
        # Note: The hostname parameter does not necessarily need to be valid, since we just want to check for SNI availability.
        conn = http.urlopen('https://{}'.format(hostname), timeout=10)
    except urllib3.exceptions.SSLError:
        print(f"Error: SNI is not available for the given hostname: {hostname}")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
    return True

# Example usage
hostname = 'example.com'
is_sni_available = check_sni_availability(hostname)
if is_sni_available:
    print(f"SNI is available for the given hostname: {hostname}")
else:
    print(f"SNI is not available for the given hostname: {hostname}")
