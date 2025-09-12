import pandas as pd

def check_all_truthy(df):
    return (df != 0).all().all()
