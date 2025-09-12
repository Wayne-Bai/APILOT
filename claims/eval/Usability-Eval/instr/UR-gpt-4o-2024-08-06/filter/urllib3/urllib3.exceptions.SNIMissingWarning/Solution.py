import urllib3

def make_https_request(url):
    http = urllib3.PoolManager()

    try:
        response = http.request('GET', url)
        print(f"Status: {response.status}")
        print(response.data.decode('utf-8'))
    except urllib3.exceptions.SSLError as e:
        print("SSL Error:", e)
    except urllib3.exceptions.HTTPWarning as warning:
        if isinstance(warning, urllib3.exceptions.SNIMissingWarning):
            print("SNI is not available in the request.")
        else:
            print("HTTP Warning:", warning)

if __name__ == "__main__":
    url = 'https://www.example.com'
    make_https_request(url)
