import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Assuming df is your DataFrame and it has 'estimate' and 'error' columns
sns.set(style="whitegrid")
ax = sns.barplot(x=df.index, y="estimate", yerr="error", data=df)
plt.show()
