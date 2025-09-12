from pyrad.packet import Packet
from pyrad.dictionary import Dictionary

def create_packet_authenticator(packet_data):
    # Create a dictionary object
    dictionary = Dictionary()

    # Create a packet object
    packet = Packet(dict=dictionary)

    # Set the packet data
    packet.raw_attributes = packet_data

    # Generate the authenticator
    authenticator = packet.CreateAuthenticator()

    return authenticator

# Example usage
packet_data = {
    "User-Name": "example_user",
    "User-Password": "example_password"
}

authenticator = create_packet_authenticator(packet_data)
print("Generated Authenticator:", authenticator)
