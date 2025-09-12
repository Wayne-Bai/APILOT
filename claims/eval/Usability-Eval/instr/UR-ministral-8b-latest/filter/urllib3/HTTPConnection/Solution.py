import urllib3
from urllib3.util.connection import Connection

# Create an HTTPConnection instance to an example server
http = urllib3.PoolManager()
connection = http.connection_poolmanager.add(index='http', conn=Connection(), **kwargs)
