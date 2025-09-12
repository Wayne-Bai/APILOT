from pysaml2.soap import parse_soap_enveloped_saml_thing

def parse_soap_enveloped_saml(soap_message):
    try:
        parsed_thing = parse_soap_enveloped_saml_thing(soap_message)
        return str(parsed_thing)
    except Exception as e:
        return f"Error parsing SOAP enveloped SAML: {e}"

# Example usage:
soap_message = """<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
    <soap:Body>
        <samlp:Response xmlns:samlp="urn:oasis:names:tc:SAML:2.0:protocol" ID="_123456789" Version="2.0" IssueInstant="2023-10-01T12:00:00Z">
            <saml:Assertion xmlns:saml="urn:oasis:names:tc:SAML:2.0:assertion" ID="_987654321" Version="2.0" IssueInstant="2023-10-01T12:00:00Z">
                <saml:Issuer>https://idp.example.com</saml:Issuer>
                <saml:Subject>
                    <saml:NameID>user@example.com</saml:NameID>
                </saml:Subject>
            </saml:Assertion>
        </samlp:Response>
    </soap:Body>
</soap:Envelope>"""

result = parse_soap_enveloped_saml(soap_message)
print(result)
