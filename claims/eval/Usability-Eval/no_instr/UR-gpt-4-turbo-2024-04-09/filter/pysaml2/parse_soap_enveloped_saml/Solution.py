from saml2 import samlp
from saml2.s_utils import decode_base64_and_inflate

def parse_soap_enveloped_saml(xml_string):
    # Decode, decompress and parse the XML string
    decoded_xml = decode_base64_and_inflate(xml_string)
    response = samlp.any_response_from_string(decoded_xml)
    return response.to_string()

# Example usage:
xml_string = "Your base64 SOAP enveloped SAML string here"
parsed_saml = parse_soap_enveloped_saml(xml_string)
print(parsed_saml)
