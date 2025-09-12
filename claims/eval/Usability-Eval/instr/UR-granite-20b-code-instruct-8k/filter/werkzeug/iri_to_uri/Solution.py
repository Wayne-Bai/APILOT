
from werkzeug.urls import iri_to_uri

def convert_iri_to_uri(iri):
    uri = iri_to_uri(iri)
    return uri
