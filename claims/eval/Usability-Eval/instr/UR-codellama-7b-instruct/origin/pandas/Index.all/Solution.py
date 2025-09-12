
import pandas as pd

def check_truthiness(list):
    return all(pd.notnull(element) for element in list)
