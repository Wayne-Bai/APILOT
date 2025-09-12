import pyrad.core.packet as packet

def create_packet_id():
    packet_id = packet.PacketID()
    return packet_id.generate()

# Example usage
packet_id = create_packet_id()
print(packet_id)
