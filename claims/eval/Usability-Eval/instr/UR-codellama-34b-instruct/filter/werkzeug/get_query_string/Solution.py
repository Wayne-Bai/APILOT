import werkzeug

def get_query_string(env):
    return env.get("QUERY_STRING", "")