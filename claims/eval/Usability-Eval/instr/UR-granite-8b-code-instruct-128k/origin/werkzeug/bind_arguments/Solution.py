from werkzeug.wrappers import Request
from werkzeug.datastructures import ImmutableMultiDict
# Create a mock request object
args = ImmutableMultiDict([('name', 'John'), ('age', '30'), ('city', 'New York')])
environ = {'REQUEST_METHOD': 'GET'}
request = Request(environ, shallow=True)
request.args = args
# Bind the arguments into a dict
args_dict = request.args.to_dict()
print(args_dict)
# Output: {'name': ['John'], 'age': ['30'], 'city': ['New York']}
