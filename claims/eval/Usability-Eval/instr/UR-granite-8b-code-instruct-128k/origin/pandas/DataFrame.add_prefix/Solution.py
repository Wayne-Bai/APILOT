import pandas as pd

# Assuming you have a pandas Series or DataFrame called 'data'
data.index = ['prefix_' + str(i) for i in data.index]
