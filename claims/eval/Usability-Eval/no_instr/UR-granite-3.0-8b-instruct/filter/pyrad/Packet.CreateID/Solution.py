import pyrad

# Create a packet ID
packet_id = pyrad.PacketID()

# Set the packet ID
packet_id.set_id(12345)

# Print the packet ID
print(packet_id.get_id())
