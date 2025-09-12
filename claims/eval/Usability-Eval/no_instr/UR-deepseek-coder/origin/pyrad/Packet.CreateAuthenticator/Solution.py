import pyrad.packet
import pyrad.dictionary

def create_packet_authenticator(secret, username, password):
    # Create a dictionary object for RADIUS attributes
    dictionary = pyrad.dictionary.Dictionary("path_to_your_dictionary_file")

    # Create a RADIUS packet
    packet = pyrad.packet.AuthPacket(dict=dictionary)

    # Set the RADIUS attributes
    packet.add_attribute("User-Name", username)
    packet.add_attribute("User-Password", password)

    # Set the shared secret
    packet.secret = secret.encode('utf-8')

    # Calculate the authenticator
    packet.CreateAuthenticator()

    return packet

# Example usage
secret = "shared_secret"
username = "user123"
password = "password123"

packet = create_packet_authenticator(secret, username, password)
print(packet)
