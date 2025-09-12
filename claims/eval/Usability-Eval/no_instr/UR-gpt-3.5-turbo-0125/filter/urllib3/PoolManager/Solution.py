
import urllib3

http = urllib3.PoolManager()

def custom_redirect(response, **kwargs):
    location = response.get_redirect_location()
    if location:
        return location

    return None

http.request('GET', 'http://www.example.com', redirect=custom_redirect)
