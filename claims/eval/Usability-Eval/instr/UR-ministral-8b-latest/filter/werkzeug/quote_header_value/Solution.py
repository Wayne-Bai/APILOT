from werkzeug import headers

# Sample URL and headers
url = "http://example.com"
headers_data = {
    "User-Agent": "Mozilla/5.0",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate",
    "Connection": "keep-alive"
}

# Getting the header value
user_agent = headers_data.get("User-Agent")

if user_agent:
    print("User-Agent:", user_agent)
else:
    print("User-Agent header not found.")
