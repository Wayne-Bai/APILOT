import urllib3
http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=None, assert_hostname=True,
	ssl_version=urllib3.util.ssl_.DEFAULT_SSL_VERSION,
	ssl_context=urllib3.contrib.pyopenssl.util.ssl_context_for_client)
