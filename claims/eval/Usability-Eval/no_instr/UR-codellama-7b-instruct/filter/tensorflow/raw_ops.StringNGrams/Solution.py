
import tensorflow as tf

def create_ngrams(input_strings, n):
    # Convert input strings to a rank-2 tensor (for later processing)
    input_tensor = tf.convert_to_tensor(value=input_strings, dtype=tf.string)
    input_rank_2 = tf.expand_dims(input_tensor, axis=-1)
    
    # Create a list of ngram sizes to iterate over
    ngram_sizes = [n]
    
    # Iterate over the ngram sizes and create the ngrams
    output_strings = []
    for n in ngram_sizes:
        # Create an initial string array with the input strings
        curr_input_array = tf.strided_slice(input=input_rank_2, begin=[0], end=[n])
        
        # Concatenate each row of the input array to create a single ngram
        for i in range(1, len(input_rank_2)):
            curr_input_array = tf.concat([curr_input_array, tf.strided_slice(input=input_rank_2, begin=[i], end=[i+n])], axis=0)
        
        # Add the ngrams to the output list
        output_strings.append(tf.reshape(curr_input_array, [-1]))
    
    # Concatenate all the ngram lists into a single tensor
    output_tensor = tf.concat(output_strings, axis=0)
    
    return output_tensor
