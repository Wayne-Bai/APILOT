import requests

def disable_insecure_ssl(host):
    # Create a secure connection context to the host with default CA certificates
    session = requests.Session()
    session.verify = True  # default should be True to verify server cert
    
    # Load custom SSL Context
    from requests.packages.urllib3.contrib import pyOpenSSL
    from requests.packages.urllib3.exceptions import InsecureRequestWarning
    import ssl
    
    # Get the CA certificates
    ca_cert_path = '/etc/ssl/certs/ca-certificates.crt' # Path to the trusted certificates on your system
    
    # Create a SSL Context
    context = ssl.create_default_context(cafile=ca_cert_path)
    
    # Load custom SSL Context
    session.mount(host, requests.adapters.HTTPAdapter(max_retries=requests.packages.urllib3.util.Retry(total=1), ssl_context=context)) #"https://"
    
    # Disable the warning
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

    # Use the session instance to make the request with disabled insecure SSL
    resp = session.get(f'https://{host}', verify=False)
    print(resp.text)

# Use the function to make a request
disable_insecure_ssl("example.com")
