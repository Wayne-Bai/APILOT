import urllib3
response_body = urllib3.connection.HTTPConnectionPool().read(url, amt=1000)
