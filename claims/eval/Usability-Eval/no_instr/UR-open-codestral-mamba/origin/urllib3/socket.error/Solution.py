import urllib3

http = urllib3.PoolManager()

def get_data():
    try:
        r = http.request('GET', 'https://httpbin.org/get')
        return r.data
    except Exception as e:
        with open('agent_log.txt', 'a') as f:
            f.write(str(e))
        return None

data = get_data()
