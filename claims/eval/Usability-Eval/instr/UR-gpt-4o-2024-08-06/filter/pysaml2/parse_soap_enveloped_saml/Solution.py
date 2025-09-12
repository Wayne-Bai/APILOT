from xml.etree import ElementTree
from saml2.s_utils import deflate_and_base64_decode
from saml2.saml import Assertion
from saml2 import SAMLError

def parse_soap_enveloped_saml(soap_message):
    try:
        # Parse the SOAP message
        tree = ElementTree.fromstring(soap_message)

        # Find the SAML assertion within the SOAP message
        namespace = {
            'soapenv': 'http://schemas.xmlsoap.org/soap/envelope/',
            'saml': 'urn:oasis:names:tc:SAML:2.0:assertion'
        }
        assertion_element = tree.find('.//saml:Assertion', namespaces=namespace)

        if assertion_element is None:
            raise SAMLError("No SAML Assertion found in SOAP message")

        # Convert the assertion element to a string
        assertion_str = ElementTree.tostring(assertion_element, encoding='unicode')
        
        return assertion_str
    except Exception as e:
        raise SAMLError(f"Error parsing SOAP enveloped SAML: {str(e)}")

# Example usage
soap_message = """<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/">
<soapenv:Body>
<Assertion xmlns="urn:oasis:names:tc:SAML:2.0:assertion"></Assertion>
</soapenv:Body>
</soapenv:Envelope>"""
saml_string = parse_soap_enveloped_saml(soap_message)
print(saml_string)
