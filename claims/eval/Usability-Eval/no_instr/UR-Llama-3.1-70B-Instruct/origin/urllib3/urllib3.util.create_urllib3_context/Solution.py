# Importing required modules
import urllib3
import ssl
from urllib3.util.ssl_ import create_urllib3_context

# Creating and configuring an ssl.SSLContext instance for use with urllib3
def create_ssl_context(
    cert_reqs=ssl.CERT_REQUIRED,
    ca_certs=None,
    ca_cert_dir=None,
    ca_cert_data=None,
    cert_file=None,
    key_file=None,
    key_password=None,
    cipher_suite=None,
):

    context = ssl.create_default_context(
        purpose=ssl.Purpose.SERVER_AUTH, cafile=ca_certs
    )

    if ca_cert_dir is not None:
        context.load_verify_locations(capath=ca_cert_dir)

    if ca_cert_data is not None:
        ca_cert_pem = ssl.DER_cert_to_PEM_cert(ca_cert_data)
        context.load_verify_locations(cadata=ca_cert_pem)

    if cert_file is not None and key_file is not None:
        context.load_cert_chain(
            certfile=cert_file, keyfile=key_file, password=key_password
        )

    if cert_reqs is not None:
        context.verify_mode = cert_reqs

    if cipher_suite is not None:
        context.set_ciphers(cipher_suite)

    return create_urllib3_context(ssl_context=context)

# Example usage
if __name__ == "__main__":
    ssl_context = create_ssl_context(
        ca_certs="path_to_your_ca_certs", cert_reqs=ssl.CERT_REQUIRED
    )
    pool_manager = urllib3.PoolManager(ssl_context=ssl_context)

    response = pool_manager.request('GET', 'http://httpbin.org/ip')
    print(response.status)
    print(response.data.decode())
