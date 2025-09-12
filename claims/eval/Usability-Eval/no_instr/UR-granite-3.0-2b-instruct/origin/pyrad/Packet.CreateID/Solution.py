import pyrad.utils.packet as packet

def create_packet_id():
    # Define the packet type
    packet_type = "example_packet_type"

    # Create a new packet
    packet_data = packet.Packet(packet_type)

    # Generate a unique packet ID
    packet_id = packet_data.generate_packet_id()

    return packet_id

# Test the function
packet_id = create_packet_id()
print(packet_id)
