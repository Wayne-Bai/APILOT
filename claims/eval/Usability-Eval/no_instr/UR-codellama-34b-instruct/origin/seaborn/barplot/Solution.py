
import seaborn as sns

# Load data
data = pd.read_csv("data.csv")

# Create figure with Seaborn
fig, ax = plt.subplots(figsize=(10, 6))
sns.set(style="whitegrid")

# Plot point estimates and errors as rectangular bars
ax.bar(x=data["group"], y=data["point_estimate"], yerr=data["error"])

# Add title and labels
ax.set_title("Point Estimates and Errors")
ax.set_ylabel("Point Estimate")
ax.set_xlabel("Group")

# Show plot
plt.show()
