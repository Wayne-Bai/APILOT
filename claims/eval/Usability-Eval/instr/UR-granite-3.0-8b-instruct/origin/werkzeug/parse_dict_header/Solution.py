from werkzeug.http import parse_cookie

def parse_cookie_to_dict(cookie_string):
    cookie_dict = {}
    for pair in parse_cookie(cookie_string).values():
        key, value = pair.split('=', 1)
        cookie_dict[key] = value
    return cookie_dict

# Example usage:
cookie_string = "sessionid=12345; username=johndoe; theme=light"
cookie_dict = parse_cookie_to_dict(cookie_string)
print(cookie_dict)
