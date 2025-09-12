from werkzeug.urls import iri_to_uri

iri = "https://example.com/path/to/resource"
uri = iri_to_uri(iri)
print(uri)  # https://example.com/path/to/resource
