import pysaml2
from pysaml2 import soap

def parse_soap_envelope(data):
    """Parses a SOAP enveloped SAML thing and returns the thing as a string."""
    try:
        soap_message = soap.SOAPMessage(data)
        # Extract the SAML thing from the SOAP message
        saml_thing = soap_message.find("{%s}" % pysaml2.NAMESPACES["saml"])[0]
        return etree.tostring(saml_thing, pretty_print=True).decode()
    except:
        raise ValueError("Failed to parse the SOAP envelope")
