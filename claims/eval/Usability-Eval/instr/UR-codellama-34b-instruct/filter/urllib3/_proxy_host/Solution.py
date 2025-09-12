
import urllib3

proxy = {
    'http': 'http://127.0.0.1:8080',
}

urllib3.request(
    'GET',
    'https://www.example.com/',
    proxies=proxy,
)
