
import numpy as np

# Create sample data
data = np.array([[10, 20, 30],
                 [15, 25, 35],
                 [22, 33, 44]])

# Specify the quantile value
q = 0.5

# Compute the q-th quantile along the specified axis
quantile_result = np.percentile(data, q*100, axis=1)

print("Quantile Result:")
print(quantile_result)
