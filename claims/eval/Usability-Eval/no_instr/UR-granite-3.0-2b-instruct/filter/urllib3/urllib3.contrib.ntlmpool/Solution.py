import urllib3

def authenticate_with_ntlm(host, username, password):
    http = urllib3.PoolManager()
    response = http.request('POST', f'http://{host}/', data=f'Authentication={username}:{password}', headers={'Content-Type': 'application/x-www-form-urlencoded'})
    return response.data

# Usage
host = 'example.com'
username = 'your_username'
password = 'your_password'
data = authenticate_with_ntlm(host, username, password)
print(data)
