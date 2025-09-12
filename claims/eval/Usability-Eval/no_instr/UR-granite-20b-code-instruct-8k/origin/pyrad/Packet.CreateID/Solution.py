import pyrad

def create_packet_id():
    packet = pyrad.Packet()
    packet.code = 1
    return packet.id
