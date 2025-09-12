import werkzeug

app = werkzeug.wrappers.BaseRequest()

@app.route('/', methods=['POST'])
def parse_json():
    request_data = request.get_json()
    return request_data