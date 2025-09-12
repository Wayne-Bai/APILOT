# Importing required libraries
import urllib3
import ssl

# Create a subclass of HTTPConnection that uses SSL for communication with secure servers
class HTTPSConnectionPool(urllib3.connectionpool.HTTPSConnectionPool):
    def __init__(self, host, port=None, context=None, **kwargs):
        if context is not None and not isinstance(context, ssl.SSLContext):
            raise ValueError("context must be an ssl.SSLContext instance")
        
        if port is None:
            port = 443
        
        super().__init__(host, port=port, **kwargs)
        
        if context is not None:
            self._context = context
        else:
            self._context = ssl.create_default_context()
            
    def _prepare_conn(self, conn):
        if not hasattr(conn, '_context'):
            conn._context = self._context
            
        if not hasattr(conn, '_context_check_hostname'):
            conn._context_check_hostname = self._context.check_hostname
            
        return super()._prepare_conn(conn)

# Create a connection to a specific host using the HTTPS connection pool
if __name__ == "__main__":
    https_pool = HTTPSConnectionPool("www.example.com")
    r = https_pool.urlopen('GET', '/')
    
    # Print the HTTP status code of the response
    print("Status:", r.status)
    
    # Print the data received from the server
    print("Data:", r.data.decode())
