from werkzeug import IRI

def convert_iri_to_uri(iri):
    return IRI(iri).get_uri()
