import pandas as pd

def check_all_truthy(df, column):
    return df[column].apply(lambda x: all(x)).all()
