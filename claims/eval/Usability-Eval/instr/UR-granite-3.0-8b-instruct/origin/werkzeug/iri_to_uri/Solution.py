from werkzeug.urls import url_unquote

def iri_to_uri(iri):
    return url_unquote(iri)
