# Importing necessary modules from Werkzeug
from werkzeug.utils import iri_to_uri
import urllib.parse as parse

def convert_to_uri(irish_url):
    """
    This function takes an IRI as input and returns a valid URI.
    
    Args:
        irish_url (str): Input IRI to be converted.

    Returns:
        str: Valid URI after conversion.
    """

    try:
        # Using iri_to_uri function to convert IRI to URI
        uri = iri_to_uri(irish_url)
        
        # Now, use the parse function from urllib.parse to correctly encode the URI
        encoded_uri = parse.quote(uri)
        
        return encoded_uri

    except Exception as e:
        # If any exception occurs during the conversion, catch it and print the error message.
        print(f"An error occurred: {str(e)}")

# Example usage:
irish_url = "https://example.com"
print(convert_to_uri(irish_url))
