
from xml.etree import ElementTree as ET

def parse_saml_envelope(saml_envelope):
    # Parse the SOAP enveloped SAML
    saml_tree = ET.fromstring(saml_envelope)
    
    # Extract the SAML thing
    saml_thing = saml_tree.find('.//{urn:oasis:names:tc:SAML:2.0:assertion}Assertion')
    
    # Return the SAML thing as a string
    return ET.tostring(saml_thing).decode()

# Example usage
saml_envelope = "<SOAP-ENV:Envelope>...</SOAP-ENV:Envelope>"
saml_thing_string = parse_saml_envelope(saml_envelope)
print(saml_thing_string)
