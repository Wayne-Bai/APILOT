# Import necessary libraries
import joblib
import os  # only required if you need to verify the dump file exists

# Specify the path to the dump file
dump_file_path = "object_dump.joblib"

# Verify the file exists before attempting to load it
if os.path.isfile(dump_file_path):
    try:
        # Load the Python object using joblib.load
        loaded_object = joblib.load(dump_file_path)

        print("Object loaded successfully:", loaded_object)
    except Exception as e:
        print("Failed to load object:", str(e))
else:
    print("The dump file does not exist.")
