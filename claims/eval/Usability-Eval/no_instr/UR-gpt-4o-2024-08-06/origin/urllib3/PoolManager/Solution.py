import urllib3
from urllib3.exceptions import MaxRetryError, RedirectError

# Define custom redirect function
def custom_redirect_manager(response):
    # Example logic: simply follow redirects up to a certain limit
    if response.status in [301, 302, 303, 307, 308] and 'location' in response.headers:
        # Extract the new location from the headers
        redirect_url = response.headers['location']
        # Log and restrict to a simple example for the purpose of this code
        print(f"Redirecting to {redirect_url}")
        # Ideally, a counter should be implemented to prevent infinite redirects
        return redirect_url
    return None

# Create a PoolManager instance to manage connections
http = urllib3.PoolManager()

# Define the URL and URIs
initial_url = "http://example.com"
request_uri = "/index.html"

try:
    # Set up manual redirects - the responsibility to follow redirects is on the developer
    max_redirects = 3
    for _ in range(max_redirects):
        # Make a request. Here we're using just the request URI portion
        response = http.request(
            'GET',
            initial_url + request_uri,
            redirect=False  # Disable automatic redirects
        )
        
        # Print status or perform operations based on response
        print(f"Response status: {response.status}")
        
        # Check redirect logic
        new_location = custom_redirect_manager(response)
        if new_location:
            # If a redirection URL is found, update the request_uri for the next loop iteration
            request_uri = new_location[len(initial_url):] # assume it's a relative link
        else:
            # If no redirection is needed, break from loop
            break

except MaxRetryError as e:
    # Handle cases where maximum retries are reached
    print(f"Max retry error: {e}")

except RedirectError as e:
    # Handle cases specific to redirection problems
    print(f"Redirect error: {e}")

except Exception as e:
    # General exception catching
    print(f"An error occurred: {e}")

finally:
    # Ensure that the response is properly closed
    response.release_conn()
