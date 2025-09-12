import urllib3

def get_response(url):
    http = urllib3.PoolManager()
    try:
        response = http.request('GET', url)
        return response
    except urllib3.exceptions.HTTPError as e:
        print(f"An error occurred: {e}")
        return None

# Example usage:
# response = get_response('http://example.com')
# if response:
#     print(response.status)
#     print(response.data)
