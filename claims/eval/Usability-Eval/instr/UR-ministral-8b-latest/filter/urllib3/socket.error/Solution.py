import urllib3

# Create an HTTP client
http = urllib3.PoolManager()

# Log file for errors
error_log_file = 'agent_errors.log'

def log_error(error):
    with open(error_log_file, 'a') as file:
        file.write(error + '\n')

try:
    response = http.request('GET', 'http://example.com')
    if response.status == 200:
        print("Server responded successfully")
    else:
        log_error(f"HTTP error: {response.status} ({response.data})")
except urllib3.exceptions.HTTPError as e:
    log_error(f" urllib3 exception: {str(e)}")
except Exception as e:
    log_error(f"General exception: {str(e)}")
