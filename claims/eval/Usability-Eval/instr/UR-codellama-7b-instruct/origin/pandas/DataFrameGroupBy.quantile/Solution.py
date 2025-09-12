import pandas as pd

# create some sample data
data = {'Age': [25, 31, 36, 22, 45, 52, 18, 29, 37],
        'Gender': ['Male', 'Female', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female']}
df = pd.DataFrame(data)

# calculate the 25th, 50th, and 75th percentiles of the data
q1 = df.quantile(q=0.25)['Age']
q2 = df.quantile(q=0.5)['Age']
q3 = df.quantile(q=0.75)['Age']

# print the results
print("The 25th percentile is {}. The 50th percentile is {}. The 75th percentile is {}.".format(q1, q2, q3))
