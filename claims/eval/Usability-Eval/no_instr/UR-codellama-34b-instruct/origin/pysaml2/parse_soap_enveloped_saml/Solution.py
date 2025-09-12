import base64
from pysaml2 import soap

def parse_soap_enveloped_saml(data):
    # Parse the SOAP envelope and extract the SAML message
    saml = soap.parse_soap_envelope(data)
    
    # Extract the SAML token from the message
    token = saml['SAML:Assertion']
    
    # Decode the base64-encoded SAML token
    decoded_token = base64.b64decode(token)
    
    # Return the decoded SAML token as a string
    return decoded_token.decode('utf-8')
