
from werkzeug.http import parse_www_authenticate

# Define the authentication challenge as a string
challenge = "Basic realm=\"Secure Area\""

# Parse the challenge using the parse_www_authenticate function
parsed_challenge = parse_www_authenticate(challenge)

# Print the scheme and parameters of the authentication challenge
print("Scheme:", parsed_challenge.scheme)
print("Parameters:", parsed_challenge.params)
