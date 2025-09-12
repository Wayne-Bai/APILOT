# Import the necessary modules from pyrad
from pyrad.packet import Packet
from pyrad.dictionary import Dictionary

# Initialize the dictionary (use appropriate dictionary path)
# Typically, pyrad comes with dictionaries which might need to be loaded
# example: dict = Dictionary("path/to/dictionary")
dict = Dictionary()

# Create a new Radius packet
packet = Packet(dict=dict)

# Generate a packet ID
packet_id = packet.CreateID()

print(f"The generated packet ID is: {packet_id}")
