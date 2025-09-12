from werkzeug.urls import url_quote

# Here is an example IRI
iri = "http://example.com/café"

# Convert IRI to URI
uri = url_quote(iri)

print(uri)
