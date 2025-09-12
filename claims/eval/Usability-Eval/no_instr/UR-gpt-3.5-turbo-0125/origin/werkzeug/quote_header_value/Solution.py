
from werkzeug.datastructures import Headers

# Create a sample header with a custom value
headers = Headers()
headers.add('X-Custom-Header', 'custom-value')

# Quote the header value if necessary
header_value = headers.get('X-Custom-Header')
quoted_value = Headers()._quote(header_value)

print(f'Quoted value: {quoted_value}')
