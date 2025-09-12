import urllib3

def make_https_request(host, port=443):
    http = urllib3.PoolManager()

    try:
        response = http.request('GET', f'https://{host}:{port}', verify=False)
        response.raise_for_status()
    except urllib3.exceptions.HTTPError as err:
        if response.status == 400:
            print(f"Bad Request: {response.data.decode()}")
        elif response.status == 404:
            print(f"Not Found: {response.data.decode()}")
        elif response.status == 500:
            print(f"Internal Server Error: {response.data.decode()}")
        else:
            print(f"Error: {err}")
    except urllib3.exceptions.ProtocolError as err:
        print(f"Protocol Error: {err}")
    except urllib3.exceptions.SSLError as err:
        if "SNICernelFailure" in str(err):
            print("Warning: SNI is not available.")
        else:
            print(f"SSL Error: {err}")
    except Exception as err:
        print(f"Error: {err}")

# Example usage:
make_https_request("example.com")
