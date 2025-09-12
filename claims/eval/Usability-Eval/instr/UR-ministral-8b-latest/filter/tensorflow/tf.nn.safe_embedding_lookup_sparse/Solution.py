import tensorflow as tf

# Assuming `lookup_table` is the lookup table and it's a pre-defined table
# This is a hypothetical lookup table for demonstration purposes
lookup_table = {
    0: "embedding_0",
    1: "embedding_1",
    2: "embedding_2",
    3: "embedding_3"
}

def valid_and_empty_check(ids, features):
    # Check for invalid IDs
    invalid_ids = [id for id in ids if id not in lookup_table]
    if invalid_ids:
        print(f"Invalid IDs found: {invalid_ids}")

    # Check for empty features
    empty_features = [features for i, features in enumerate(ids) if not features]
    if empty_features:
        print(f"Empty features found at indices: {empty_features}")

    return valid_ids, non_empty_features

ids = [0, 1, 2, 4, '', '']
features = [None, None, None, None, None, None]

valid_ids, non_empty_features = valid_and_empty_check(ids, features)
print(f"Valid IDs: {valid_ids}")
print(f"Non-empty features: {non_empty_features}")

# Conducting the lookup
embeddings = [lookup_table[id] for id in valid_ids if id in lookup_table]
print(f"Retrieved embeddings: {embeddings}")
