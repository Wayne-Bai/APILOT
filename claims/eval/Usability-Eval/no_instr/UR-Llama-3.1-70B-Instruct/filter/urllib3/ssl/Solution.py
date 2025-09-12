import urllib3
import ssl

def main():
    # Create a pool manager
    http = urllib3.PoolManager()

    # Define a URL to request
    url = "https://www.example.com"

    try:
        # Request a URL with SSL verification
        response = http.request('GET', url)
        
        # Print the status code
        print(f"Status Code: {response.status}")
        
        # Print the data received from the server
        print(f"Received Data: {response.data}")
        
    except urllib3.exceptions.SSLError as e:
        # Print any SSL verification errors
        print(f"SSL Error: {e}")
        
    except urllib3.exceptions.HTTPError as e:
        # Print any HTTP errors
        print(f"HTTP Error: {e}")
        
    except Exception as e:
        # Print any other errors
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
