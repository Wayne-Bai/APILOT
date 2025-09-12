from urllib.parse import quote

def iri_to_uri(iri):
    return quote(iri, safe=':/%')
