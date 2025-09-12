import urllib3
import re

# specify proxy URL
proxy_url = "http://your-proxy-url.com:8080"

def extract_proxy_details(proxy_url):
    # Create a PoolManager to manage connections
    http = urllib3.PoolManager()
    
    try:
        # Send a request to the proxy server
        response = http.urlopen('OPTIONS', proxy_url)
        
        # Get the proxy URL from the 'Via' header
        via_header = response.getheader('Via')
        
        if via_header:
            # Use regex to extract the proxy name and port
            match = re.search(r'(\w+)\/\d+\.\d+ (\w+):(\d+)', via_header)
            if match:
                proxy_name = match.group(2)
                proxy_port = match.group(3)
                return proxy_name, proxy_port
    except Exception as e:
        print(f"An error occurred: {e}")
    
    return None, None

# Usage example
proxy_name, proxy_port = extract_proxy_details(proxy_url)

if proxy_name and proxy_port:
    print(f"Proxy name: {proxy_name}, Port: {proxy_port}")
else:
    print("Failed to extract proxy details.")
