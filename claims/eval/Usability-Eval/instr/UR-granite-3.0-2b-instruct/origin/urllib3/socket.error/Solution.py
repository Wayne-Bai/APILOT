import urllib3

http = urllib3.PoolManager()

try:
    response = http.request('GET', 'http://example.com')
    response.raise_for_status()
    print(response.data)
except urllib3.exceptions.HTTPError as errh:
    print ("HTTP Error:", errh)
except urllib3.exceptions.URLError as erru:
    print ("URL Error:", erru)
except urllib3.exceptions.ConnectionError as errc:
    print ("Connection Error:", errc)
except urllib3.exceptions.Timeout as errt:
    print ("Timeout Error:", errt)
except urllib3.exceptions.ChunkedEncodingError as errce:
    print ("Chunked Encoding Error:", errce)
except urllib3.exceptions.Sorry as errsor:
    print ("Sorry Error:", errsor)
except urllib3.exceptions.SocketError as errsock:
    print ("Socket Error:", errsock)
except urllib3.exceptions.C100Error as errc100:
    print ("C100 Error:", errc100)
except urllib3.exceptions.RequestException as errreq:
    print ("Request Error:", errreq)
