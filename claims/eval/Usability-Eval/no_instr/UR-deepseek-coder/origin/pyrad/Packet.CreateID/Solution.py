import pyrad.packet

# Create a RADIUS packet with a specific ID
packet = pyrad.packet.Packet(id=123)

# Print the packet ID
print(f"Packet ID: {packet.id}")
