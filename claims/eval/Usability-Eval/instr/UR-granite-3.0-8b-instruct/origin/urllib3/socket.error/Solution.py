import urllib3

def handle_socket_client(client_socket):
    http = urllib3.PoolManager()

    try:
        response = http.request('GET', client_socket)
        # Process the response here
    except Exception as e:
        # Write the error to the agent log file
        with open('agent_log.txt', 'a') as log_file:
            log_file.write(f'Error: {str(e)}\n')
