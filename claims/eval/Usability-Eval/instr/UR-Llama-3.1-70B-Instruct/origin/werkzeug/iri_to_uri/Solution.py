# Import the necessary modules from werkzeug
from werkzeug.urls import url_parse, url_unparse
import urllib.parse

# Function to convert IRI to URI
def iri_to_uri(iri):
    """
    Convert an IRI to a URI.

    This function takes an IRI as input, converts it to a URI and returns the URI.
    The conversion involves converting the IRI's scheme and netloc to ASCII and
    encoding any non-ASCII characters in the path, query, and fragment.
    """
    parsed = url_parse(iri)
    
    # Convert scheme and netloc to ASCII
    scheme = parsed.scheme.encode('ascii').decode('ascii')
    netloc = parsed.netloc.encode('ascii').decode('ascii')
    
    # Encode non-ASCII characters in the path, query, and fragment
    path = urllib.parse.quote(parsed.path, safe='/')
    query = urllib.parse.quote(parsed.query, safe='=&')
    fragment = urllib.parse.quote(parsed.fragment, safe='')
    
    # Reconstruct the URI
    uri = url_unparse((scheme, netloc, path, parsed.params, query, fragment))
    
    return uri

# Example usage:
iri = 'http://example.com/path with spaces?param1=value1&param2=value2#fragment'
uri = iri_to_uri(iri)
print(uri)
