import urllib3

# create a connection pool
http = urllib3.PoolManager()

# define a custom redirect function
def custom_redirect(self, response, **request_kwargs):
    # your custom cross-host logic here
    url = request_kwargs.get('url')
    # modify url to handle the redirection according to your logic
    r = self.request('GET', url, **request_kwargs)
    return r

# integrate the custom_redirect function into urllib3
http.connection_pool.request = custom_redirect

# make a GET request
request_url = 'http://example.com'
response = http.request('GET', request_url)

# for urllib3 versions before 1.25 response is Unicode, it's safer to always decode it
print(response.data.decode('utf-8'))
