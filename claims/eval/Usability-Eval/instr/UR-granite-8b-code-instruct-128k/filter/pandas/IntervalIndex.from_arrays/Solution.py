import pandas as pd

def construct_from_bounds(left_bounds, right_bounds):
    # code to construct from two arrays defining the left and right bounds
    constructed_array = []
    
    for i in range(len(left_bounds)):
        constructed_array.append([left_bounds[i], right_bounds[i]])
    
    return pd.DataFrame(constructed_array, columns=['left', 'right'])
