import tensorflow as tf

# Create a ragged tensor of string data
string_data = tf.ragged.constant(
    [
        ["hello", "world"],
        [""],  # empty string
        ["tensorflow", "is", "awesome"],
        ["",
         "ragged",
         "tutorial"]
    ]
)

# Define a function to create n-grams
def create_ngrams(string_data, n):
    """
    Creates n-grams from ragged string data.

    Args:
    string_data: Ragged Tensor of string data.
    n: Integer, number of characters to extract at a time.

    Returns:
    Ragged Tensor of extracted n-grams.
    """
    # Convert the string data to a ragged tensor of integers (character codes)
    integer_data = tf.ragged.map_flat_values(lambda s: tf.strings.ascii녁to_int(s), string_data)
    
    # Create n-grams by extracting substrings of size n
    ngrams = tf.strings.ngrams(integer_data, n)
    
    return ngrams

# Create 3-grams from the string data
ngrams = create_ngrams(string_data, 3)

# Print the result
print(ngrams)
