import joblib

def load_object_from_file(file_name):
    loaded_object = joblib.load(file_name)
    return loaded_object
