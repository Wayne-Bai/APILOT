from xml.etree import ElementTree
from pysaml2.saml import s_utils

def parse_soap_enveloped_saml(soap_message):
    """
    Parses a SOAP enveloped SAML message and returns the SAML payload as a string.
    
    :param soap_message: A SOAP envelope XML string containing a SAML message.
    :return: The extracted SAML message as a string.
    """
    # Parse the SOAP envelope
    try:
        root = ElementTree.fromstring(soap_message)
    except ElementTree.ParseError as e:
        raise ValueError(f"Invalid SOAP message: {e}")

    # Find the SAML assertion within the SOAP body
    namespaces = {
        'soap-env': 'http://schemas.xmlsoap.org/soap/envelope/',
        'saml2': 'urn:oasis:names:tc:SAML:2.0:assertion'
    }

    # Locate the SOAP Body
    body = root.find('soap-env:Body', namespaces)
    if body is None:
        raise ValueError("No SOAP Body found in the message.")

    # Find the SAML Assertion within the SOAP Body
    saml_assertion = body.find('saml2:Assertion', namespaces)
    if saml_assertion is None:
        raise ValueError("No SAML Assertion found in the SOAP Body.")

    # Obtain the SAML assertion as a string
    saml_as_string = ElementTree.tostring(saml_assertion, encoding='unicode')
    return saml_as_string

# Example usage
soap_message = """<soap-env:Envelope xmlns:soap-env="http://schemas.xmlsoap.org/soap/envelope/">
    <soap-env:Body>
        <saml2:Assertion xmlns:saml2="urn:oasis:names:tc:SAML:2.0:assertion">
            <!-- SAML Assertion content -->
        </saml2:Assertion>
    </soap-env:Body>
</soap-env:Envelope>"""

try:
    print(parse_soap_enveloped_saml(soap_message))
except ValueError as e:
    print(f"Error parsing the message: {e}")
