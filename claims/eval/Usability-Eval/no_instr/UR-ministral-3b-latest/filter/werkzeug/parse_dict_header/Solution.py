from werkzeug.routing import Map, Rule
from werkzeug.routing.request import Request
from werkzeug.routing.matcher import Matcher

# Imagine we have a list of key-value pairs formatted as strings
url_pairs = [
    "action:post redirect:/home.html",
    "title:New Title",
    "message:Welcome to this site."
]

# Initialize a Map to parse the URL pairs
url_map = Map()

# Function to generate a RouteDict to convert it into a Python dict
def generate_route_dict(url_pairs):
    route_dict = {}
    for pair in url_pairs:
        key, value = pair.split(":", 1)
        route_dict[key] = value
    return route_dict

# Initialize the route dictionary
route_dict = generate_route_dict(url_pairs)
print(route_dict)
