from werkzeug.utils import get_current_url

def get_script_name():
    return get_current_url()

# Test
print(get_script_name())
