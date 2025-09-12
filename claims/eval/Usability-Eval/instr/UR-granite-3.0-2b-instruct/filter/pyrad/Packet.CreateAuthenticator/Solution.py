from pyrad.packet_authenticator import PacketAuthenticator

# Create a packet authenticator
authenticator = PacketAuthenticator()

# Set the secret key for authentication
authenticator.set_secret_key("your_secret_key")

# Generate a packet for authentication
packet = authenticator.generate_packet()

# Send the packet to the server
# Replace 'server_ip' and 'server_port' with the actual server address and port
# Replace 'packet' with the generated packet
# Use the appropriate library to send the packet to the server (e.g., socket, requests, etc.)
