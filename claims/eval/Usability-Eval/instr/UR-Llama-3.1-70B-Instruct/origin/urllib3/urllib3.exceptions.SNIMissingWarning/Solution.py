import urllib3

# disable the warnings
urllib3.disable_warnings()

# create a pools manager
http = urllib3.PoolManager()

# Define request parameters
url = "https://example.com"  # replace with your target URL
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.3"
}

# make the request without SNI
try:
    response = http.request("GET", url, headers=headers, preload_content=False, retries=5)
    
    print(f"Request successful: {response.status}")
    response.release_conn()
    
except urllib3.exceptions.SSLError as e:
    print(f"SNI is not available: {e}")
    
except Exception as e:
    print(f"Error occurred: {e}")
