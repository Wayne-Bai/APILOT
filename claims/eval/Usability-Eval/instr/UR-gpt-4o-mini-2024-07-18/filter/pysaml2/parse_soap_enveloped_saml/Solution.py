from pysaml2 import saml, SamlBase


def parse_saml_soap_envelope(soap_envelope):
    # Extract the SAML assertion from the SOAP envelope
    try:
        # Assuming the SOAP envelope has a specific structure
        # Parse the envelope to find the SAML assertion
        start_tag = "<saml:Assertion"
        end_tag = "</saml:Assertion>"

        start_index = soap_envelope.find(start_tag)
        end_index = soap_envelope.find(end_tag, start_index)

        if start_index == -1 or end_index == -1:
            raise ValueError("SAML Assertion not found in the SOAP envelope.")

        saml_assertion = soap_envelope[start_index:end_index + len(end_tag)]
        
        return saml_assertion

    except Exception as e:
        print(f"Error parsing SAML SOAP envelope: {e}")
        return None


# Example usage
soap_envelope = """<soap:Envelope>...<saml:Assertion ...>...</saml:Assertion>...</soap:Envelope>"""
saml_assertion = parse_saml_soap_envelope(soap_envelope)
print(saml_assertion)
