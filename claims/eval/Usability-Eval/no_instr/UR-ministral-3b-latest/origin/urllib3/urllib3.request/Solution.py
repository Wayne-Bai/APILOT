import urllib3

# Code to use urllib3 without outdated APIs
http = urllib3.PoolManager()
response = http.request("GET", "<URL>")
print(response.read().decode("utf-8"))
