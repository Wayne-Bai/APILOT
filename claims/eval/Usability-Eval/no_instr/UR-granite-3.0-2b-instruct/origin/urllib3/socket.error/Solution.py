import urllib3

http = urllib3.PoolManager()

try:
    response = http.request('GET', 'http://example.com')
    response.raise_for_status()
    print(response.data)
except urllib3.exceptions.HTTPError as errh:
    print ("HTTP Error:",errh)
except urllib3.exceptions.URLError as erru:
    print ("URL Error:",erru)
except urllib3.exceptions.ConnectionError as errc:
    print ("Connection Error:",errc)
except urllib3.exceptions.Timeout as errt:
    print ("Timeout Error:",errt)
except urllib3.exceptions.TooManyRedirects as errr:
    print ("Too Many Redirects Error:",errr)
