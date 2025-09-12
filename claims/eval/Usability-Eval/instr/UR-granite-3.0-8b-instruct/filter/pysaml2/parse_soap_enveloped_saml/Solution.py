from pysaml2.saml import (
    parse_saml,
    pretty_print,
)

def parse_soap_envelope(soap_envelope):
    # Parse the SOAP envelope and extract the SAML assertion
    saml_assertion = parse_saml(soap_envelope)

    # Return the SAML assertion as a string
    return pretty_print(saml_assertion)
