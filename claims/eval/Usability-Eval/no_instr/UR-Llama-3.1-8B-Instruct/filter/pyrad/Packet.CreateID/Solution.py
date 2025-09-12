# Import the pyrad module
from pyrad.server import PacketIDManager

# Create a packet ID
packet_id_manager = PacketIDManager()

# Get a new packet ID
packet_id = packet_id_manager.create_packet_id()

print(packet_id)
