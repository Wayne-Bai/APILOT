from xml.etree import ElementTree as ET
from pysaml2.samlp import SamlpResponse

def parse_saml_envelope(envelope):
    root = ET.fromstring(envelope)
    response = root.find('.//{urn:oasis:names:tc:SAML:2.0:protocol}Response')
    assertion = response.find('{urn:oasis:names:tc:SAML:2.0:assertion}Assertion')
    assertion_string = ET.tostring(assertion, encoding='unicode')
    return assertion_string

# Usage
saml_envelope = '''
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"
               xmlns:xm="urn:oasis:names:tc:SAML:2.0:protocol">
  <soap:Header>
    <xm:Security>...</xm:Security>
  </soap:Header>
  <soap:Body>
    <xm:Response ID="ID_RESP1"
                 Version="2.0"
                 IssueInstant="2006-07-29T21:45:29.820553Z"
                 Destination="http://example.com/saml-consumer"
                 Consent="urn:oasis:names:tc:SAML:2.0:consent:unspecified"
                 xmlns:xm="urn:oasis:names:tc:SAML:2.0:protocol">
      <xm:Issuer>http://idp.example.org</xm:Issuer>
      <xm:Status>
        <xm:StatusCode Value="urn:oasis:names:tc:SAML:2.0:status:Success" />
      </xm:Status>
      <xm:Assertion ID="_a195d6c6-b100-4813-9e8c-ec2617d6a33e"issueinstant="2006-07-29T21:45:49.031496Z" Version="2.0">
        <!-- ... SAML assertion body ... -->
      </xm:Assertion>
    </xm:Response>
  </soap:Body>
</soap:Envelope>
'''

print(parse_saml_envelope(saml_envelope))
