import tensorflow as tf
import numpy as np

def apply_upper_bound(sorted_search_values, values):
    def get_upper_bound(row_sorted_values, row_values):
        upper_bounds = []
        for value in row_values:
            while len(row_sorted_values) > 0 and row_sorted_values[0] < value:
                row_sorted_values = row_sorted_values[1:]
            upper_bounds.append(row_sorted_values[-1] if len(row_sorted_values) > 0 else float('nan'))
        return np.array(upper_bounds)

    return tf.map_fn(lambda row_sorted_values, row_values: get_upper_bound(row_sorted_values, row_values),
                     elems=(sorted_search_values, values), dtype=tf.float32)
