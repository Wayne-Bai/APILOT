import urllib3
from urllib3.util.ssl_ import create_urllib3_context, DEFAULT_CIPHERS

def verify_cert(hostname, cert):
    """
    Verify that the given decoded certificate matches the given hostname.
    Parameters:
    hostname (str): The hostname to verify.
    cert (bytes): The decoded certificate to verify.
    """
    # Create an SSL context
    ssl_context = create_urllib3_context(ciphers=DEFAULT_CIPHERS)

    # The maximum length of hostname against which the certificate should match must be one,
    # which means the hostname order with an ending *. should be comparated
    for subj in cert['subject'].split(','):
        if hostname == subj.split()[0]:
            # Cert check passed
            return

    raise urllib3.URLError("Certificate validation failed.")

# Usage example:
hostname = "example.com"
cert = {
    'subject': "C = US, O = Example, CN = example.com"
}

try:
    verify_cert(hostname, cert)
    print("Certificate is valid.")
except urllib3.URLError as e:
    print(e)
