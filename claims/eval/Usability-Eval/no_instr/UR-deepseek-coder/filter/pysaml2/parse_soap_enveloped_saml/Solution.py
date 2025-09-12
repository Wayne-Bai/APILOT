import xml.etree.ElementTree as ET
from pysaml2.saml import SamlBase

def parse_soap_enveloped_saml(soap_envelope: str) -> str:
    # Parse the SOAP envelope XML
    root = ET.fromstring(soap_envelope)
    
    # Find the SAML assertion within the SOAP envelope
    saml_assertion = root.find('.//{urn:oasis:names:tc:SAML:2.0:assertion}Assertion')
    
    if saml_assertion is not None:
        # Convert the SAML assertion back to a string
        saml_assertion_str = ET.tostring(saml_assertion, encoding='unicode')
        return saml_assertion_str
    else:
        raise ValueError("No SAML assertion found in the SOAP envelope.")

# Example usage:
soap_envelope = """
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
    <soap:Body>
        <saml:Assertion xmlns:saml="urn:oasis:names:tc:SAML:2.0:assertion">
            <!-- SAML assertion content -->
        </saml:Assertion>
    </soap:Body>
</soap:Envelope>
"""

saml_assertion_str = parse_soap_enveloped_saml(soap_envelope)
print(saml_assertion_str)
