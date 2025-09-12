from saml2 import sigver
from saml2.saml import assert_statement_from_string

def parse_soap_enveloped_saml(xmlstr):
    """
    Parses a SOAP enveloped SAML assertion and returns the assertion as a string.
    
    :param xmlstr: XML string containing a SOAP enveloped SAML Assertion.
    :return: SAML Assertion as a string.
    """
    try:
        # Remove SOAP envelope to extract the SAML Assertion
        start_tag = '<saml:Assertion'
        end_tag = '</saml:Assertion>'
        start_idx = xmlstr.find(start_tag)
        end_idx = xmlstr.find(end_tag)

        if start_idx == -1 or end_idx == -1:
            raise ValueError("SAML Assertion not found in the provided XML.")

        saml_assertion = xmlstr[start_idx:end_idx + len(end_tag)]
        
        # Optionally verify the signature
        verified_assertion = sigver.check_signature(saml_assertion)
        
        # Return the assertion if verified
        return verified_assertion if verified_assertion else None
    except Exception as e:
        print(f"Error processing the SAML Assertion: {str(e)}")
        return None
