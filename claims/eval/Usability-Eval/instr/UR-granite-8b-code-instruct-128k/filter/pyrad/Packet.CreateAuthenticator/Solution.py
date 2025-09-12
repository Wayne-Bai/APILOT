import pyrad

def create_packet_authenticator(packet):
    authenticator = pyrad.create_authenticator()
    return authenticator
