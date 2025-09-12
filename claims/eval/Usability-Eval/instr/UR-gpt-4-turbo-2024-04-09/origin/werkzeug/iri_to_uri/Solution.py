from werkzeug.urls import iri_to_uri

def convert_iri_to_uri(iri):
    return iri_to_uri(iri)

# Example usage
iri = "https://example.com/über"
uri = convert_iri_to_uri(iri)
print(uri)
