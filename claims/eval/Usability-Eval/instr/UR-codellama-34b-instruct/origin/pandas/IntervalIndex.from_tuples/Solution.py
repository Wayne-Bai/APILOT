import pandas as pd

def construct_intervalindex_from_tuples(tuples):
    # Create an empty IntervalIndex object
    interval_index = pd.IntervalIndex([])

    # Loop through the tuples and add them to the IntervalIndex
    for tuple in tuples:
        interval_index.append(pd.Interval(tuple[0], tuple[1]))

    return interval_index
