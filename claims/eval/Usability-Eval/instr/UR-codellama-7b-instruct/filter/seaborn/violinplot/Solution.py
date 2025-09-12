import seaborn as sns

# Load the data
data = sns.load_dataset("iris")

# Create a Kernel Density Estimate (KDE) plot
sns.kdeplot(data["petal_length"], shade=True, color="orange", label="Petal Length")

# Add observations or box plot statistics
sns.pointplot(x="species", y="petal_length", data=data, hue="species", markers=["o", "v"])
