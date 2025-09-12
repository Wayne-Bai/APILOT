
# Importing the required modules from pyrad 
from pyrad.server import Server
from pyrad.packet import AccessRequest, AccessAccept, AccessReject

# Creating a packet authenticator
class PacketAuthenticator(Server):
    def __init__(self, address="localhost", port=1812, secret=b"radiussecret", dict=None):
        Server.__init__(self, dict)
        self.address = address
        self.port = port
        self.secret = secret

    def _CreateReplyPacket(self, packet):
        reply = self.CreateReplyPacket(packet)
        return reply

    def _SendReplyPacket(self, reply):
        reply.source = (self.address, self.port)
        self.SendReplyPacket(reply) 
