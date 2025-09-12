import pyrad.packet
import struct

class PacketAuthenticator:
    def __init__(self, secret):
        self.secret = secret.encode('utf-8')

    def create_authenticator(self, packet):
        authenticator = self.hmac_md5(packet, self.secret)
        return authenticator

    def hmac_md5(self, packet, secret):
        import hmac
        import hashlib
        auth = hmac.new('md5', secret, packet.Packet.Authenticator)
        return auth.digest()

def create_radius_packet(code, id, secret, authenticator):
    packet = pyrad.packet.AuthPacket(code=code, id=id, secret=secret, authenticator=authenticator)
    return packet

# usage
packet_authenticator = PacketAuthenticator("radius_secret")
packet = create_radius_packet(1, 1, secret="radius_secret", authenticator=packet_authenticator.create_authenticator(packet))
