from pyrad import Radius
import random

# Generate a unique identifier for the packet
identifier = random.randint(0, 2**31-1)

# Create a new packet authenticator with the generated ID
packet_authenticator = Radius.PacketAuthenticator(identifier)
