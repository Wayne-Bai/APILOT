import urllib3

def get_proxied_server_info(proxy_url):
    http = urllib3.PoolManager()
    try:
        response = http.request('GET', proxy_url)
        if response.status == 200:
            # Assuming the response contains the server name and port in the format "server_name:port"
            server_info = response.data.decode('utf-8').strip()
            server_name, port = server_info.split(':')
            return server_name, port
        else:
            print(f"Failed to retrieve server info. Status code: {response.status}")
            return None, None
    except urllib3.exceptions.HTTPError as e:
        print(f"An error occurred: {e}")
        return None, None

# Example usage
proxy_url = "http://your-proxy-server.com/server_info"
server_name, port = get_proxied_server_info(proxy_url)
if server_name and port:
    print(f"Server Name: {server_name}, Port: {port}")
else:
    print("Failed to retrieve server information.")
