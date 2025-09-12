import urllib3
import ssl
import warnings

# Suppress UserWarning related to the use of deprecated APIs
warnings.filterwarnings("ignore", category=UserWarning, module='urllib3')

class CustomHttp:
    def __init__(self):
        # Generate a custom SSLContext with the lowest supported TLS version
        ssl_context = ssl.create_default_context()
        self.ssl_context = ssl_context

        # The minimum supported version is TLSVersion.TLSv1
        self.ssl_context.options |= ssl.OP_NO_TLSv1_2
        self.ssl_context.options |= ssl.OP_NO_TLSv1_1

        self.http = urllib3.HTTPSConnectionPool('https://httpbin.org', cert_reqs=ssl.CERT_REQUIRED, context=self.ssl_context)

    def request(self, method, url, **kwargs):
        return self.http.request(method, url, **kwargs)


# Usage:
if __name__ == "__main__":
    http = CustomHttp()
    res = http.request('GET', '/ip')
    print(res.status)
    print(res.headers)
    print(res.data)
