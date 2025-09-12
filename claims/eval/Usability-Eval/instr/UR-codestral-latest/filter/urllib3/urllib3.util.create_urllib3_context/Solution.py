import urllib3
import ssl

# Create a custom SSL context with specific protocols and options
ssl_context = ssl.create_default_context()
ssl_context.set_ciphers('HIGH:!DH:!aNULL')

# Configure urllib3 to use this SSL context
http = urllib3.PoolManager(ssl_context=ssl_context)

# Then you can use this http object for any urllib3 requests. Here's an example:
response = http.request('GET', 'https://www.example.com')
