
import urllib3

def read_response_body(url, amt):
    http = urllib3.PoolManager()
    response = http.request('GET', url, preload_content=False)
    
    body = b''
    while len(body) < amt:
        chunk = response.read(min(amt - len(body), 8192))
        if not chunk:
            break
        body += chunk
        
    response.release_conn()
    
    return body

url = 'http://example.com'
amt = 1024
response_body = read_response_body(url, amt)
print(response_body)
