import requests
import json

# Replace these values with your actual API URL and authorization token
BASE_URL = "https://your-rhodecode-url.com/api"
AUTH_TOKEN = "your-auth-token"

def get_repository(name=None, id=None):
    headers = {
        'Authorization': 'token ' + AUTH_TOKEN,
        'Content-Type': 'application/json'
    }
    endpoint = ""

    if name:
        endpoint = f"/{name}"
    elif id:
        endpoint = f"/{id}"
    else:
        raise ValueError("Either name or id must be provided.")

    response = requests.get(BASE_URL + "/repos" + endpoint, headers=headers)

    if response.status_code == 200:
        return json.loads(response.text)['result']['members']
    else:
        return None

# Example of usage
print(get_repository(name="my_repo"))
