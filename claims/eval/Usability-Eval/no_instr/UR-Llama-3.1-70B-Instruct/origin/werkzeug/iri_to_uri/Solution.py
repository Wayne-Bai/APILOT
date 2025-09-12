from werkzeug.urls import uri_to_iri, iri_to_uri

def convert_iri_to_uri(iri):
    """
    Converts an IRI to a URI.
    
    Parameters:
    iri (str): The IRI to convert.
    
    Returns:
    str: The converted URI.
    """
    # Use iri_to_uri function from werkzeug.urls to convert IRI
    uri = iri_to_uri(iri)
    
    return uri

# Test the function
iri_example = "http://example.org/path?query=abc#fragment"
print(f"Original IRI: {iri_example}")
print(f"Converted URI: {convert_iri_to_uri(iri_example)}")
