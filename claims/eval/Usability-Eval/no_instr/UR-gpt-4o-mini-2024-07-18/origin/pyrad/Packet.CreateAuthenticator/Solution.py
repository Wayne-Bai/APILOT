import pyrad
from pyrad import packet
from pyrad.dictionary import Dictionary
import hashlib

# Create a new radius server instance
server = pyrad.client.Client(server="localhost", secret=b"secret", dict=Dictionary("path/to/dictionary"))

# Create a new packet
request = server.NewRequest(packet.AccessRequest)

# Function to create a packet authenticator
def create_authenticator(data):
    # Use SHA256 to create a hash as the authenticator
    hasher = hashlib.sha256()
    hasher.update(data)
    return hasher.digest()

# Sample data to be included in the authenticator
sample_data = b"sample_data_for_authentication"
authenticator = create_authenticator(sample_data)

# Assign the authenticator to the request packet
request['Auth-Request'] = authenticator

print("Authenticator generated:", authenticator.hex())
