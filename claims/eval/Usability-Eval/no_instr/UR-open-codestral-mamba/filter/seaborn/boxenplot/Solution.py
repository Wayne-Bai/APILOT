import seaborn as sns
import matplotlib.pyplot as pl
import numpy as np

# Assuming you have a data frame 'df'
df = sns.load_dataset('tips')

pl.figure(figsize=(10,8))

# Draw enhanced box plot
plot = sns.boxplot(x='day', y='tip', data = df, palette = 'hsv', width=0.6)
sns.swarmplot(x="day", y="tip", data=df, color="yellow", size=5, alpha =0.4)

# Make the plots more readable
plot.set_title('Enhanced box plot', fontsize = 25)
plot.set_xlabel("Day of the week", fontsize = 20)
plot.set_ylabel("Tips ($)", fontsize = 20)

pl.show()
