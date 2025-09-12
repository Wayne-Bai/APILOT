from werkzeug.urls import url_ir_to_uri

def convert_to_uri(iri: str) -> str:
    uri = url_ir_to_uri(iri)
    return uri

ira = "http://example.com'at'%Barras"
converted_uri = convert_to_uri(ira)
print(converted_uri)
