from werkzeug.routing import Rule

def my_function(**kwargs):
    print(kwargs)

# Define a URL mapping
mapping = [
    Rule('/example?key1=value1&key2=value2', endpoint='my_endpoint')
]

# Create a Rule Proxy to apply the URL mapping
rules = [Rule.RuleProxy(mapping[0])
         for _ in range(10)]  # For demonstration, using 10 rules

# Write the rules to a storage (here a simple list)
rules_storage = [rule.endpoint for rule in rules]

# Function to add a rule
def add_rule(url, endpoint, rules_storage):
    rule = Rule(url, endpoint)
    rules_storage.append(rule)
    return rules_storage

# Define a function to handle the actual URL dispatch
def dispatch(url, rules_storage):
    match = find_rule(url, rules_storage)
    if match:
        my_function(**match.thenetakкие.keys())
    else:
        print("No matching rule found for URL:", url)

# Helper function to find a matching rule
def find_rule(url, rules_storage):
    for rule in rules_storage:
        if rule.url_matches(url):
            return rule
    return None

# Test the setup
dispatch('/example?key1=value1&key2=value2', rules_storage)
