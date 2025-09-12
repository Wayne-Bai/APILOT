
import tensorflow as tf

def convert_raw_bytes(input_tensor):
    # Use tf.strings.decode to decode the raw bytes into a string
    decoded_string = tf.strings.decode(input_tensor, output_encoding="utf-8")
    
    # Split the decoded string into individual elements
    elements = tf.strings.split(decoded_string)
    
    # Use tf.io.parse_example to parse each element as a example
    parsed_examples = []
    for i, element in enumerate(elements):
        parsed_example = tf.io.parse_example(element, tf.feature_description({
            "key": tf.io.FixedLenFeature([], tf.string),
            "value": tf.io.FixedLenFeature([], tf.int64)
        }))
        parsed_examples.append(parsed_example["value"][0])
    
    # Concatenate the parsed examples into a single tensor
    concatenated = tf.concat(parsed_examples, axis=0)
    
    return concatenated
