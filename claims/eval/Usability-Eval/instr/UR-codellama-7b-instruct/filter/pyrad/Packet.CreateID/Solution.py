
from pyrad import PacketID

# Create a new Packet ID
packet_id = PacketID()

# Set the packet ID type
packet_id.set_type(PacketID.Type.ID)

# Set the packet ID value
packet_id.set_value(1234567890)

# Get the packet ID value
print(packet_id.get_value())
