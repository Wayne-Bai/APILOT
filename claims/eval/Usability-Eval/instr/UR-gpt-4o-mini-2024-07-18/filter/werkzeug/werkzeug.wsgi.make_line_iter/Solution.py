from werkzeug.utils import secure_filename

def safe_iter_line(input_stream):
    try:
        for line in input_stream:
            yield line.strip()
    except Exception as e:
        print(f"An error occurred while iterating: {e}")

# Example usage
if __name__ == "__main__":
    with open("example.txt", "r") as f:
        for line in safe_iter_line(f):
            print(line)
