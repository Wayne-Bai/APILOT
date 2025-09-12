import tensorflow as tf

class SummaryWriter:
    def __init__(self, log_dir):
        self.log_dir = log_dir
        self.summary_writer = tf.summary.create_file_writer(log_dir)

    def open(self):
        with self.summary_writer.as_default():
            print(f"Opened summary writer for log directory: {self.log_dir}")

    def close(self):
        self.summary_writer.close()
        print("Summary writer closed")

    def write(self, tag, value, step):
        with self.summary_writer.as_default():
            tf.summary.scalar(tag, value, step=step)
            print(f"Wrote scalar with tag: {tag}, value: {value}, at step: {step}")

# Example usage:
# log_directory = 'logs'
# writer = SummaryWriter(log_directory)
# writer.open()
# writer.write('loss', 0.1, 1)
# writer.close()
