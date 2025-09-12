from saml2 import saml, response
from saml2.entity_category import parse_attribute_map

def parse_saml_soap_envelope(soap_envelope: str):
    # Parse the SOAP envelope to extract the SAML response
    saml_response = response.from_string(soap_envelope)

    # Check that it is a valid SAML response
    if not saml_response.is_valid():
        raise ValueError("Invalid SAML response.")

    # Extract the SAML assertion from the response
    assertions = saml_response.assertions

    # Convert the SAML assertion to a string and return
    return str(assertions)

# Example usage:
soap_envelope = """<SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/">
    <SOAP-ENV:Header/>
    <SOAP-ENV:Body>
        <!-- SAML Response goes here -->
    </SOAP-ENV:Body>
</SOAP-ENV:Envelope>"""

saml_thing = parse_saml_soap_envelope(soap_envelope)
print(saml_thing)
