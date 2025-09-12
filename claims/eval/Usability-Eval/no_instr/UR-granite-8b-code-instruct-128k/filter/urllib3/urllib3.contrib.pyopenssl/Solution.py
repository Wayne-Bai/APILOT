import urllib3
from urllib3.contrib.pyopenssl import PyOpenSSLContext
http = urllib3.PoolManager(context=PyOpenSSLContext)
