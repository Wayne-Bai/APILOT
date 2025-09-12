
import packet

# Create a new packet object
pkt = packet.Packet()

# Set the Ethernet header values
pkt.eth_src = '00:11:22:33:44:55'
pkt.eth_dst = '66:77:88:99:aa:bb'
pkt.eth_type = packet.ETHERTYPE_IPv4

# Set the IP header values
pkt.ip_src = '192.168.0.1'
pkt.ip_dst = '192.168.0.2'
pkt.protocol = packet.PROTOCOL_UDP

# Set the UDP header values
pkt.udp_src = 12345
pkt.udp_dst = 54321

# Create a packet ID using the PyRad library
packet_id = pkt.create_packet_id()
