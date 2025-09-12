
# Importing urllib3 library
import urllib3

# Creating a PoolManager instance
http = urllib3.PoolManager()

# Sending a GET request to a URL to retrieve data
url = 'http://www.example.com/data'
response = http.request('GET', url)

# Check if the response status code is not 200
if response.status != 200:
    # Write the error message to the log file
    with open('agent_log.txt', 'a') as log_file:
        log_file.write(f'Error: Unable to retrieve data from {url}. Status Code: {response.status}\n')
