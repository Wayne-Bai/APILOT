
from werkzeug import routing

def get_next_segment(path):
    path = routing.normalize_path(path)
    parts = path.split('/')
    next_part = None
    for i, part in enumerate(parts):
        if i == len(parts) - 1:
            break
        next_part = parts[i + 1]
        if not next_part.startswith('{') and not next_part.endswith('}'):
            return next_part
    return None
