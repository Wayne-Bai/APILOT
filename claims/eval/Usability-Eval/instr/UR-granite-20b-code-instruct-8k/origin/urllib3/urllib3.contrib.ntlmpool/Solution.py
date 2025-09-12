import urllib3
from urllib3.poolmanager import PoolManager

class MyNTLMPoolManager(PoolManager):
    def __init__(self, **kwargs):
       PoolManager.__init__(self, **kwargs)

    def _make_connection(self, conn_id):
        conn = self.connection_Cls(self.num_pools, **self.connection_pool_kw)
        if self.proxy_headers:
            conn.proxy_headers = self.proxy_headers

        # AddNTLMAuthentication here
        conn.connect()
        return conn

http = MyNTLMPoolManager(headers=headers, **pool_manager_kwargs)
