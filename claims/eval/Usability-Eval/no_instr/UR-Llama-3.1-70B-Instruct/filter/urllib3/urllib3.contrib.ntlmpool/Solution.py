# Importing required modules
import urllib3
from requests_ntlm import HttpNtlmAuth

# Suppressing the InsecureRequestWarning
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Creating an NTLM authentication pool with urllib3
class NTLMHttpPool(urllib3.HTTPConnectionPool):
    def __init__(self, host, port=None, username=None, password=None, **kwargs):
        self.username = username
        self.password = password
        # Be aware that theseproxy settings can lead to finely-tuned desasters ;)
        if 'proxies' in kwargs:
            proxies = kwargs.pop('proxies')
        super(NTLMHttpPool, self).__init__(host, port=port, **kwargs)

    def _get_conn(self, timeout=None):
        conn = super(NTLMHttpPool, self)._get_conn(timeout)
        if self.username and self.password:
            # NTLM authentication
            conn.set_ntlm_credentials(self.username, self.password)
        return conn

    urlopen = urllib3.connectionpool.HTTPConnectionPool.urlopen

def main():
    # Create an NTLM authenticated connection pool
    http = NTLMHttpPool(host='your_host', port=443,
                        username='your_username', password='your_password')

    # Use the connection pool to make a request
    try:
        r = http.request('GET', '/your_path', retries=3, timeout=10)
        print(r.data.decode('utf-8'))
    except urllib3.exceptions.RequestError as e:
        print(f"Request Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
