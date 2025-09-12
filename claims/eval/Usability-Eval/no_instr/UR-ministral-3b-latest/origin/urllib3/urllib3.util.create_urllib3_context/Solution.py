import urllib3
import ssl

# Creates and configures an ssl.SSLContext instance for use with urllib3
http = urllib3.PoolManager(
    ssl=ssl._create_default_https_context()
)

# Configures the SSLContext with specific options if needed
http = urllib3.PoolManager(
    ssl_context=ssl.create_default_context(),
    maxsize=10,
    timeout=urllib3.util.timeout.Timeout(5, 5)
)

# Usage
response = http.request('GET', 'https://www.example.com')
print(response.status)
