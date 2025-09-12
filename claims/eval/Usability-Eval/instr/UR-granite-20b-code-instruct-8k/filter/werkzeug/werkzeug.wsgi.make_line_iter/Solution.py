from werkzeug.urls import url_encode
url_encode({'foo': 'bar', 'baz': ' qux'})
# => 'foo=bar&baz=%20qux'
