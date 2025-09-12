import requests

def check_content_length(url):
    response = requests.get(url)

    content_length = response.headers.get('Content-Length')
    if content_length is not None:
        if int(content_length) != len(response.content):
            raise ValueError("Content-Length header does not match the size of body.")

# Use the function with a URL
check_content_length('https://your-url.com')
