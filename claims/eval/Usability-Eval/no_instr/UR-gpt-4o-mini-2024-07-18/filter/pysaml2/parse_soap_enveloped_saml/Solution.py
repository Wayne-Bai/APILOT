from pysaml2 import saml, config
from lxml import etree

def parse_saml_from_soap(soap_envelope):
    # Parse the SOAP envelope
    namespaces = {
        'soapenv': 'http://schemas.xmlsoap.org/soap/envelope/',
        'saml': 'urn:oasis:names:tc:SAML:2.0:assertion'
    }
    
    # Parse the XML content
    soap_tree = etree.fromstring(soap_envelope)
    
    # Find the SAML assertion in the SOAP body
    saml_assertion = soap_tree.find('.//saml:Assertion', namespaces)
    
    if saml_assertion is not None:
        # Return the SAML assertion as a string
        return etree.tostring(saml_assertion, pretty_print=True).decode()
    else:
        raise ValueError("No SAML assertion found in the provided SOAP envelope.")

# Example usage:
# soap_envelope = "<SOAP Envelope XML here>"
# saml_string = parse_saml_from_soap(soap_envelope)
# print(saml_string)
