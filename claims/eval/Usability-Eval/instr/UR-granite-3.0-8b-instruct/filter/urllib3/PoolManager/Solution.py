from urllib3 import PoolManager, HTTPConnectionPool

def custom_redirect_logic(request, response):
    # Custom redirect logic goes here
    pass

def perform_request(host, request_uri):
    manager = PoolManager()
    pool = manager.get_connection(host)

    # Set custom redirect logic
    pool.pool_manager.redirect_handler = custom_redirect_logic

    # Perform request with only request_uri
    pool.urlopen('GET', request_uri, preload_content=False)

# Usage
perform_request('example.com', '/path/to/resource')
