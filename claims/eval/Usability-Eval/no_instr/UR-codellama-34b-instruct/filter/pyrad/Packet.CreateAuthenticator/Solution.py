
import pyrad.packet as pp

# Define the authentication parameters
auth_type = "plaintext"
username = "your_username"
password = "your_password"
realm = "your_realm"

# Create a new packet authenticator
authenticator = pp.Authenticator(
    auth_type=auth_type,
    username=username,
    password=password,
    realm=realm,
)
