
from werkzeug.urls import url_parse

def extract_path_info(url):
    parsed_url = url_parse(url)
    return parsed_url.path

url = "https://www.example.com/products/1234"
path_info = extract_path_info(url)
print("Path Info:", path_info)
