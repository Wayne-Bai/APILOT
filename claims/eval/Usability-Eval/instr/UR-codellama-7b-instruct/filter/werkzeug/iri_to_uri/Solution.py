
import urllib

def convert_iri_to_uri(iri):
    uri = urllib.parse.quote(iri)
    return uri
