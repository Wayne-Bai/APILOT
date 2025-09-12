import urllib3

http = urllib3.PoolManager()

def warn_no_sni(url):
    try:
        response = http.request('GET', url)
        if response.getheader('Server').startswith('nginx'):
            print("Warning: SNI not available for this server.")
        else:
            print("No warning, SNI available for this server.")
    except Exception as e:
        print(f"Error: {e}")

# Usage
warn_no_sni('https://example.com')
