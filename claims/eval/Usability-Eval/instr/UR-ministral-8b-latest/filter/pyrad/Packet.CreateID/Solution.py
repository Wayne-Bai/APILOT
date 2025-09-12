import pyrad

# Replace these values with your actual AAA setup
radius_shared_secret = 'your_shared_secret'
radius_authentication_port = 1812
radius_accounting_port = 1813
radius_ip_address = 'radius_server_ip_address'

# Create a server instance
server = pyrad.packet.Packet()

# Set the shared secret for authentication
server['Acct-Interim-Interval'] = '30'
server['R1-ACCT'] = 'on'

# Let's create a packet ID example
server['NAS-Identifier'] = 'your_nas_identifier'
server['User-Name'] = 'username'

# Code for creating a packet ID
packet_id = server['Packet-ID']

# Display the generated packet ID
print('Generated Packet ID:', packet_id)
