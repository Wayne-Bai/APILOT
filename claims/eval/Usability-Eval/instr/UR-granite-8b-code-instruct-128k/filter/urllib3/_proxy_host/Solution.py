
import urllib3
http = urllib3.PoolManager()

proxy_name = 'example.com'
proxy_port = 8080

proxy_pass = f"proxy_pass http://{proxy_name}:{proxy_port};"

print(proxy_pass)
