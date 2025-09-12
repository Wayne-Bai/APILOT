
from pysaml2 import saml
import xml.etree.ElementTree as ET

# Load the SAML message from a file
with open("saml_message.xml", "r") as f:
    root = ET.fromstring(f.read())

# Parse the SAML message using pysaml2
context = saml.create_context()
parsed_saml = saml.parse_elementtree(root, context)

# Print the parsed SAML message as a string
print(str(parsed_saml))
