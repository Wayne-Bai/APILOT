from saml2 import soap

def parse_soap_saml(soap_envelope):
    try:
        # Parse the SOAP envelope and extract the SAML message
        saml_message = soap.extract_message_from_soap(soap_envelope)
        return saml_message
    except Exception as e:
        return str(e)

# Example usage
soap_envelope = """
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
    <soap:Body>
        <samlp:Response xmlns:samlp="urn:oasis:names:tc:SAML:2.0:protocol">
            <!-- SAML Response content -->
        </samlp:Response>
    </soap:Body>
</soap:Envelope>
"""

saml_response = parse_soap_saml(soap_envelope)
print(saml_response)
