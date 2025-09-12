import StringIO
from saml2 import validate, VerifyError
from saml2.pack import http_post_form
from saml2.soap import parse_soap_enveloped_saml

def parse_soap_enveloped_saml_soap(env):
    """
    Parse SOAP enveloped SAML and return the assertion as a string.

    :param env: SAML as a http POST form request data
    :type env: StringIO.StringIO
    :return: SAML Assertion as a string
    :rtype: str
    """
    # Extract the SAML assertion from the SOAP enveloped payload
    saml_assertion = parse_soap_enveloped_saml(env.read())

    # Convert the assertion to a string
    saml_assertion_str = http_post_form("%-", {
        "SAMLResponse": saml_assertion,
    })

    return saml_assertion_str


# Test example data
saml_data = """<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/">
    <!-- SOAP Content -->
    <soapenv:Body>
        <saml:Assertion xmlns:saml="urn:oasis:names:tc:SAML:2.0:assertion">
            <!-- SAML 2.0 Assertion content  -->
        </saml:Assertion>
    </soapenv:Body>
</soapenv:Envelope>
"""

saml_env = StringIO.StringIO(saml_data)

try:
    saml_assertion_str = parse_soap_enveloped_saml_soap(saml_env)
    print("SAML Assertion: " + saml_assertion_str)
except VerifyError as e:
    print("Failed SAML verification: " + str(e))
    print("  Error:", e)
