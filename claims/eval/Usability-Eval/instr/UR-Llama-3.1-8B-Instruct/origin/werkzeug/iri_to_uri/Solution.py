
from werkzeug.urls import url_encode
from urllib.parse import unquote, quote

def iri_to_uri(iri):
    """
    Convert an IRI to a URI.

    :param iri: Input IRI
    :return: Converted URI
    """
    # Unquote the input IRI to separate the path from any percent-encoded characters
    unquoted_iri = unquote(iri)
    
    # Remove any non-ASCII characters from the host part
    host_part = unquoted_iri.split(':')[0]
    ascii_host_part = ''.join(c for c in host_part if ord(c) < 128)
    
    # Replace the original host with the ASCII-compatible host
    uri = unquoted_iri.replace(host_part, ascii_host_part, 1)
    
    # Quote the URI to convert it to a valid URI
    quoted_uri = quote(uri)
    
    return quoted_uri

# Example usage
iri = "https://example.com/path?query=parameter #fragment"
uri = iri_to_uri(iri)
print(uri)
