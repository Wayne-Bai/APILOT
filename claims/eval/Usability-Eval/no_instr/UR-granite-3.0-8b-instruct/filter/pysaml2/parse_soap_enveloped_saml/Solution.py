from pysaml2.samlfacility import SAML2
from pysaml2.soap import SOAP

def parse_saml_response(saml_response_soap_envelope):
    # Parse the SOAP envelope
    soap = SOAP(saml_response_soap_envelope)

    # Get the SAML response
    saml_response = soap.body

    # Return the SAML response as a string
    return str(saml_response)
