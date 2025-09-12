# Importing the necessary libraries
import pyrad.packet
import pyrad.dictionary

# Create a dictionary
dict = pyrad.dictionary.Dictionary("d dictionary")

# Create a packet
pkt = pyrad.packet.AuthPacket(code=pyrad.packet.AccessRequest, id=1, secret=b"Your Radius Secret", dict=dict)

# Print the packet
print(pkt)
