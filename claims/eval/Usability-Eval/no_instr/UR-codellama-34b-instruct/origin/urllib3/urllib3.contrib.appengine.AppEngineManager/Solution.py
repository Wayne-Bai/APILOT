import urllib3

class GAEConnectionManager:
    def __init__(self, app_id):
        self.app_id = app_id
        self.session = None

    def get_session(self):
        if not self.session:
            self.session = urllib3.PoolManager()
        return self.session

    def make_request(self, url, method="GET", headers={}, data=None):
        session = self.get_session()
        request_headers = {"Content-Type": "application/json"}
        if headers:
            request_headers.update(headers)
        response = session.request(method, url, headers=request_headers, body=data)
        return response.status, response.json()
