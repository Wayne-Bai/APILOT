import urllib3

def read_response_body(url, amt=None):
    http = urllib3.PoolManager()
    try:
        response = http.request('GET', url)
        if response.status == 200:
            if amt is None:
                return response.data
            else:
                return response.data[:amt]
        else:
            return f"Failed to retrieve data. Status code: {response.status}"
    except urllib3.exceptions.HTTPError as e:
        return f"An error occurred: {e}"

# Example usage:
# url = 'http://example.com'
# print(read_response_body(url, amt=100))
