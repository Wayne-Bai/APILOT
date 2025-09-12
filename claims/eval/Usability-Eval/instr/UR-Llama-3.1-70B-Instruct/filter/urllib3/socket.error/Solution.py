# Importing urllib3 library
import urllib3

# Disabling warnings for insecure connections
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Function to write errors to the agent log file
def write_to_log_file(error_message):
    """
    Writes error messages to the agent log file.

    Args:
    error_message (str): Error message to be written to the log file.
    """
    try:
        # Open the log file in append mode
        with open('agent_log.txt', 'a') as log_file:
            # Write the error message to the log file
            log_file.write(f"{error_message}\n")
        print(f"Error written to log file: {error_message}")
    except Exception as e:
        # Handle any exceptions that occur while writing to the log file
        print(f"Failed to write to log file: {str(e)}")


# Function to handle socket client errors
def handle_socket_errors(url):
    """
    Handles errors that occur with data received from a socket client.

    Args:
    url (str): URL of the socket client.
    """
    try:
        # Create a urllib3 pool manager
        http = urllib3.PoolManager()

        # Make a GET request to the socket client
        response = http.request('GET', url)

        # Check if the response was successful
        if response.status!= 200:
            # Write the error to the log file
            write_to_log_file(f"Socket client error: {url} returned {response.status}")
    except Exception as e:
        # Write the error to the log file
        write_to_log_file(f"Socket client error: {str(e)}")


# Example usage:
handle_socket_errors('http://example.com')
