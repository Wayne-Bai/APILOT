import numpy as np
from collections import Counter

def common_type(arr1, arr2):
    arithmetics = {
        'indexes': arr2, # set to the second array
        'min_size': min(len(arr1), len(arr2)),
    }
    common_type = max(arr1, arithmetics['indexes'])[0:arithmetics['min_size']]
    flattened_common_type = []

    for _ in common_type:
        try:
            flattened_common_type.append(float(_))
        except ValueError:
            pass

    return Counter(flattened_common_type)

arr1 = np.random.randint(1, 100, size=7)
arr2 = np.random.randint(1, 100, size=5)

chart= common_type(arr1, arr2)
print("Common Types\n-----\n", chart)