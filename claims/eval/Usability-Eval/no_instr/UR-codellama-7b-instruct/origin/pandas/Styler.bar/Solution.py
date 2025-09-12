
import pandas as pd

# create a sample dataframe
data = {'A': [10, 20, 30], 'B': [40, 50, 60]}
df = pd.DataFrame(data)

# draw bar chart in the cell backgrounds
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.bar(x=['A', 'B'], height=df['A'])
ax.set_xticks(labels=['A', 'B'])
plt.show()
