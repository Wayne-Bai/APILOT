from werkzeug.datastructures import Headers

headers = Headers()
headers.add('Content-Type', 'text/html')
quoted_value = headers.get('Content-Type')

print(quoted_value)
