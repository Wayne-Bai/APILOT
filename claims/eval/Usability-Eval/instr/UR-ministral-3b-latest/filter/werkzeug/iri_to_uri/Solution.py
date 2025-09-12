from werkzeug.urls import iri_to_uri

# Example IRI
iri = 'https://example.com/path/to/resource'

# Convert IRI to URI
uri = iri_to_uri(iri)
print(uri)
