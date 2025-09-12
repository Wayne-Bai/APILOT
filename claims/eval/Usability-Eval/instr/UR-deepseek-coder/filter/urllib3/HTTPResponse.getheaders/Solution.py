import urllib3

def get_unmodifiable_headers(headers):
    # Create a PoolManager instance
    http = urllib3.PoolManager()
    
    # Convert headers to a case-insensitive, unmodifiable dictionary
    unmodifiable_headers = http._normalize_headers(headers)
    
    return unmodifiable_headers

# Example usage
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer token'
}

unmodifiable_headers = get_unmodifiable_headers(headers)
print(unmodifiable_headers)
