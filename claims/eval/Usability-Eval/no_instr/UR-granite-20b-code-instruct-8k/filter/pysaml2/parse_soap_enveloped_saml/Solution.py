from pysaml2 import soap

def parse_soap_enveloped_saml_thing(thing):
    return soap.to_string(thing)
