import pyrad.packet

# Create a new packet authenticator
def create_packet_authenticator(packet_type, secret, authenticator=None):
    """
    Create a new packet authenticator.

    :param packet_type: The type of packet (e.g. Access-Request, Access-Accept)
    :param secret: The shared secret used for encryption
    :param authenticator: The authenticator value (if not specified, a random value will be generated)
    :return: The authenticator value
    """
    authenticator = authenticator or pyrad.packet.Authenticator(packet_type, secret)
    return authenticator

# Example usage:
packet_type = pyrad.packet.AuthType.AccessRequest
secret = b'secret123'
authenticator = create_packet_authenticator(packet_type, secret)
print("Authenticator:", authenticator)

# Create a new packet with the authenticator
packet = pyrad.packet.AuthPacket(packet_type, secret, authenticator)
print("Packet code:", packet.code)
print("Packet id:", packet.id)
print("Packet authenticator:", packet.authenticator)
