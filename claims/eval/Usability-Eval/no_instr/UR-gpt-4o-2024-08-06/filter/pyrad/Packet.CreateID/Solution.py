from pyrad.packet import Packet
import pyrad.dictionary

# Load a RADIUS dictionary
dictionary = pyrad.dictionary.Dictionary("dictionary")

# Create a new packet
packet = Packet()

# Assign an ID to the packet
packet_id = packet.CreateID()
print(f"Generated Packet ID: {packet_id}")
