
import pyrad.packet

# Define the authentication method and parameters
auth_method = "PAP"
username = "myuser"
password = "mypass"

# Create a new PyRAD packet object
pkt = pyrad.packet.Packet()

# Set the packet type to Access-Request
pkt.code = pyrad.packet.AccessRequest

# Set the username and password attributes
pkt.attributes["User-Name"] = username
pkt.attributes["User-Password"] = password

# Set the authentication method attribute
pkt.attributes["Auth-Method"] = auth_method

# Create a new RADIUS client object
client = pyrad.client.Client("127.0.0.1", 1812)

# Send the packet to the RADIUS server
response = client.send(pkt)

# Check if the response is a success
if response.code == pyrad.packet.AccessAccept:
    print("Authentication successful!")
else:
    print("Authentication failed with code %d" % response.code)
