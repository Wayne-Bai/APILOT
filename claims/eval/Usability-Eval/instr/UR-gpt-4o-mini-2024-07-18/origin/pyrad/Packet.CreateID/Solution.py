import pyrad.packet
import pyrad.client

# Function to create a packet with a unique ID
def create_packet(client, code, request_id):
    packet = client.CreateAuthPacket(code=code, request_id=request_id)
    return packet

# Example usage
if __name__ == "__main__":
    # Setup the client
    client = pyrad.client.Client(server="localhost", secret=b"secret_key", dict=pyrad.dictionary.Dictionary("path_to_dictionary_file"))
    
    # Create an Access-Request packet with a specific request ID
    packet_id = 1  # You can replace this with a dynamically generated ID if required
    access_request_packet = create_packet(client, pyrad.packet.AccessRequest, packet_id)
    
    print(f"Created packet with ID: {packet_id}")
