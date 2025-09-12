from pyrad import PacketAuthenticator

# Create a packet authenticator
authenticator = PacketAuthenticator()

# Set the secret key for authentication
authenticator.set_secret_key("your_secret_key")

# Now you can use the authenticator to authenticate packets
# For example, to authenticate a packet:
packet = b"your_packet_data"
authenticated_packet = authenticator.authenticate(packet)

# The authenticated_packet is now a cryptographically secure authentication tag
