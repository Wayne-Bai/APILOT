import pandas as pd

def last_n_rows(df, n):
    return df.iloc[-n:]

# Testing with a sample DataFrame
data = {'Name': ['John', 'Anna', 'Mike', 'Laura'],
        'Age': [30, 25, 35, 28]}
df = pd.DataFrame(data)
n = 2
print(last_n_rows(df, n))
