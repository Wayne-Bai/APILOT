import tensorflow as tf

class AsynchronousIterator:
    def __init__(self, iterable, buffer_size=10):
        self.iterable = iterable
        self.buffer_size = buffer_size
        self.buffer = tf.data.FIFOQueue(capacity=buffer_size, dtypes=[tf.int64])
        self.iterator = tf.data.Iterator.from_structure(tf.data.Dataset.from_tensor_slices(iterable).batch(buffer_size).take(buffer_size).output_types([tf.int64]))
        self.iterator = self.iterator.make_initializer(self.buffer.destroy)

    def __iter__(self):
        return self

    def __next__(self):
        try:
            return self.buffer.get().numpy()
        except tf.errors.OutOfRangeError:
            self.buffer.clear()
            raise StopIteration

# Example usage:
iterable = [1, 2, 3, 4, 5]
async_iterator = AsynchronousIterator(iterable)

for item in async_iterator:
    print(item)
