import pyrad
from pyrad.packet import Packet

# Create an instance of the RADIUS packet
packet = Packet(
    code=pyrad.packet.AccessRequest,
    authenticator=pyrad.packet.RandomVector(16),
    attributes=[
        # Add any attributes you want to include in the packet here
        pyrad.packet.UserName("username"),
        pyrad.packet.UserPassword("password"),
    ],
)

# Generate the packet ID
packet_id = packet.identifier

print(f"Packet ID: {packet_id}")
