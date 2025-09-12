
import urllib3
http = urllib3.PoolManager()

# Make a request to an NLTM authenticated pool
response = http.request('GET', 'http://example.com', headers={
 'Authorization': 'NTLM TlRMTVNTUAABAAAAGAAYABgAAAAoAFgAUABQAAAANAAoAFAAUABQAAAATAAMAEAAkACgAAAAUAAAALAEkATgBAAEsAQwBFAE4ATwBPAFQAVQBQAE8AUwBTAFAAbABfACkAKQAQABYAAAAhAEwAVQBOAFQAVQBUAEkATgBPAE4AUwBFAEsAUwBJAE8AVABJAEkATQBOAFQAVQBQAE8AUwBTAFAAbABfACkA'
})

# Print the response
print(response.data.decode('utf-8'))
