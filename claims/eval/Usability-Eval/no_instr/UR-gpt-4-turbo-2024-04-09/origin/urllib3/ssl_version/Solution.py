import urllib3

# Create a function to verify SSL/TLS versions supported by a server
def check_ssl_versions(url, timeout=3):
    # List of SSL/TLS protocols to test
    protocols = [
        'TLSv1',
        'TLSv1_1',
        'TLSv1_2',
        'TLSv1_3'
    ]

    supported_versions = []

    # Iterate over each protocol and check if the server supports it
    for protocol in protocols:
        # Create a PoolManager with specified SSL version
        try:
            http = urllib3.PoolManager(
                timeout=timeout,
                ssl_version=protocol
            )
            response = http.request('GET', url)
            if response.status == 200:
                supported_versions.append(protocol)
        except urllib3.exceptions.SSLError:
            print(f"{protocol} is not supported.")
        except Exception as e:
            print(f"Error checking {protocol}: {str(e)}")

    return supported_versions

# Example usage
url = "https://www.example.com"
supported_protocols = check_ssl_versions(url)
print(f"Supported SSL/TLS versions for {url}: {supported_protocols}")
