from werkzeug.utils import make_response
response = make_response(app.make_response())

response_buffers = []
for data in response.get_data(as_text=True):
    response_buffers.append(data)

response.headers['Content-Length'] = str(len(''.join(response_buffers)))

if not response.headers.get('ETag'):
    response.headers['ETag'] = calculate_etag(response_buffers)
