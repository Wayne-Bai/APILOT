from pyrad.dictionary import Dictionary
from pyrad.packet import CoAPPacket, StringAttribute, IntegerAttribute
import random

# Load the CoAP dictionary
dictionary = Dictionary("dictionary.txt")

# Create a CoAP packet
packet = CoAPPacket(code=CoAPPacket.Code.Post, id=random.randint(0, 65535))

# Add an attribute to the packet
packet["SomeAttribute"] = IntegerAttribute(dictionary["SomeAttribute"], 123)

# Generate a random authentication token
packet["AuthToken"] = IntegerAttribute(dictionary["AuthToken"], random.randint(0, 65535))

# Sign the packet
packet.sign(key=b"SharedSecret")
