
import ssl

# Get minimum supported version of the SSL protocol
def get_minimum_supported_version():
    # Minimum TLS version is TLS 1.0
    # You can uncomment or comment the following lines based on your requirement
    # We are assuming TLS 1.3 as a higher minimum version
    tls_min_version = ssl.TLSVersion.TLSv1_3
    #tls_min_version = ssl.TLSVersion.TLSv1_2
    #tls_min_version = ssl.TLSVersion.TLSv1_1
    #tls_min_version = ssl.TLSVersion.TLSv1
    return tls_min_version

# Set the context to use the minimum supported version of the SSL protocol
# We are getting minimum supported TLS version in the above line and using that
# to establish a connection
context = ssl.create_default_context()
context.minimum_version = get_minimum_supported_version()

# Now you can use this context to establish secure SSL/TLS connection
