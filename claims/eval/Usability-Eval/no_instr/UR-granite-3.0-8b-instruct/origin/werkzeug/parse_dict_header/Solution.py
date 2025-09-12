from werkzeug.http import parse_cookie

def parse_cookies(cookies):
    parsed_cookies = {}
    for cookie in cookies:
        key, value = cookie.split('=', 1)
        parsed_cookies[key] = value
    return parsed_cookies

# Example usage:
cookies = "key1=value1; key2=value2; key3=value3"
parsed_cookies = parse_cookies([cookies])
print(parsed_cookies)
