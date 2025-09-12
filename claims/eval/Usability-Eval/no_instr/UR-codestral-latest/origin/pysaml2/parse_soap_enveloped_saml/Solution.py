from saml2 import BINDING_SOAP, decoder

def parse_soap_enveloped_saml(soap_saml):
    # Decode the SOAP enveloped SAML
    pysaml_response = decoder.decode_base64_and_inflate(soap_saml)

    # Parse the SAML response
    saml_response = BINDING_SOAP.unbind(pysaml_response)

    # Return the parsed SAML response as a string
    return str(saml_response)
