import urllib3

def get_connection_and_make_request(url, headers, max_redirects=5):
    http = urllib3.PoolManager()
    for attempt in range(max_redirects):
        try:
            response = http.request('GET', url, headers=headers)
            if response.status == 301 or response.status == 302:
                # Handle cross-host redirect
                new_url = response.headers['Location']
                break
            else:
                return response
        except urllib3.exceptions.RequestException as e:
            # Handle connection errors
            print(f"Connection error: {e}")
            continue
    else:
        print("Max redirects reached. Unable to retrieve the resource.")
        return None

    return response
