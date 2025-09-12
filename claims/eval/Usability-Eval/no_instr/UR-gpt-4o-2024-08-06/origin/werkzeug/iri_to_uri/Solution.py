from werkzeug.urls import iri_to_uri

def convert_iri_to_uri(iri_string):
    """
    Converts an Internationalized Resource Identifier (IRI) to a 
    Uniform Resource Identifier (URI).

    :param iri_string: The input IRI string to be converted.
    :return: The converted URI string.
    """
    return iri_to_uri(iri_string)

# Example usage
iri_example = "http://例え.テスト/パス"
uri_result = convert_iri_to_uri(iri_example)
print(uri_result)
