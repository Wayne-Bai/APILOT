from pyrad.packet import Packet
from pyrad.authentication import Authenticator
from pyrad.dict import Dictionary

# Create a dictionary object
dictionary = Dictionary("path/to/your/dictionary")

# Create a packet
packet = Packet(code=1, identifier=1, secret=b'secret', dict=dictionary)

# Create an authenticator
authenticator = Authenticator(secret=b'secret')

# Generate the packet authenticator
authenticator_value = authenticator.Authenticate(packet)

print(authenticator_value)
