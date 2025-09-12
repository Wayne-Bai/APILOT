from werkzeug import request

def get_query_string():
    return request.args

# Example usage
if __name__ == "__main__":
    query_string = get_query_string()
    print(query_string)
