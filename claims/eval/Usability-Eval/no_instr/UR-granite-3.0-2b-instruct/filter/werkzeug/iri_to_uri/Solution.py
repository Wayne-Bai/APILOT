from werkzeug import url_encode

def convert_iri_to_uri(iri):
    # Encode the IRI to a URI
    uri = url_encode(iri)
    return uri
