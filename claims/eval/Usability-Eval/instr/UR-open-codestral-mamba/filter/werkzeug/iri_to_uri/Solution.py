from werkzeug.urls import url_parse, url_fix

def iri_to_uri(iri):
    """Convert an IRI to a URI."""
    url = url_parse(iri.strip())
    normal_chars = url.to_url(quote=True, charset='utf-8')
    fixed_chars = url_fix(normal_chars)
    return fixed_chars

# Example usage:
input_iri = "http://www.example.com/foo/bar"
output_uri = iri_to_uri(input_iri)
print(output_uri)
