from werkzeug.http import parse_qs, parse_qs_string, url_quote, url_unquote, url_join, parse_url

# Example usage:
input_stream = "path=example/path&query=example=value"
parsed_params = parse_qs(input_stream)

for key, values in parsed_params.items():
    for value in values:
        print(f"{key} = {value}")
