import urllib3

http = urllib3.PoolManager()
http.load_certificate = urllib3.security.ca_batteries.SSLContext.load_verify_locations
http.load_verify_locations = urllib3.security.ca_batteries.SSLContext.load_verify_locations
http.ssl_version = urllib3.util.ssl_.get_best_ssl_version()
http.max_retries = 3

# Now you can use the http object to make requests
