from pyrad.packet import Packet

def create_packet_id():
    # Create an instance of a Packet
    pkt = Packet()

    # Generate a packet ID
    packet_id = pkt.CreateID()

    # Print the generated packet ID
    print(f"Generated Packet ID: {packet_id.hex()}")

# Example usage
create_packet_id()
