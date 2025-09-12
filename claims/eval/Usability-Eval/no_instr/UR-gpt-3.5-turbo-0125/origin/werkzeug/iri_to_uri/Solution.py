
from werkzeug.urls import iri_to_uri

iri = 'http://www.example.com/my path'
uri = iri_to_uri(iri)

print(uri)
