import urllib3

def get_hostname(self):
    if self.hostname is None:
        return None
    return str(self.hostname)
