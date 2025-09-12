from cryptography.fernet import Fernet

def configure_encryption():
    # Generate a new encryption key
    key = Fernet.generate_key()
    
    # Create a Fernet object with the generated key
    fernet = Fernet(key)
    
    return fernet

# Example usage
if __name__ == "__main__":
    encryption_builder = configure_encryption()
    print("Encryption builder configured successfully.")
