import tensorflow as tf
import os

# Function to summarize log files
def summarize_log_files(log_directory):
    # Combine all logs into a single text file
    combined_logs = open(os.path.join(log_directory, 'combined_logs.txt'), 'w')

    for file_name in os.listdir(log_directory):
        file_path = os.path.join(log_directory, file_name)
        if os.path.isfile(file_path):
            with open(file_path, 'r') as file:
                for line in file:
                    combined_logs.write(line)

    combined_logs.close()

# Define the log directory
log_directory = './logs'

# Check if the log directory exists, create if not
if not os.path.exists(log_directory):
    os.makedirs(log_directory)

# Generate the summary file writer
summarize_log_files(log_directory)
