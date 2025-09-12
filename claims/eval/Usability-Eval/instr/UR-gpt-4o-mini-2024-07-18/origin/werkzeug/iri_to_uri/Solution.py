from werkzeug.urls import url_parse, url_unparse

def iri_to_uri(iri):
    parsed = url_parse(iri)
    # Convert the IRI components to a URI
    uri = url_unparse(parsed)
    return uri

# Example usage
iri = "http://example.com/カタカナ"
uri = iri_to_uri(iri)
print(uri)
