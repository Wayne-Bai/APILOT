from cryptography.hazmat.primitives.serialization import load_ssh_private_key
from cryptography.hazmat.backends import default_backend

# Function to deserialize an OpenSSH private key
def deserialize_ssh_private_key(ssh_private_key_data: bytes):
    # Load the private key using the modern API
    private_key = load_ssh_private_key(ssh_private_key_data, backend=default_backend())
    return private_key

# Example usage
if __name__ == "__main__":
    # Replace this with your actual SSH private key data
    ssh_private_key_data = b"your_open_ssh_private_key_data_here"
    
    private_key = deserialize_ssh_private_key(ssh_private_key_data)
    print(private_key)
