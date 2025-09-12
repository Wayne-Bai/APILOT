from pyrad.packet import Packet
from pyrad.dictionary import Dictionary
from pyrad.client import Client

def create_packet_authenticator(client_secret, request_authenticator):
    # Create a dictionary object
    dictionary = Dictionary("path_to_your_dictionary_file")

    # Create a client object
    client = Client(server="radius_server_address", secret=client_secret, dict=dictionary)

    # Create a packet object
    packet = Packet(dict=dictionary)

    # Set the request authenticator
    packet.RequestAuthenticator = request_authenticator

    # Calculate the authenticator
    packet.CreateAuthenticator()

    return packet.authenticator
