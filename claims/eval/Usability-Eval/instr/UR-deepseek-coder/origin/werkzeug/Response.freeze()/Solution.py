from werkzeug.wrappers import Response
import hashlib

def prepare_response_for_pickling(response: Response) -> Response:
    # Buffer the response into a list
    buffered_data = []
    for data in response.response:
        buffered_data.append(data)
    
    # Set the Content-Length header
    response.headers['Content-Length'] = str(sum(len(d) for d in buffered_data))
    
    # Generate an ETag header if one is not already set
    if 'ETag' not in response.headers:
        etag_content = ''.join(buffered_data).encode('utf-8')
        etag = hashlib.sha1(etag_content).hexdigest()
        response.headers['ETag'] = f'"{etag}"'
    
    return response
