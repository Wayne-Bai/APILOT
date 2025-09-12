from pysaml2 import saml

def parse_soap_saml_thing(soap_enveloped_saml_thing):
    """
    Parses a SOAP enveloped SAML thing and returns the thing as
    a string.
    """
    saml_thing = saml.SAML().soap_parse(soap_enveloped_saml_thing)
    return saml_thing
