import os
from pyrad.packet import AuthPacket
from pyrad.client import Client
from pyrad.dictionary import Dictionary

# Create a client to handle the communication
client = Client(server="radius_server_address", secret=b"radius_secret", dict=Dictionary("path_to_dictionary"))

# Create an authentication packet
request = client.CreateAuthPacket(code=AuthPacket.AccessRequest, User_Name="username")

# Add a password to the request packet (PAP authentication)
request["User-Password"] = request.PwCrypt("password")

# Set the NAS IP Address (Modify this as per actual NAS IP)
request["NAS-IP-Address"] = "192.168.1.1"

# Generate the authenticator
authenticator = os.urandom(16)
request.authenticator = authenticator

print("Generated authenticator:", authenticator)
