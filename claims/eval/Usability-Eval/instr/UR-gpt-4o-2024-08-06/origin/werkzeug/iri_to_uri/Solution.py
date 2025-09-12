from werkzeug.urls import url_quote

def iri_to_uri(iri):
    # Convert an IRI to a URI using UTF-8 encoding
    uri = url_quote(iri, safe=':/?#[]@!$&\'()*+,;=%')
    return uri

# Example usage:
iri_example = "http://example.com/Übermensch"
uri_example = iri_to_uri(iri_example)
print(uri_example)
