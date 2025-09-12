from sklearn import preprocessing
#Assuming you have a numpy array called "data"
data_normalized = preprocessing.scale(data)
data_original_space = preprocessing.inverse_transform(data_normalized)
