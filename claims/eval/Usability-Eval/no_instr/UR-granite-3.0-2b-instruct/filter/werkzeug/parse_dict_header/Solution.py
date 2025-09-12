from werkzeug import Request, util

def parse_query_string(query_string):
    query_string = query_string.strip()
    if not query_string:
        return {}

    pairs = query_string.split('&')
    result = {}

    for pair in pairs:
        key, value = pair.split('=')
        result[key] = util.parse_qsl(value)[0]

    return result

# Example usage:
query_string = "name=John&age=30&city=New%20York"
print(parse_query_string(query_string))
