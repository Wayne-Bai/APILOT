import seaborn as sns

# Load the example tips dataset
tips = sns.load_dataset("tips")

# Draw a nested violinplot and split the violins for easier comparison
sns.catplot(x="day", y="total_bill",
            hue="sex", col="time",
            data=tips,
            kind="violin", split=True,
            palette={"Male": "r", "Female": "y"})
