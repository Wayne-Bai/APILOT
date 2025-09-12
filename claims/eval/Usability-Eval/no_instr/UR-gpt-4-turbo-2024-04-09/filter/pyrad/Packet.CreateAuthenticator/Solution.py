from pyrad.packet import AuthPacket
from pyrad.client import Client
from pyrad.dictionary import Dictionary

# Initialize the client with server address and secret
client = Client(server="radius.server.address", secret=b"radius_secret", dict=Dictionary("path/to/dictionary"))

# Create an authentication packet
request = client.CreateAuthPacket(code=AuthPacket.AccessRequest, User_Name="username")

# Add a password attribute to the request
request["User-Password"] = request.PwCrypt("password")

print("Packet authenticator:", request.authenticator)
