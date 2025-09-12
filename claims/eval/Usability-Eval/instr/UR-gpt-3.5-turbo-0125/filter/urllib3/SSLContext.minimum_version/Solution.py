
import urllib3

# Define a custom function to get the lowest supported TLS version
def get_lowest_supported_tls_version():
    try:
        # Create a dummy pool manager to access TLS configuration
        pool_manager = urllib3.PoolManager()
        
        # Get the TLS configuration object
        tls_config = pool_manager.connection_pool_kw.get('cert_reqs')

        # Return the lowest supported TLS version
        return tls_config.minimum_version

    except Exception as e:
        print(f"Error: {e}")
        return None

# Call the function to get the lowest supported TLS version
lowest_tls_version = get_lowest_supported_tls_version()
print(f"Lowest supported TLS version: {lowest_tls_version}")
