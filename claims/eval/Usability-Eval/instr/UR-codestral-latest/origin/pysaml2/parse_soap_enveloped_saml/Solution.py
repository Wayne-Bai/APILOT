import saml2
from saml2 import BINDING_SOAP
from saml2.client import Saml2Client
from saml2.s_utils import dumps_xml

def parse_saml(saml_envelope):
    """
    Parse a SOAP enveloped SAML message and return the SAML message as a string
    """
    # Create an empty SAML client (no configuration needed for parsing)
    client = Saml2Client(config={})

    # Parse the SOAP enveloped SAML message
    message = client.parse_authn_request(saml_envelope, BINDING_SOAP)

    # Return the SAML message as a string
    return dumps_xml(message.message)
