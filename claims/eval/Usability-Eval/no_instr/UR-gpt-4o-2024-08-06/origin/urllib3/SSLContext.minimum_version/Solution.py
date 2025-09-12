import urllib3
from urllib3.util.ssl_ import create_urllib3_context, TLSVersion

def get_minimum_tls_version():
    # Create a context similar to how urllib3 would create one
    context = create_urllib3_context()

    # Set the lowest supported TLS version
    # TLSVersion.MINIMUM_SUPPORTED is the concept of setting it to a lower limit
    context.minimum_version = TLSVersion.TLSv1_2

    # Return the minimum version for demonstration which is set
    return context.minimum_version

if __name__ == "__main__":
    min_version = get_minimum_tls_version()
    print(f"Minimum supported TLS version is: {min_version}")
