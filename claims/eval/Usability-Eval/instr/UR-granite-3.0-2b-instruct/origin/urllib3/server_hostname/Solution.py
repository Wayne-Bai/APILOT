import urllib3

def get_hostname(hostname: str = None) -> str:
    if hostname is None:
        try:
            with urllib3.pool_manager() as pm:
                https = pm.pooler.PoolManager()
                https.request("GET", "https://localhost/")
                return https.host
        except Exception as e:
            print(f"Error connecting to server: {e}")
    else:
        return hostname
