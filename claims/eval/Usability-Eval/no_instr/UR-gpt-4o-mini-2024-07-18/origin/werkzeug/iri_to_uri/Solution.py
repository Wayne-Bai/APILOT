from werkzeug.urls import iri_to_uri

def convert_iri_to_uri(iri):
    try:
        uri = iri_to_uri(iri)
        return uri
    except Exception as e:
        print(f"Error converting IRI to URI: {e}")
        return None

# Example usage:
iri = "http://example.com/привет"  # An example IRI containing non-ASCII characters
uri = convert_iri_to_uri(iri)
print(uri)
