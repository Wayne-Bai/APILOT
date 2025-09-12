import pyrad.packet

def create_packet_id():
    # Create a new Packet instance
    packet = pyrad.packet.Packet(code=pyrad.packet.AccessRequest)

    # Access the packet id
    packet_id = packet.id

    return packet_id

# Print the packet id
print(create_packet_id())
