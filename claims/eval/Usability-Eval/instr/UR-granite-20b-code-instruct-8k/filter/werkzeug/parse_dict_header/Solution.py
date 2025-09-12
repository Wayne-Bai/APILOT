from werkzeug.urls import parse_qs

def parse_key_value_pairs(pairs_string):
    pairs = parse_qs(pairs_string)
    return pairs
