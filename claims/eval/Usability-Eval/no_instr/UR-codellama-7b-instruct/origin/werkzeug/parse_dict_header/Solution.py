from werkzeug.wrappers import Request
from werkzeug.routing import Map
from werkzeug.routing import Rule

# Create a werkzeug routing map
map = Map([
    Rule('/', endpoint='index'),
])

# Add custom routing rule to the map
map.add(Rule('/api/keyvaluepairs', endpoint='key_value_pairs'))

# Define an endpoint for the key-value pairs API
@map.endpoint('key_value_pairs')
def key_value_pairs():
    # Get the request data from the Werkzeug Request object
    req = Request()
    data = req.get_data(as_text=True)
    
    # Split the data into a list of key-value pairs
    kvs = [kv.split('=') for kv in data.split(',')]
    
    # Convert the list of key-value pairs to a python dict
    d = {k: v for k, v in kvs}
    
    return jsonify({'key_value_pairs': d})
