from urllib3 import PoolManager

class GoogleAppEngineConnectionManager:
    def __init__(self, host='appengine.gcloud.googleapis.com', port=8080):
        self.pool_manager = PoolManager(host=host, port=port)

    def request(self, method, url, **kwargs):
        with self.pool_manager.request(method, url, **kwargs) as response:
            return response.data

    def close(self):
        self.pool_manager.release_connection()
