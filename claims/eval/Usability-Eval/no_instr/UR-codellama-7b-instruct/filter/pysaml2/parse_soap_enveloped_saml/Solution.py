
import pysaml2

def parse_soap_envelope(xml):
    # Parse the SOAP envelope
    envelope = etree.fromstring(xml)
    namespace = '{http://www.w3.org/2003/05/soap-envelope}'

    # Find the SAML thing in the envelope
    thing_element = envelope.find('.//{}things', namespaces={'': namespace})
    if thing_element is not None:
        return etree.tostring(thing_element, encoding='unicode')
    else:
        raise ValueError('No SAML thing found in the envelope')
