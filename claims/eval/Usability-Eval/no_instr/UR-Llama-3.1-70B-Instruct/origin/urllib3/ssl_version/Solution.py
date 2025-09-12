# Importing required libraries
import ssl
import urllib.request

# Creating an SSL context object
context = ssl.create_default_context()
context.options &= ~ssl.OP_NO_TLSv1
context.options &= ~ssl.OP_NO_TLSv1_1

# Add supported protocols
context.options |= ssl.OP_NO_TLSv1_3 
context.options |= ssl.OP_NO_SSLv3
context.minimum_version = ssl.TLSVersion.TLSv1_2

def get_supported_ssl_versions(url):
    """
    Function to check the supported SSL versions
    """
    try:
        # Opening the connection with our created SSL context
        with urllib.request.urlopen(url, context=context) as response:
            print("Supported SSL version:", context.maximum_version)

    except ssl.SSLError as e:
        print("SSL Error occurred:", e)

    except Exception as e:
        print("An error occurred:", e)


# Usage
url = 'https://example.com'  # replace with the desired URL
get_supported_ssl_versions(url)
