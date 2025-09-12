import pysaml2

class SAMLParser(pysaml2.claims.SAMLClaims):
    def __init__(self, raw_saml):
        self.raw_saml = raw_saml

    def parse(self):
        soap_envelope = self.raw_saml.split('<?xml version="1.0" encoding="UTF-8"?>\n<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">')[1].split('</soap:Envelope>')[0]
        return str(self.unparse(soap_envelope))
