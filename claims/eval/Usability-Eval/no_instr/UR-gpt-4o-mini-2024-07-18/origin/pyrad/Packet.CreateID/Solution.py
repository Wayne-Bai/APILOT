import pyrad.packet

# Create a packet ID
def create_packet_id():
    packet = pyrad.packet.Packet()
    packet.ID = packet.new_id()
    return packet.ID

packet_id = create_packet_id()
print(f"Generated Packet ID: {packet_id}")
