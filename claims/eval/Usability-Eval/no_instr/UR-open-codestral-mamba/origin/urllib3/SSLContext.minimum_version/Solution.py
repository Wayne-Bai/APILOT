import urllib3

http = urllib3.PoolManager()

SSLSensitiveCompleteURL = "https://example.com" #replace this with your actual SSL URL

try:
    # Getting the connection pool for the URL
    conn_pool = http.connection_pool_from_url(SSLSensitiveCompleteURL)

    # Getting the chosen SSL/TLS version
    ssl_version = conn_pool.ssl_version

    print("The lowest supported TLS/SSL version is {}".format(ssl_version))

except urllib3.exceptions.SSLError as e:
    print("An error occurred: {}".format(e))
