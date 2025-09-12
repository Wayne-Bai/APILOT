from werkzeug.datastructures import MultiDict

# Function to parse the query string into a dict
def parse_query_string(query_string):
    parsed_qs = MultiDict(query_string)
    data_dict = {key: list(parsed_qs.getlist(key)) for key in parsed_qs.keys()}
    return data_dict

# Usage example
query_string = "name=John&age=30&skills=python&skills=java"
parsed_dict = parse_query_string(query_string)
print(parsed_dict)
