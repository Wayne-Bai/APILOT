import xmlsec
import pysaml2

def parse_saml_envelope(saml_envelope):
    xmlsec.init()
    xmlsec.crypto.builder_check()
    xmlsec.crypto.init()

    # Parse the SOAP envelope
    saml_document = xmlsec.parser.fromstring(saml_envelope)

    # Extract the SAML assertion
    saml_assertion = saml_document.find('{http://schemas.xmlsoap.org/soap/envelope/}Body/{http://www.w3.org/2000/09/xmldsig#}Assertion')

    # Convert the SAML assertion to a string
    saml_string = xmlsec.builder.tostring(saml_assertion)

    return saml_string

# Example usage
saml_envelope = '... your SOAP enveloped SAML here ...'
saml_string = parse_saml_envelope(saml_envelope)
print(saml_string)
