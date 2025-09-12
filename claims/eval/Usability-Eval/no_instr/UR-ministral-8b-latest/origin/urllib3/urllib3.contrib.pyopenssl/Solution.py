import urllib3
from urllib3.contrib import pyopenssl
import requests

# Setup urllib3 to use pyOpenSSL as the TLS backend
urllib3.disable_warnings()
http = urllib3.PoolManager(cert_reqs='CERT_NONE', ca_certs=None, ssl_version=pyopenssl.SSLVersion.TLSv1_2)
