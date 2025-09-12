import urllib3
from ssl import SSLContext, SSLError

def verify_cert(url):
    http = urllib3.PoolManager()
    context = SSLContext(ssl. protocols.ALL)
    context.check_hostname = True
    context.verify_mode = ssl.CERT_REQUIRED

    try:
        with http.request('GET', url, headers={'Host': url}) as response:
            response.raise_for_status()
            cert = response.getpeercert()
            context.load_verify_locations(cafile='ca-bundle.crt')
            context.verify_mode = ssl.CERT_REQUIRED
            context.check_hostname = True
            context.verify()
            print("Certificate matches the hostname.")
    except SSLContext.CertificateError as e:
        print("Certificate does not match the hostname.")
        print(f"Error: {e}")
    except Exception as e:
        print("An error occurred:", e)

# Example usage
verify_cert("https://example.com")
