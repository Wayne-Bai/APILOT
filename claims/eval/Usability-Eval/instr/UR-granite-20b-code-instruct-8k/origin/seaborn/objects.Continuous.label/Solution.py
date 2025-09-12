import seaborn as sns

# Set the style to whitegrid
sns.set(style="whitegrid")

# Load the example tips dataset
tips = sns.load_dataset("tips")

# Draw a nested histogram by speaker and day
g = sns.relplot(x="total_bill", y="tip", hue="day", col="sex",
                kind="hist", height=3, aspect=.7, palette="pastel",
                legend=False, multiple="stack")

# Show the plot
sns.despine(offset=10, trim=True)
plt.show()
