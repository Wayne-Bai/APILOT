from werkzeug.urls import iri_to_uri

def convert_iri_to_uri(iri):
    return iri_to_uri(iri)

# Test the function
iri = "http://example.com/résumé"
print(convert_iri_to_uri(iri))
