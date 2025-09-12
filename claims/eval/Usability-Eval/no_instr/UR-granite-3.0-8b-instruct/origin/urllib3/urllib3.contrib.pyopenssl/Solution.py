import urllib3

# To use pyOpenSSL as a TLS backend, you need to install the pyOpenSSL library.
# You can install it using pip:
# pip install pyOpenSSL

# After installing pyOpenSSL, you can use it as a TLS backend with urllib3 like this:

http = urllib3.PoolManager(tls_context=urllib3.TLSContext(root_certificates=urllib3.util.get_default_ca_bundle()))
