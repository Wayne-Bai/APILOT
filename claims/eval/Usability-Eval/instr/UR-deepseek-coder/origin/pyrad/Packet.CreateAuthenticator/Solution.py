import pyrad.packet
import pyrad.dictionary

def create_packet_authenticator(secret, request_authenticator):
    # Create a RADIUS packet
    packet = pyrad.packet.Packet(dict=pyrad.dictionary.Dictionary("path_to_dictionary_file"))
    
    # Set the shared secret
    packet.secret = secret.encode('utf-8')
    
    # Set the request authenticator
    packet.authenticator = request_authenticator
    
    # Calculate the response authenticator
    response_authenticator = packet.CreateAuthenticator()
    
    return response_authenticator

# Example usage
secret = "shared_secret"
request_authenticator = b'\x00' * 16  # Example request authenticator
authenticator = create_packet_authenticator(secret, request_authenticator)
print("Response Authenticator:", authenticator)
