import pandas as pd
df = pd.read_csv("data.csv")
window = df["value"].rolling(2)
window.mean()