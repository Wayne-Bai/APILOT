import urllib3

# Initialize the urllib3 PoolManager
http = urllib3.PoolManager()

def handle_socket_client(client_socket):
    try:
        # Receive data from the socket client
        data = client_socket.recv(1024)
        
        if data:
            # Prepare the data for sending via HTTP
            encoded_data = data.decode('utf-8')
            response = http.request('POST', 'http://example.com/endpoint', body=encoded_data)
            
            if response.status != 200:
                raise Exception(f"HTTP request failed with status {response.status}")
        
        else:
            raise Exception("No data received from the socket client")
    
    except Exception as e:
        # Log the error to the agent log file
        with open('agent_log.txt', 'a') as log_file:
            log_file.write(f"Error: {str(e)}\n")

# Example usage
# Assuming client_socket is already connected
handle_socket_client(client_socket)
