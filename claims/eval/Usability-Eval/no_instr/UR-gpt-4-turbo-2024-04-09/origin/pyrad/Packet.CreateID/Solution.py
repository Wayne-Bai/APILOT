from pyrad.packet import Packet

# Create a Packet instance
packet = Packet()

# Generate a packet ID
packet_id = packet.CreateID()

print(f"The generated packet ID is: {packet_id}")
