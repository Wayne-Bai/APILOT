import pyrad.packet

def create_packet_id():
    # Create a new RADIUS packet
    packet = pyrad.packet.Packet()
    
    # Generate a unique packet ID
    packet_id = packet.CreateID()
    
    return packet_id

# Example usage
if __name__ == "__main__":
    packet_id = create_packet_id()
    print(f"Generated Packet ID: {packet_id}")
