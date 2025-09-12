import urllib3

http = urllib3.PoolManager()

def ntlm_authenticate_pool(url, username, password):
    auth_headers = {
        'Authorization': 'NTLM TlRMTVNTUAABAAAA ihDOTQ7B-origin==',
        'Content-Type': 'application/json'
    }

    response = http.request('GET', url, headers=auth_headers)
    if response.status == 200:
        print("NTLM Authentication Successful!")
    else:
        print("NTLM Authentication Failed!")

url = 'http://example.com'
username = 'your_username'
password = 'your_password'

ntlm_authenticate_pool(url, username, password)
