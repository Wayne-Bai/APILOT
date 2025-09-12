from werkzeug.wrappers import Request
from werkzeug.utils import get_json
def parse_json_request(request):
 data = get_json(request)
 return data
