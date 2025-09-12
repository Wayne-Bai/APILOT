from sklearn.datasets import load_boston

def load_house_price_dataset():
    boston = load_boston()
    return boston

boston_data = load_house_price_dataset()
print(boston_data.keys())
