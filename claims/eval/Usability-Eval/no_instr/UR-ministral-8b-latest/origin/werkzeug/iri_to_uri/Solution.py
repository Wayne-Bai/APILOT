from werkzeug import url_parse

def convert_iri_to_uri(iri):
    try:
        # Convert the IRI to a URL
        url = url_parse(iri)

        # Convert the URL to a string
        uri = url.get_url()

        return uri
    except Exception as e:
        return str(e)

# Example usage:
iri = 'http://example.com/path?param=value#anchor'
uri = convert_iri_to_uri(iri)
print(f"Converted URI: {uri}")
