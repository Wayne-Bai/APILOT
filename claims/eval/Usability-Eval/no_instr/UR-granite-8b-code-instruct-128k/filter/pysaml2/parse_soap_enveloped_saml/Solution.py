from saml2.saml import soapenv_to_string

def parse_soap_saml(soap_envelop):
    saml_thing = soapenv_to_string(soap_envelop)
    return saml_thing
