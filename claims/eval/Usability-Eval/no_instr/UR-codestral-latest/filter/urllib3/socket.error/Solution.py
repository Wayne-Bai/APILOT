import requests
import socket

def fetch_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error in case of unsuccessful request
        return response.text
    except requests.RequestException as err:
        log_error(f"Request failed: {err}")
    except socket.error as err:
        log_error(f"Socket error occurred: {err}")

def log_error(error):
    with open("agent_log_file.txt", "a") as file:  # Append errors to log file
        file.write(f"{error}\n")
