
import seaborn as sns

# Load your data into a pandas dataframe
df = pd.read_csv("your_data.csv")

# Create a new column that assigns each row to a categorical bin
df["bin"] = pd.cut(df["column_name"], bins=[0, 1, 2, 3])

# Use Seaborn's barplot function to create the plot
sns.barplot(x="bin", y="count", data=df)
