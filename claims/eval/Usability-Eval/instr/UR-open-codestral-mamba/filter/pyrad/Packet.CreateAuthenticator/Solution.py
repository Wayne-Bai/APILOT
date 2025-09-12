from pyrad.client import Client
from pyrad.dictionary import Dictionary
from pyrad.packet import AccessRequest

# Import RADIUS server details
SERVER = 'localhost'
SECRET = 'testing123'

# Create RADIUS client
client = Client(server=SERVER,
                secret=SECRET,
                dict=Dictionary("dictionary"))

# Create an Access-Request packet
req = client.CreateAuthPacket(code=AccessRequest, User_Name="testuser")
req["User-Password"] = req.PwCrypt("testpassword")

# Send the request and print the reply
reply = client.SendPacket(req)

if reply.code == AccessAccept:
    print("Authentication successful")
else:
    print("Authentication failed")
