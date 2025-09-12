from pyrad.packet import Packet

# Function to create a RADIUS packet with an ID
def create_radius_packet():
    # Creating a packet object
    packet = Packet(id=Packet.CreateID())
    return packet

# Create and print the ID of the packet
radius_packet = create_radius_packet()
print(f"Created packet ID: {radius_packet.id}")
