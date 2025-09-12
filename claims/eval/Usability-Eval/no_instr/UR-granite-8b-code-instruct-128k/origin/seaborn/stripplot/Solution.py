import seaborn as sns

# Draw a categorical scatterplot using jitter to reduce overplotting
sns.catplot(x="category", y="value", hue="category", data=df, kind="strip", jitter=True)
