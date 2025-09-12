import os
from pyrad.packet import AuthPacket

def create_packet_id():
    # Generate a random packet ID between 0 and 255
    return os.urandom(1)[0]

# Example usage:
packet_id = create_packet_id()
print("Generated Packet ID:", packet_id)
